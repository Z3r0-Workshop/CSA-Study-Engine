'use client';

import type { Stats } from '@/lib/api';

interface Props {
  stats: Stats;
  onStart: () => void;
  onEngine: () => void;
}

function bar(pct: number, color: string) {
  return (
    <div
      style={{
        height: '100%',
        width: `${pct}%`,
        borderRadius: 6,
        background: `linear-gradient(90deg,${color}cc,${color})`,
        transition: 'width .5s ease',
      }}
    />
  );
}

function accColor(pct: number) {
  return pct >= 70 ? '#5fe3aa' : pct >= 50 ? '#f5b945' : '#f0888c';
}

const DOT_COLORS: Record<string, string> = {
  green: '#34d399',
  cyan: '#38bdf8',
  violet: '#a78bfa',
  amber: '#f5b945',
};

function topicDot(weight: number) {
  if (weight >= 0.14) return '#34d399';
  if (weight >= 0.10) return '#38bdf8';
  if (weight >= 0.08) return '#a78bfa';
  return '#f5b945';
}

export default function Dashboard({ stats, onStart, onEngine }: Props) {
  const readPct = Math.round(stats.exam_readiness * 100);
  const rColor =
    readPct >= 75 ? '#5fe3aa' : readPct >= 60 ? '#9af7cf' : readPct >= 45 ? '#f5b945' : '#f0888c';

  const priority = (t: (typeof stats.topics)[0]) =>
    t.weight * (1 - t.accuracy);

  const weakTopics = [...stats.topics].sort((a, b) => priority(b) - priority(a)).slice(0, 3);
  const rankColors = ['#5fe3aa', '#7ad0fb', '#c0aefb'];

  const { lifecycle } = stats;
  const logged = stats.total_attempts;
  const target = 1000;
  const loggedPct = Math.round(Math.min(logged / target, 1) * 100);

  return (
    <div style={{ animation: 'fadeIn .2s ease' }}>
      {/* Row 1 */}
      <div style={{ display: 'grid', gridTemplateColumns: '1.45fr 1fr', gap: 18, alignItems: 'stretch' }}>
        {/* Welcome card */}
        <div
          style={{
            border: '1px solid rgba(120,140,135,.16)',
            borderRadius: 16,
            background: 'linear-gradient(180deg,#11181a,#0d1314)',
            padding: '26px 28px',
            display: 'flex',
            flexDirection: 'column',
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
            Welcome back
          </div>
          <h1
            style={{
              margin: '8px 0 0',
              fontSize: 32,
              fontWeight: 700,
              letterSpacing: -0.6,
              color: '#f2f8f5',
              lineHeight: 1.1,
            }}
          >
            Let&apos;s close the gap to CSA.
          </h1>
          <p style={{ margin: '10px 0 0', color: '#9aa8a4', fontSize: 15, lineHeight: 1.55, maxWidth: 460 }}>
            The scheduler has lined up a session weighted toward your weakest domains. Free-text
            answers are graded locally by Ollama.
          </p>
          <div
            style={{ marginTop: 'auto', display: 'flex', gap: 12, alignItems: 'center', paddingTop: 24 }}
          >
            <button
              onClick={onStart}
              style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 14,
                fontWeight: 600,
                padding: '13px 22px',
                borderRadius: 11,
                cursor: 'pointer',
                border: '1px solid rgba(52,211,153,.5)',
                background: 'linear-gradient(180deg,rgba(52,211,153,.2),rgba(52,211,153,.08))',
                color: '#9af7cf',
                transition: 'all .15s ease',
              }}
              onMouseEnter={(e) => {
                (e.target as HTMLElement).style.background = 'rgba(52,211,153,.26)';
                (e.target as HTMLElement).style.borderColor = '#34d399';
              }}
              onMouseLeave={(e) => {
                (e.target as HTMLElement).style.background =
                  'linear-gradient(180deg,rgba(52,211,153,.2),rgba(52,211,153,.08))';
                (e.target as HTMLElement).style.borderColor = 'rgba(52,211,153,.5)';
              }}
            >
              &#9654; Start adaptive session
            </button>
            <span
              style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 12, color: '#7e8d89' }}
            >
              {stats.total_questions} questions queued
            </span>
          </div>
        </div>

        {/* Engine snapshot */}
        <div
          style={{
            border: '1px solid rgba(120,140,135,.16)',
            borderRadius: 16,
            background: '#0d1314',
            padding: '22px 24px',
            display: 'flex',
            flexDirection: 'column',
            gap: 14,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div style={{ fontSize: 15, fontWeight: 600, color: '#eef5f2' }}>Engine snapshot</div>
            <span
              style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 10,
                color: '#a78bfa',
                border: '1px solid rgba(167,139,250,.3)',
                borderRadius: 5,
                padding: '2px 7px',
              }}
            >
              self-improving
            </span>
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
            <div
              style={{
                border: '1px solid rgba(245,185,69,.25)',
                borderRadius: 10,
                background: 'rgba(245,185,69,.05)',
                padding: '12px 13px',
              }}
            >
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 24,
                  fontWeight: 700,
                  color: '#f5b945',
                  lineHeight: 1,
                }}
              >
                {lifecycle.golden}
              </div>
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 10.5,
                  color: '#9aa8a4',
                  marginTop: 2,
                }}
              >
                golden questions
              </div>
            </div>
            <div
              style={{
                border: '1px solid rgba(52,211,153,.22)',
                borderRadius: 10,
                background: 'rgba(52,211,153,.05)',
                padding: '12px 13px',
              }}
            >
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 24,
                  fontWeight: 700,
                  color: '#5fe3aa',
                  lineHeight: 1,
                }}
              >
                {lifecycle.active}
              </div>
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 10.5,
                  color: '#9aa8a4',
                  marginTop: 2,
                }}
              >
                active in bank
              </div>
            </div>
          </div>
          <div style={{ borderTop: '1px dashed rgba(120,140,135,.2)', paddingTop: 13 }}>
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 11,
                color: '#9aa8a4',
                marginBottom: 6,
              }}
            >
              <span>logged answers &rarr; fine-tune</span>
              <span style={{ color: '#c0aefb' }}>
                {logged} / {target}
              </span>
            </div>
            <div
              style={{
                height: 8,
                borderRadius: 6,
                background: '#13191a',
                overflow: 'hidden',
                border: '1px solid rgba(120,140,135,.14)',
              }}
            >
              {bar(loggedPct, '#a78bfa')}
            </div>
          </div>
        </div>
      </div>

      {/* Row 2 */}
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: '1.45fr 1fr',
          gap: 18,
          marginTop: 18,
          alignItems: 'start',
        }}
      >
        {/* Domain mastery */}
        <div
          style={{
            border: '1px solid rgba(120,140,135,.16)',
            borderRadius: 16,
            background: '#0d1314',
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              padding: '16px 22px',
              borderBottom: '1px solid rgba(120,140,135,.12)',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            <div style={{ fontSize: 15, fontWeight: 600, color: '#eef5f2' }}>Domain mastery</div>
            <div
              style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 11,
                color: '#7e8d89',
              }}
            >
              rolling accuracy · exam weight
            </div>
          </div>
          <div style={{ padding: '8px 22px 18px' }}>
            {stats.topics.map((t) => {
              const accPct = Math.round(t.accuracy * 100);
              const aColor = accColor(accPct);
              const dot = topicDot(t.weight);
              return (
                <div
                  key={t.id}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 14,
                    padding: '9px 0',
                    borderBottom: '1px solid rgba(120,140,135,.07)',
                  }}
                >
                  <div
                    style={{
                      width: 9,
                      height: 9,
                      borderRadius: '50%',
                      background: dot,
                      flex: 'none',
                    }}
                  />
                  <div style={{ flex: 1, minWidth: 0 }}>
                    <div
                      style={{
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'baseline',
                        gap: 8,
                      }}
                    >
                      <span
                        style={{
                          fontSize: 13.5,
                          color: '#dfe7e4',
                          whiteSpace: 'nowrap',
                          overflow: 'hidden',
                          textOverflow: 'ellipsis',
                        }}
                      >
                        {t.name}
                      </span>
                      <span
                        style={{
                          fontFamily: "'JetBrains Mono', monospace",
                          fontSize: 11,
                          color: aColor,
                          flex: 'none',
                        }}
                      >
                        {accPct}%
                      </span>
                    </div>
                    <div
                      style={{
                        height: 6,
                        borderRadius: 5,
                        background: '#13191a',
                        overflow: 'hidden',
                        marginTop: 5,
                      }}
                    >
                      {bar(accPct, aColor)}
                    </div>
                  </div>
                  <span
                    style={{
                      fontFamily: "'JetBrains Mono', monospace",
                      fontSize: 10,
                      color: '#7e8d89',
                      flex: 'none',
                      width: 34,
                      textAlign: 'right',
                    }}
                  >
                    {Math.round(t.weight * 100)}%
                  </span>
                </div>
              );
            })}
          </div>
        </div>

        {/* Up next */}
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
            <div style={{ fontSize: 15, fontWeight: 600, color: '#eef5f2' }}>Up next</div>
            <div
              style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 11,
                color: '#7e8d89',
                marginTop: 2,
              }}
            >
              weight &times; (1 &minus; accuracy) + unseen
            </div>
          </div>
          <div style={{ padding: '14px 18px 18px', display: 'flex', flexDirection: 'column', gap: 10 }}>
            {weakTopics.map((t, i) => {
              const rc = rankColors[i];
              const isBest = i === 0;
              return (
                <div
                  key={t.id}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 12,
                    border: `1px solid ${isBest ? 'rgba(52,211,153,.3)' : 'rgba(120,140,135,.16)'}`,
                    borderRadius: 11,
                    background: isBest ? 'rgba(52,211,153,.05)' : '#0e1415',
                    padding: '12px 14px',
                  }}
                >
                  <div
                    style={{
                      fontFamily: "'JetBrains Mono', monospace",
                      fontSize: 18,
                      fontWeight: 700,
                      color: rc,
                    }}
                  >
                    0{i + 1}
                  </div>
                  <div style={{ flex: 1, minWidth: 0 }}>
                    <div style={{ fontSize: 13.5, color: '#eef5f2', fontWeight: 500 }}>{t.name}</div>
                    <div
                      style={{
                        fontFamily: "'JetBrains Mono', monospace",
                        fontSize: 10.5,
                        color: '#9aa8a4',
                        marginTop: 1,
                      }}
                    >
                      {Math.round(t.accuracy * 100)}% accuracy · weight {Math.round(t.weight * 100)}%
                    </div>
                  </div>
                  <div
                    style={{
                      fontFamily: "'JetBrains Mono', monospace",
                      fontSize: 13,
                      color: rc,
                      fontWeight: 600,
                    }}
                  >
                    {priority(t).toFixed(3)}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
