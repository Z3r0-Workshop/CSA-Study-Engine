'use client';

import { useState, useEffect, useCallback } from 'react';
import TopBar from '@/components/TopBar';
import Dashboard from '@/components/Dashboard';
import Quiz from '@/components/Quiz';
import Result from '@/components/Result';
import Engine from '@/components/Engine';
import { api } from '@/lib/api';
import type { Stats } from '@/lib/api';

type View = 'dashboard' | 'quiz' | 'result' | 'engine';

interface SessionResult {
  question: { id: number; topic_name: string; kind: string };
  answer: { correct: boolean; score: number };
  userAnswer: string;
}

const EMPTY_STATS: Stats = {
  topics: [],
  total_questions: 0,
  total_attempts: 0,
  exam_readiness: 0.5,
  lifecycle: { candidate: 0, active: 0, golden: 0, retired: 0 },
  quality: [],
};

export default function Home() {
  const [view, setView] = useState<View>('dashboard');
  const [stats, setStats] = useState<Stats>(EMPTY_STATS);
  const [sessionResults, setSessionResults] = useState<SessionResult[]>([]);
  const [statsError, setStatsError] = useState(false);

  const loadStats = useCallback(async () => {
    try {
      const s = await api.stats();
      setStats(s);
      setStatsError(false);
    } catch {
      setStatsError(true);
    }
  }, []);

  useEffect(() => {
    loadStats();
  }, [loadStats]);

  // Refresh stats whenever we leave quiz or result
  useEffect(() => {
    if (view === 'dashboard' || view === 'engine') {
      loadStats();
    }
  }, [view, loadStats]);

  function handleNavClick(target: View) {
    if (target === 'quiz') {
      setView('quiz');
    } else {
      setView(target);
    }
  }

  function handleSessionComplete(results: SessionResult[]) {
    setSessionResults(results);
    setView('result');
  }

  return (
    <div
      style={{
        minHeight: '100vh',
        background:
          'radial-gradient(1100px 640px at 78% -12%, rgba(52,211,153,.05), transparent 60%), radial-gradient(900px 600px at -5% 110%, rgba(167,139,250,.05), transparent 55%), #0a0d0e',
        color: '#d7e0dd',
      }}
    >
      <TopBar
        view={view === 'result' ? 'quiz' : (view as 'dashboard' | 'quiz' | 'engine')}
        examReadiness={stats.exam_readiness}
        onNav={(target) => handleNavClick(target as View)}
      />

      {statsError && (
        <div
          style={{
            background: 'rgba(229,72,77,.08)',
            borderBottom: '1px solid rgba(229,72,77,.2)',
            padding: '10px 26px',
            fontFamily: "'JetBrains Mono', monospace",
            fontSize: 12,
            color: '#f0888c',
          }}
        >
          ⚠ API unreachable — start the FastAPI server with{' '}
          <code style={{ background: '#1a1f20', padding: '1px 5px', borderRadius: 4 }}>
            uvicorn api:app --reload
          </code>
        </div>
      )}

      <div style={{ maxWidth: 1120, margin: '0 auto', padding: '30px 26px 70px' }}>
        {view === 'dashboard' && (
          <Dashboard
            stats={stats}
            onStart={() => setView('quiz')}
            onEngine={() => setView('engine')}
          />
        )}

        {view === 'quiz' && (
          <Quiz onSessionComplete={handleSessionComplete} />
        )}

        {view === 'result' && (
          <Result
            results={sessionResults}
            onNewSession={() => setView('quiz')}
            onEngine={() => setView('engine')}
          />
        )}

        {view === 'engine' && <Engine stats={stats} />}
      </div>
    </div>
  );
}
