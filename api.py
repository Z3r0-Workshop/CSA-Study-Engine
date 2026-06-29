from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import db
import quiz


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    db.seed_db()
    yield


app = FastAPI(
    title="CSA Study Engine",
    description="Local-first quiz API for the ServiceNow CSA certification.",
    version="0.1.0",
    lifespan=lifespan,
)


# ── Schemas ───────────────────────────────────────────────────────────────────

class TopicOut(BaseModel):
    id: int
    name: str
    weight: float
    blueprint_notes: str


class QuestionOut(BaseModel):
    id: int
    topic_id: int
    topic_name: str
    stem: str
    kind: str           # "mcq" | "free"
    options: list[str]  # empty for free-text
    source: str         # "seed" | "generated"


class AnswerIn(BaseModel):
    question_id: int
    user_answer: str


class AnswerOut(BaseModel):
    correct: bool
    score: float
    rationale: str      # LLM rationale for free-text; empty for MCQ
    model_answer: str
    explanation: str


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok"}


@app.get("/topics", response_model=list[TopicOut], tags=["study"])
def get_topics():
    """Return all topics ordered by exam weight (highest first)."""
    return [TopicOut(**vars(t)) for t in db.get_topics()]


@app.get("/question", response_model=QuestionOut, tags=["study"])
def get_question():
    """Return the next question chosen by the scheduler.

    The scheduler weights toward topics with high exam importance and low
    recent accuracy, so questions are not random — they target your gaps.
    """
    topic, question = quiz.next_question()
    return QuestionOut(
        id=question.id,
        topic_id=question.topic_id,
        topic_name=topic.name,
        stem=question.stem,
        kind=question.kind,
        options=question.options,
        source=question.source,
    )


@app.post("/answer", response_model=AnswerOut, tags=["study"])
def post_answer(body: AnswerIn):
    """Submit an answer for a question.

    For MCQ supply the exact option text.
    For free-text supply any prose — the LLM grades it 0..1.
    """
    question = db.get_question_by_id(body.question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    correct, score, rationale = quiz.submit_answer(question, body.user_answer)
    return AnswerOut(
        correct=bool(correct),
        score=round(score, 4),
        rationale=rationale,
        model_answer=question.answer,
        explanation=question.explanation,
    )
