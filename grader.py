import json
import re

from models import Question
from ollama_client import generate as llm_generate

MAX_RETRIES = 2

_PROMPT = """\
You are grading a ServiceNow CSA exam free-text answer.

Question: {stem}

Model answer: {model_answer}

Student's answer: {user_answer}

Score the student's answer from 0.0 to 1.0:
  1.0 — fully correct, captures the key concept
  0.5 — partially correct, shows some understanding
  0.0 — incorrect or entirely missing the point

Respond with ONLY valid JSON, no other text:
{{"score": 0.8, "rationale": "One sentence explaining the grade."}}"""


def _extract(raw: str) -> dict:
    text = re.sub(r"```(?:json)?\s*", "", raw).strip().rstrip("`").strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError("No JSON object found in grader response")


def _validate(data: dict) -> None:
    if "score" not in data or "rationale" not in data:
        raise ValueError(f"Missing score or rationale: {data}")
    score = float(data["score"])
    if not 0.0 <= score <= 1.0:
        raise ValueError(f"Score {score} out of 0..1 range")


def grade(question: Question, user_answer: str) -> tuple[float, str]:
    """Grade a free-text answer against the model answer.

    Returns (score 0.0..1.0, one-line rationale).
    Falls back to (0.5, 'Could not grade') if LLM output is unparseable.
    """
    prompt = _PROMPT.format(
        stem=question.stem,
        model_answer=question.answer,
        user_answer=user_answer,
    )

    last_err: Exception = RuntimeError("no attempts made")
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            raw = llm_generate(prompt)
            data = _extract(raw)
            _validate(data)
            return float(data["score"]), str(data["rationale"])
        except (ValueError, json.JSONDecodeError, KeyError) as exc:
            last_err = exc

    print(f"  [grader] parse failed after {MAX_RETRIES} attempts: {last_err}")
    return 0.5, "Could not grade — counted as partial credit."


if __name__ == "__main__":
    from db import get_questions, init_db, seed_db

    init_db()
    seed_db()

    q = get_questions()[0]
    print(f"Question : {q.stem}")
    print(f"Model ans: {q.answer}\n")

    user_ans = "I'm not sure but I think " + q.answer
    print(f"Test ans : {user_ans}\n")

    score, rationale = grade(q, user_ans)
    print(f"Score    : {score:.2f}")
    print(f"Rationale: {rationale}")
