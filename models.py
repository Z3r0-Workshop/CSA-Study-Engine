from dataclasses import dataclass


@dataclass
class Topic:
    id: int
    name: str
    weight: float
    blueprint_notes: str


@dataclass
class Question:
    id: int
    topic_id: int
    stem: str
    kind: str           # "mcq" | "free"
    options: list[str]  # empty for free-text questions
    answer: str
    explanation: str
    source: str         # "seed" | "generated"
    created_at: str


@dataclass
class Attempt:
    id: int
    question_id: int
    user_answer: str
    correct: int        # 0 or 1
    score: float        # 0.0 .. 1.0
    answered_at: str
