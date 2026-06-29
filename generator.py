import json
import re

from models import Question, Topic
from ollama_client import generate as llm_generate

MAX_RETRIES = 3

_PROMPT = """\
You are a ServiceNow CSA certification exam question writer.

Generate exactly ONE multiple-choice question for this exam topic.

Topic: {topic_name}
Blueprint context: {blueprint_notes}

Rules:
- The question must test real ServiceNow CSA knowledge
- Provide exactly 4 answer options
- Only ONE option is correct
- The correct answer must be one of the four options verbatim
- Include a one-to-two sentence explanation of why the answer is correct

Respond with ONLY valid JSON — no markdown, no extra text:
{{
  "stem": "Question text ending with a question mark?",
  "options": ["Option A", "Option B", "Option C", "Option D"],
  "answer": "Option A",
  "explanation": "Explanation of why Option A is correct."
}}"""


def _extract(raw: str) -> dict:
    """Pull JSON out of raw LLM text, handling markdown fences and leading prose."""
    text = re.sub(r"```(?:json)?\s*", "", raw).strip().rstrip("`").strip()

    # Try the whole string first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Fall back to finding the first {...} block
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())

    raise ValueError("No JSON object found in LLM response")


def _validate(data: dict) -> None:
    required = {"stem", "options", "answer", "explanation"}
    missing = required - data.keys()
    if missing:
        raise ValueError(f"Missing fields: {missing}")
    if not isinstance(data["options"], list) or len(data["options"]) != 4:
        raise ValueError(f"Expected 4 options, got {data.get('options')}")
    if data["answer"] not in data["options"]:
        raise ValueError(f"Answer '{data['answer']}' not in options {data['options']}")


def _save(topic: Topic, data: dict) -> Question:
    from db import get_connection

    with get_connection() as conn:
        cur = conn.execute(
            """INSERT INTO questions
               (topic_id, stem, kind, options, answer, explanation, source)
               VALUES (?, ?, 'mcq', ?, ?, ?, 'generated')""",
            (
                topic.id,
                data["stem"],
                json.dumps(data["options"]),
                data["answer"],
                data["explanation"],
            ),
        )
        row = conn.execute(
            "SELECT * FROM questions WHERE id = ?", (cur.lastrowid,)
        ).fetchone()

    d = dict(row)
    d["options"] = json.loads(d["options"])
    return Question(**d)


def generate_question(topic: Topic) -> Question:
    """Generate one MCQ for *topic*, persist it, and return the Question."""
    prompt = _PROMPT.format(
        topic_name=topic.name,
        blueprint_notes=topic.blueprint_notes,
    )

    last_err: Exception = RuntimeError("no attempts made")
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            raw = llm_generate(prompt)
            data = _extract(raw)
            _validate(data)
            return _save(topic, data)
        except (ValueError, json.JSONDecodeError, KeyError) as exc:
            last_err = exc
            print(f"  [attempt {attempt}/{MAX_RETRIES}] parse failed: {exc}")

    raise RuntimeError(
        f"Could not generate a valid question after {MAX_RETRIES} attempts: {last_err}"
    )


if __name__ == "__main__":
    from db import get_topics, init_db, seed_db

    init_db()
    seed_db()

    topics = get_topics()
    topic = topics[0]
    print(f"Generating question for: {topic.name}\n")

    q = generate_question(topic)

    print(f"Stem: {q.stem}\n")
    for i, opt in enumerate(q.options):
        marker = "  <-- correct" if opt == q.answer else ""
        print(f"  {chr(65 + i)}) {opt}{marker}")
    print(f"\nExplanation: {q.explanation}")
    print(f"\nSaved -> Question ID {q.id} (source: {q.source})")
