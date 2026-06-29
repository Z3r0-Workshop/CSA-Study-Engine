import json
import sqlite3

from config import DB_PATH
from models import Attempt, Question, Topic


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS topics (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT    NOT NULL UNIQUE,
                weight          REAL    NOT NULL,
                blueprint_notes TEXT    NOT NULL DEFAULT ''
            );

            CREATE TABLE IF NOT EXISTS questions (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id    INTEGER NOT NULL REFERENCES topics(id),
                stem        TEXT    NOT NULL,
                kind        TEXT    NOT NULL CHECK(kind IN ('mcq', 'free')),
                options     TEXT    NOT NULL DEFAULT '[]',
                answer      TEXT    NOT NULL,
                explanation TEXT    NOT NULL DEFAULT '',
                source      TEXT    NOT NULL CHECK(source IN ('seed', 'generated')),
                created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS attempts (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                question_id INTEGER NOT NULL REFERENCES questions(id),
                user_answer TEXT    NOT NULL,
                correct     INTEGER NOT NULL CHECK(correct IN (0, 1)),
                score       REAL    NOT NULL,
                answered_at TEXT    NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS votes (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                question_id INTEGER NOT NULL REFERENCES questions(id),
                kind        TEXT    NOT NULL CHECK(kind IN ('up', 'down', 'flag')),
                voted_at    TEXT    NOT NULL DEFAULT (datetime('now'))
            );
        """)


def seed_db() -> None:
    from seed_data import QUESTIONS, TOPICS

    with get_connection() as conn:
        for t in TOPICS:
            conn.execute(
                "INSERT OR IGNORE INTO topics (name, weight, blueprint_notes) VALUES (?,?,?)",
                (t["name"], t["weight"], t["blueprint_notes"]),
            )

        existing = {
            row["stem"]
            for row in conn.execute("SELECT stem FROM questions").fetchall()
        }
        for q in QUESTIONS:
            if q["stem"] in existing:
                continue
            row = conn.execute(
                "SELECT id FROM topics WHERE name = ?", (q["topic"],)
            ).fetchone()
            if row:
                conn.execute(
                    """INSERT INTO questions
                       (topic_id, stem, kind, options, answer, explanation, source)
                       VALUES (?, ?, ?, ?, ?, ?, 'seed')""",
                    (
                        row["id"],
                        q["stem"],
                        q["kind"],
                        json.dumps(q.get("options", [])),
                        q["answer"],
                        q.get("explanation", ""),
                    ),
                )


# ── Read helpers used by other modules ───────────────────────────────────────

def get_topics() -> list[Topic]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM topics ORDER BY weight DESC"
        ).fetchall()
    return [Topic(**dict(r)) for r in rows]


def get_questions(topic_id: int | None = None) -> list[Question]:
    with get_connection() as conn:
        if topic_id is not None:
            rows = conn.execute(
                "SELECT * FROM questions WHERE topic_id = ?", (topic_id,)
            ).fetchall()
        else:
            rows = conn.execute("SELECT * FROM questions").fetchall()
    result = []
    for r in rows:
        d = dict(r)
        d["options"] = json.loads(d["options"])
        result.append(Question(**d))
    return result


def get_question_by_id(question_id: int) -> Question | None:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM questions WHERE id = ?", (question_id,)
        ).fetchone()
    if row is None:
        return None
    d = dict(row)
    d["options"] = json.loads(d["options"])
    return Question(**d)


def get_attempts(question_id: int) -> list[Attempt]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM attempts WHERE question_id = ? ORDER BY answered_at",
            (question_id,),
        ).fetchall()
    return [Attempt(**dict(r)) for r in rows]


def record_attempt(
    question_id: int,
    user_answer: str,
    correct: int,
    score: float,
) -> None:
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO attempts (question_id, user_answer, correct, score)
               VALUES (?, ?, ?, ?)""",
            (question_id, user_answer, correct, score),
        )


def record_vote(question_id: int, kind: str) -> None:
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO votes (question_id, kind) VALUES (?, ?)",
            (question_id, kind),
        )


def get_stats() -> dict:
    with get_connection() as conn:
        topics = conn.execute("SELECT * FROM topics ORDER BY weight DESC").fetchall()
        total_q = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
        total_a = conn.execute("SELECT COUNT(*) FROM attempts").fetchone()[0]

        topic_stats = []
        readiness = 0.0
        for t in topics:
            rows = conn.execute(
                "SELECT correct FROM attempts a JOIN questions q ON q.id = a.question_id "
                "WHERE q.topic_id = ? ORDER BY a.answered_at DESC LIMIT 10",
                (t["id"],),
            ).fetchall()
            attempt_count = conn.execute(
                "SELECT COUNT(*) FROM attempts a JOIN questions q ON q.id = a.question_id "
                "WHERE q.topic_id = ?",
                (t["id"],),
            ).fetchone()[0]
            accuracy = (sum(r["correct"] for r in rows) / len(rows)) if rows else 0.5
            readiness += t["weight"] * accuracy
            q_count = conn.execute(
                "SELECT COUNT(*) FROM questions WHERE topic_id = ?", (t["id"],)
            ).fetchone()[0]
            topic_stats.append({
                "id": t["id"],
                "name": t["name"],
                "weight": t["weight"],
                "accuracy": round(accuracy, 4),
                "attempt_count": attempt_count,
                "question_count": q_count,
            })

        # Question lifecycle counts
        candidate = conn.execute(
            "SELECT COUNT(*) FROM questions WHERE source='generated' AND id NOT IN "
            "(SELECT question_id FROM attempts)"
        ).fetchone()[0]
        active = conn.execute(
            "SELECT COUNT(*) FROM questions WHERE id IN (SELECT question_id FROM attempts)"
        ).fetchone()[0]
        golden_ids = conn.execute(
            "SELECT question_id FROM votes WHERE kind='up' GROUP BY question_id HAVING COUNT(*)>=3"
        ).fetchone()
        golden = conn.execute(
            "SELECT COUNT(*) FROM (SELECT question_id FROM votes WHERE kind='up' "
            "GROUP BY question_id HAVING COUNT(*)>=3)"
        ).fetchone()[0]
        retired = conn.execute(
            "SELECT COUNT(*) FROM (SELECT question_id FROM votes WHERE kind='flag' "
            "GROUP BY question_id HAVING COUNT(*)>=2)"
        ).fetchone()[0]

        # Vote totals per question
        quality_rows = conn.execute(
            """SELECT q.id, t.name as topic_name,
               COUNT(a.id) as attempts,
               SUM(a.correct) as correct_count,
               (SELECT COUNT(*) FROM votes v WHERE v.question_id=q.id AND v.kind='up') as up_votes,
               (SELECT COUNT(*) FROM votes v WHERE v.question_id=q.id AND v.kind='down') as down_votes,
               (SELECT COUNT(*) FROM votes v WHERE v.question_id=q.id AND v.kind='flag') as flag_votes
               FROM questions q
               JOIN topics t ON t.id = q.topic_id
               LEFT JOIN attempts a ON a.question_id = q.id
               GROUP BY q.id HAVING attempts > 0
               ORDER BY attempts DESC LIMIT 10""",
        ).fetchall()

    quality = []
    for r in quality_rows:
        diff = round(r["correct_count"] / r["attempts"], 2) if r["attempts"] else None
        net_votes = r["up_votes"] - r["down_votes"] - r["flag_votes"]
        if r["flag_votes"] >= 2:
            status = "retired"
        elif r["up_votes"] >= 3:
            status = "golden"
        elif diff is not None and diff > 0.9:
            status = "too easy"
        else:
            status = "active"
        quality.append({
            "id": f"Q#{r['id']}",
            "topic": r["topic_name"],
            "difficulty": diff,
            "up_votes": r["up_votes"],
            "down_votes": r["down_votes"],
            "flag_votes": r["flag_votes"],
            "net_votes": net_votes,
            "status": status,
        })

    return {
        "topics": topic_stats,
        "total_questions": total_q,
        "total_attempts": total_a,
        "exam_readiness": round(readiness, 4),
        "lifecycle": {
            "candidate": candidate,
            "active": active,
            "golden": golden,
            "retired": retired,
        },
        "quality": quality,
    }


# ── CLI smoke-test ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    seed_db()

    with get_connection() as conn:
        topics = conn.execute(
            "SELECT * FROM topics ORDER BY weight DESC"
        ).fetchall()
        q_count = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]

        print(f"DB ready -> {DB_PATH.resolve()}")
        print(f"Topics: {len(topics)}   Questions: {q_count}\n")
        for t in topics:
            n = conn.execute(
                "SELECT COUNT(*) FROM questions WHERE topic_id = ?", (t["id"],)
            ).fetchone()[0]
            print(f"  [{t['weight']:.0%}]  {t['name']}  ({n} questions)")
