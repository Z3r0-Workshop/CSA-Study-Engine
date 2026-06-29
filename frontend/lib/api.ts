const BASE = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

export interface Topic {
  id: number;
  name: string;
  weight: number;
  blueprint_notes: string;
}

export interface Question {
  id: number;
  topic_id: number;
  topic_name: string;
  stem: string;
  kind: 'mcq' | 'free';
  options: string[];
  source: string;
}

export interface AnswerResult {
  correct: boolean;
  score: number;
  rationale: string;
  model_answer: string;
  explanation: string;
}

export interface TopicStat {
  id: number;
  name: string;
  weight: number;
  accuracy: number;
  attempt_count: number;
  question_count: number;
}

export interface QualityRow {
  id: string;
  topic: string;
  difficulty: number | null;
  up_votes: number;
  down_votes: number;
  flag_votes: number;
  net_votes: number;
  status: 'active' | 'golden' | 'retired' | 'too easy';
}

export interface Stats {
  topics: TopicStat[];
  total_questions: number;
  total_attempts: number;
  exam_readiness: number;
  lifecycle: { candidate: number; active: number; golden: number; retired: number };
  quality: QualityRow[];
}

async function get<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}${path}`, { cache: 'no-store' });
  if (!res.ok) throw new Error(`GET ${path} → ${res.status}`);
  return res.json() as Promise<T>;
}

async function post<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`POST ${path} → ${res.status}`);
  return res.json() as Promise<T>;
}

export const api = {
  health: () => get<{ status: string }>('/health'),
  topics: () => get<Topic[]>('/topics'),
  question: () => get<Question>('/question'),
  answer: (question_id: number, user_answer: string) =>
    post<AnswerResult>('/answer', { question_id, user_answer }),
  vote: (question_id: number, kind: 'up' | 'down' | 'flag') =>
    post<{ recorded: boolean }>('/vote', { question_id, kind }),
  stats: () => get<Stats>('/stats'),
};
