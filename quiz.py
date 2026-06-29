import random

from db import get_questions, record_attempt
from models import Question, Topic
from scheduler import next_topic


def _pick_topic() -> Topic:
    return next_topic()


def next_question() -> tuple[Topic, Question]:
    """Pick a topic, return an existing question or generate a fresh one."""
    topic = _pick_topic()
    questions = get_questions(topic.id)
    if questions:
        return topic, random.choice(questions)

    # No questions yet for this topic — generate one on the fly
    from generator import generate_question
    return topic, generate_question(topic)


def submit_answer(question: Question, user_answer: str) -> tuple[int, float, str]:
    """Grade *user_answer*, persist the attempt.

    Returns (correct 0|1, score 0.0..1.0, rationale).
    MCQ:       exact case-insensitive match; rationale is empty (cli shows explanation).
    Free-text: LLM grades via grader.py; score >= 0.6 counts as correct.
    """
    if question.kind == "mcq":
        correct = int(user_answer.strip().lower() == question.answer.strip().lower())
        score, rationale = float(correct), ""
    else:
        from grader import grade
        score, rationale = grade(question, user_answer)
        correct = int(score >= 0.6)

    record_attempt(question.id, user_answer, correct, score)
    return correct, score, rationale
