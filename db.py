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


# ── CLI smoke-test ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    seed_db()

    with get_connection() as conn:
        topics = conn.execute(
            "SELECT * FROM topics ORDER BY weight DESC"
        ).fetchall()
        q_count = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]

        print(f"DB ready  →  {DB_PATH.resolve()}")
        print(f"Topics: {len(topics)}   Questions: {q_count}\n")
        for t in topics:
            n = conn.execute(
                "SELECT COUNT(*) FROM questions WHERE topic_id = ?", (t["id"],)
            ).fetchone()[0]
            print(f"  [{t['weight']:.0%}]  {t['name']}  ({n} questions)")
