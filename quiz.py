import random

from db import get_questions, get_topics, record_attempt
from models import Question, Topic


def _pick_topic() -> Topic:
    """Random topic for now — replaced by scheduler.next_topic() in Phase 5."""
    return random.choice(get_topics())


def next_question() -> tuple[Topic, Question]:
    """Pick a topic, return an existing question or generate a fresh one."""
    topic = _pick_topic()
    questions = get_questions(topic.id)
    if questions:
        return topic, random.choice(questions)

    # No questions yet for this topic — generate one on the fly
    from generator import generate_question
    return topic, generate_question(topic)


def submit_answer(question: Question, user_answer: str) -> tuple[int, float]:
    """Grade *user_answer*, persist the attempt, return (correct 0|1, score 0.0|1.0).

    MCQ: exact case-insensitive match against question.answer.
    Free-text: always scores 0.5 until grader.py is wired in (Phase 6).
    """
    if question.kind == "mcq":
        correct = int(user_answer.strip().lower() == question.answer.strip().lower())
        score = float(correct)
    else:
        correct, score = 0, 0.5  # grader.py will replace this

    record_attempt(question.id, user_answer, correct, score)
    return correct, score
