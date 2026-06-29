# Project Structure

```
csa-study-engine/
│
├── config.py            # env vars + paths (imported by every module)
├── models.py            # shared dataclasses: Topic, Question, Attempt
│
├── db.py                # SQLite connection + schema init + seed loader
├── ollama_client.py     # single function: POST prompt → return text
│
├── generator.py         # topic → LLM prompt → Question (parse + retry)
├── grader.py            # question + user_answer → LLM → score 0–1 + rationale
├── scheduler.py         # next_topic_priority(): weight × miss-rate + unseen bonus
│
├── quiz.py              # session orchestrator: ties scheduler/generator/grader/db
├── cli.py               # terminal entry point (Typer or argparse)
├── api.py               # FastAPI routes — wraps quiz.py, exposes /docs
│
├── seed_data.py         # initial CSA question bank (hand-written, source="seed")
│
├── tests/
│   └── test_scheduler.py  # unit tests for next_topic_priority()
│
├── Dockerfile
├── .env.example
├── requirements.txt
├── structure.md         # this file
├── README.md
└── architecture.png     # system-map screenshot
```

## Data flow (request cycle)

```
CLI / API
   └─▶ quiz.py (orchestrator)
          ├─▶ scheduler.py   ─▶ db.py ─▶ SQLite   (pick weakest topic)
          ├─▶ generator.py   ─▶ ollama_client.py ─▶ Ollama  (generate Q)
          │      └─▶ db.py   (store question)
          ├─▶ [serve question, collect answer]
          ├─▶ grader.py      ─▶ ollama_client.py ─▶ Ollama  (score free-text)
          └─▶ db.py          (record attempt → feeds scheduler next round)
```

## Module responsibilities (one job each)

| File | Single responsibility |
|------|-----------------------|
| `config.py` | Read `.env`, expose typed constants |
| `models.py` | Dataclass definitions only, no logic |
| `db.py` | Open connection, run migrations, expose helpers |
| `ollama_client.py` | POST to Ollama API, return raw text |
| `generator.py` | Build generation prompt, call client, parse JSON, retry |
| `grader.py` | Build grading prompt, call client, parse score |
| `scheduler.py` | Compute per-topic priority from attempt history |
| `quiz.py` | Coordinate a full question→answer→grade→record cycle |
| `cli.py` | Parse CLI args, call quiz.py, print results |
| `api.py` | Define FastAPI routes, call quiz.py, return JSON |
