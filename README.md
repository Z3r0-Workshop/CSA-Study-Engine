# CSA Study Engine

> Local-first CLI / API study engine for the ServiceNow CSA certification.

![Architecture](architecture.png)

---

## Problem

Studying for CSA with static flashcards is passive. This engine quizzes you, generates new questions aligned to the official blueprint, and weights what it serves next toward the topics you're weakest on.

---

## Architecture

See [`structure.md`](structure.md) for the full file map.

Three SQLite tables (`topics`, `questions`, `attempts`) power a lightweight scheduler that applies:

```
priority = topic.weight × (1 − rolling_accuracy) + unseen_bonus
```

Everything that touches the model goes through `ollama_client.py` — the single seam for swapping models later.

---

## Stack & Why

| Layer | Choice | Reason |
|-------|--------|--------|
| LLM | Ollama (Mistral 7B) | Local, offline, $0 |
| API | FastAPI | Auto `/docs`, real HTTP surface |
| DB | SQLite | Single-user tool — Postgres would be resume-padding |
| Container | Docker | One-command run, ships the DB file |

---

## How to Run

```bash
# 1. Clone & set up
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env

# 2. Make sure Ollama is running with Mistral
ollama pull mistral

# 3. CLI quiz session
python cli.py

# 4. API server (browse /docs)
uvicorn api:app --reload
```

---

## Screenshots

_Coming after each phase._

---

## What's Next

Fine-tune the generator on your logged wrong answers for a tighter question style.
