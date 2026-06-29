# CSA Engine — Frontend

Next.js 15 web UI for the [CSA Study Engine](../README.md).

---

## Stack

| Layer | Choice | Reason |
|-------|--------|--------|
| Framework | Next.js 15 (App Router) | SPA with SSR capability, zero config |
| Language | TypeScript | Type-safe API calls and component props |
| Styling | Tailwind CSS + inline styles | Pixel-accurate match to the design spec |
| Fonts | Space Grotesk + JetBrains Mono | Loaded via `next/font/google` — no layout shift |
| Data | `fetch` + `use client` | Simple client-side calls, no extra dependencies |

---

## Views

| View | Route trigger | What it shows |
|------|--------------|---------------|
| **Dashboard** | default | Exam readiness, domain mastery bars, top-3 priority topics, engine snapshot |
| **Study** | Start session / Study tab | Scheduler-driven question session — MCQ and free-text, Ollama grading, vote buttons, live engine rail |
| **Result** | Session complete | Score, per-topic mastery delta, what the engine learned from this session |
| **Engine** | Engine tab | Flywheel diagram, question lifecycle counts, item quality table, fine-tuning horizon |

---

## Getting started

The frontend talks to the FastAPI backend. Start the API first:

```bash
# From the project root
uvicorn api:app --reload
```

Then in this directory:

```bash
npm install
npm run dev
# → http://localhost:3000
```

---

## Environment

| Variable | Default | Purpose |
|----------|---------|---------|
| `NEXT_PUBLIC_API_URL` | `http://localhost:8000` | FastAPI base URL |

Create a `.env.local` file to override:

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Project structure

```
frontend/
├── app/
│   ├── layout.tsx       Font setup, global metadata
│   ├── globals.css      Base styles + scrollbar theme
│   └── page.tsx         SPA shell — owns view state
├── components/
│   ├── TopBar.tsx       Sticky nav + exam readiness bar
│   ├── Dashboard.tsx    Landing view
│   ├── Quiz.tsx         Full quiz session flow
│   ├── Result.tsx       Post-session summary
│   └── Engine.tsx       Engine internals view
└── lib/
    └── api.ts           Typed fetch helpers for all API endpoints
```
