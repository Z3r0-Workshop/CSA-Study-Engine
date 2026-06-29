'use client';

interface SessionResult {
  question: {
    id: number;
    topic_name: string;
    kind: string;
  };
  answer: {
    correct: boolean;
    score: number;
  };
}

interface Props {
  results: SessionResult[];
  onNewSession: () => void;
  onEngine: () => void;
}

export default function Result({ results, onNewSession, onEngine }: Props) {
  const total = results.length;
  const correctN = results.filter((r) => r.answer.correct).length;
  const pct = total ? Math.round((correctN / total) * 100) : 0;

  const verdict =
    pct >= 80 ? 'Strong — keep this cadence' : pct >= 55 ? 'Solid progress' : 'The gap is the plan — run it again';
  const vColor = pct >= 80 ? '#5fe3aa' : pct >= 55 ? '#f5b945' : '#f0888c';

  // Per-topic breakdown
  const topicMap = new Map<string, { before: number; correct: number; total: number }>();
  results.forEach((r) => {
    const key = r.question.topic_name;
    if (!topicMap.has(key)) topicMap.set(key, { before: 50, correct: 0, total: 0 });
    const entry = topicMap.get(key)!;
    entry.total++;
    if (r.answer.correct) entry.correct++;
  });

  const topicRows = Array.from(topicMap.entries()).map(([name, { correct, total }]) => {
    const after = Math.round((correct / total) * 100);
    const before = 50;
    const d = after - before;
    return {
      name,
      before,
      after,
      delta: (d > 0 ? '▲ +' : d < 0 ? '▼ ' : '· ') + (d === 0 ? '0' : Math.abs(d)),
      deltaColor: d > 0 ? '#5fe3aa' : d < 0 ? '#f0888c' : '#7e8d89',
    };
  });

  const missedTopics = results.filter((r) => !r.answer.correct).map((r) => r.question.topic_name);
  const uniqueMissed = [...new Set(missedTopics)];

  const eventRows =
    uniqueMissed.length > 0
      ? uniqueMissed.map((t) => ({ icon: '◵', color: '#7ad0fb', text: `${t}: missed — weighted up for next session.` }))
      : [{ icon: '★', color: '#f5b945', text: 'Perfect run — all answers matched the bank cleanly.' }];

  return (
    <div style={{ animation: 'fadeIn .2s ease' }}>
      {/* Score hero */}
      <div
        style={{
          border: '1px solid rgba(120,140,135,.16)',
          borderRadius: 16,
          background: 'linear-gradient(180deg,#11181a,#0d1314)',
          padding: '30px 32px',
          textAlign: 'center',
        }}
      >
        <div
          style={{
            fontFamily: "'JetBrains Mono', monospace",
            fontSize: 11,
            letterSpacing: 2,
            color: '#34d399',
            textTransform: 'uppercase',
          }}
        >
          Session complete
        </div>
        <div
          style={{
            fontFamily: "'JetBrains Mono', monospace",
            fontSize: 58,
            fontWeight: 700,
            color: '#f2f8f5',
            lineHeight: 1.05,
            marginTop: 8,
          }}
        >
          {correctN}
          <span style={{ color: '#54625f', fontSize: 30 }}> / {total}</span>
        </div>
        <div style={{ fontSize: 16, color: vColor, fontWeight: 600, marginTop: 4 }}>
          {verdict}
        </div>
        <div style={{ display: 'flex', gap: 12, justifyContent: 'center', marginTop: 22 }}>
          <button
            onClick={onNewSession}
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 13,
              fontWeight: 600,
              padding: '11px 20px',
              borderRadius: 10,
              cursor: 'pointer',
              border: '1px solid rgba(52,211,153,.5)',
              background: 'rgba(52,211,153,.12)',
              color: '#9af7cf',
              transition: 'all .15s',
            }}
          >
            ↻ New session
          </button>
          <button
            onClick={onEngine}
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 13,
              fontWeight: 600,
              padding: '11px 20px',
              borderRadius: 10,
              cursor: 'pointer',
              border: '1px solid rgba(167,139,250,.4)',
              background: 'rgba(167,139,250,.1)',
              color: '#c0aefb',
              transition: 'all .15s',
            }}
          >
            View engine →
          </button>
        </div>
      </div>

      {/* Details grid */}
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: 18,
          marginTop: 18,
          alignItems: 'start',
        }}
      >
        {/* Mastery moved */}
        <div
          style={{
            border: '1px solid rgba(120,140,135,.16)',
            borderRadius: 16,
            background: '#0d1314',
            overflow: 'hidden',
          }}
        >
          <div
            style={{ padding: '16px 22px', borderBottom: '1px solid rgba(120,140,135,.12)' }}
          >
            <div style={{ fontSize: 15, fontWeight: 600, color: '#eef5f2' }}>Your mastery moved</div>
            <div
              style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 11,
                color: '#7e8d89',
                marginTop: 2,
              }}
            >
              scheduler will reweight from here
            </div>
          </div>
          <div style={{ padding: '10px 22px 18px' }}>
            {topicRows.map((r) => (
              <div
                key={r.name}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 14,
                  padding: '11px 0',
                  borderBottom: '1px solid rgba(120,140,135,.07)',
                }}
              >
                <div style={{ flex: 1, fontSize: 13.5, color: '#dfe7e4' }}>{r.name}</div>
                <div
                  style={{
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 12,
                    color: '#7e8d89',
                  }}
                >
                  {r.before}%
                </div>
                <span
                  style={{
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 12,
                    color: '#54625f',
                  }}
                >
                  →
                </span>
                <div
                  style={{
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 13,
                    color: '#eef5f2',
                    fontWeight: 600,
                    width: 34,
                    textAlign: 'right',
                  }}
                >
                  {r.after}%
                </div>
                <div
                  style={{
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 12,
                    fontWeight: 600,
                    color: r.deltaColor,
                    width: 46,
                    textAlign: 'right',
                  }}
                >
                  {r.delta}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* What the engine learned */}
        <div
          style={{
            border: '1px solid rgba(167,139,250,.22)',
            borderRadius: 16,
            background: 'linear-gradient(180deg,#130f1c,#0c0a14)',
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              padding: '16px 22px',
              borderBottom: '1px solid rgba(167,139,250,.16)',
            }}
          >
            <div style={{ fontSize: 15, fontWeight: 600, color: '#eef5f2' }}>
              What the engine learned
            </div>
            <div
              style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 11,
                color: '#9aa8a4',
                marginTop: 2,
              }}
            >
              from your answers + votes this session
            </div>
          </div>
          <div
            style={{ padding: '14px 22px 18px', display: 'flex', flexDirection: 'column', gap: 12 }}
          >
            {eventRows.map((e, i) => (
              <div key={i} style={{ display: 'flex', gap: 11 }}>
                <span
                  style={{
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 14,
                    color: e.color,
                    flex: 'none',
                  }}
                >
                  {e.icon}
                </span>
                <span style={{ fontSize: 13, color: '#cdd6d3', lineHeight: 1.5 }}>{e.text}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
