from db import get_connection, get_topics
from models import Topic


# ── DB helpers ────────────────────────────────────────────────────────────────

def _rolling_accuracy(topic_id: int, n: int = 10) -> float:
    """Average correctness of the last *n* attempts on this topic's questions.
    Returns 0.5 (neutral) when no attempts exist yet."""
    with get_connection() as conn:
        rows = conn.execute(
            """SELECT a.correct
               FROM attempts a
               JOIN questions q ON a.question_id = q.id
               WHERE q.topic_id = ?
               ORDER BY a.answered_at DESC
               LIMIT ?""",
            (topic_id, n),
        ).fetchall()
    if not rows:
        return 0.5
    return sum(r["correct"] for r in rows) / len(rows)


def _attempt_count(topic_id: int) -> int:
    """Total attempts across all questions in this topic."""
    with get_connection() as conn:
        return conn.execute(
            """SELECT COUNT(*)
               FROM attempts a
               JOIN questions q ON a.question_id = q.id
               WHERE q.topic_id = ?""",
            (topic_id,),
        ).fetchone()[0]


# ── Pure formula (tested directly) ───────────────────────────────────────────

def priority_score(weight: float, recent_accuracy: float, attempt_count: int) -> float:
    """Compute a topic's priority — higher means serve sooner.

    priority = weight × (1 − recent_accuracy) + unseen_bonus

    weight          — exam blueprint importance (0..1)
    recent_accuracy — rolling accuracy over last 10 attempts (0..1, default 0.5)
    attempt_count   — total attempts; 0 triggers the +0.3 unseen bonus
    """
    unseen = 0.3 if attempt_count == 0 else 0.0
    return weight * (1.0 - recent_accuracy) + unseen


# ── Public API ────────────────────────────────────────────────────────────────

def topic_priority(topic: Topic) -> float:
    """Fetch live DB stats for *topic* and return its priority score."""
    return priority_score(
        weight=topic.weight,
        recent_accuracy=_rolling_accuracy(topic.id),
        attempt_count=_attempt_count(topic.id),
    )


def next_topic() -> Topic:
    """Return the topic with the highest priority score."""
    topics = get_topics()
    return max(topics, key=topic_priority)
