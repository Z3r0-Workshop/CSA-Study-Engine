'use client';

import { useState, useEffect, useCallback } from 'react';
import { api } from '@/lib/api';
import type { Question, AnswerResult } from '@/lib/api';

interface SessionResult {
  question: Question;
  answer: AnswerResult;
  userAnswer: string;
}

interface LiveEvent {
  type: 'miss' | 'flag' | 'up' | 'down';
  text: string;
}

interface Props {
  onSessionComplete: (results: SessionResult[]) => void;
}

const SESSION_SIZE = 9;

function bar(pct: number, color: string) {
  return (
    <div
      style={{
        height: '100%',
        width: `${Math.max(pct, 4)}%`,
        borderRadius: 6,
        background: `linear-gradient(90deg,${color}cc,${color})`,
        transition: 'width .5s ease',
      }}
    />
  );
}

export default function Quiz({ onSessionComplete }: Props) {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [queue, setQueue] = useState<Question[]>([]);
  const [idx, setIdx] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  const [freeText, setFreeText] = useState('');
  const [revealed, setRevealed] = useState(false);
  const [grading, setGrading] = useState(false);
  const [currentResult, setCurrentResult] = useState<AnswerResult | null>(null);
  const [results, setResults] = useState<SessionResult[]>([]);
  const [vote, setVote] = useState<'up' | 'down' | 'flag' | null>(null);
  const [liveEvents, setLiveEvents] = useState<LiveEvent[]>([]);

  const pushEvent = useCallback((type: LiveEvent['type'], text: string) => {
    setLiveEvents((prev) => {
      if (prev.some((e) => e.text === text)) return prev;
      return [{ type, text }, ...prev].slice(0, 8);
    });
  }, []);

  const fetchQuestion = useCallback(async (): Promise<Question | null> => {
    try {
      return await api.question();
    } catch {
      return null;
    }
  }, []);

  useEffect(() => {
    (async () => {
      setLoading(true);
      const qs: Question[] = [];
      for (let i = 0; i < SESSION_SIZE; i++) {
        const q = await fetchQuestion();
        if (q && !qs.find((x) => x.id === q.id)) qs.push(q);
      }
      if (qs.length === 0) {
        setError('Could not fetch questions. Is the API running?');
      } else {
        setQueue(qs);
      }
      setLoading(false);
    })();
  }, [fetchQuestion]);

  const q = queue[idx];
  const isMcq = q?.kind === 'mcq';
  const isFree = q?.kind === 'free';
  const canSubmit = isMcq ? selected !== null : freeText.trim().length > 0;
  const isLast = idx + 1 >= queue.length;

  async function submit() {
    if (!q || !canSubmit || revealed || grading) return;
    const userAnswer = isMcq ? q.options[selected!] : freeText;
    setGrading(true);
    try {
      const result = await api.answer(q.id, userAnswer);
      setCurrentResult(result);
      setRevealed(true);
      setResults((prev) => [...prev, { question: q, answer: result, userAnswer }]);
      if (!result.correct) {
        pushEvent('miss', `${q.topic_name}: missed — added to weak-topic queue.`);
      }
    } catch (e) {
      setError('Failed to submit answer. API may be unreachable.');
    } finally {
      setGrading(false);
    }
  }

  async function handleVote(kind: 'up' | 'down' | 'flag') {
    if (!q) return;
    setVote(kind);
    await api.vote(q.id, kind).catch(() => {});
    if (kind === 'flag')
      pushEvent('flag', `Q#${q.id} flagged — queued for review + rewrite.`);
    else if (kind === 'down')
      pushEvent('down', `Q#${q.id} down-voted — discrimination re-check queued.`);
    else if (kind === 'up')
      pushEvent('up', `Q#${q.id} up-voted — reinforcing its place toward golden set.`);
  }

  function next() {
    if (isLast) {
      onSessionComplete(results);
      return;
    }
    setIdx((i) => i + 1);
    setSelected(null);
    setFreeText('');
    setRevealed(false);
    setCurrentResult(null);
    setVote(null);
  }

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: 300 }}>
        <div style={{ fontFamily: "'JetBrains Mono', monospace", color: '#34d399', fontSize: 14 }}>
          Loading questions...
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div
        style={{
          border: '1px solid rgba(229,72,77,.3)',
          borderRadius: 14,
          background: 'rgba(229,72,77,.06)',
          padding: '24px 28px',
          color: '#f0888c',
          fontFamily: "'JetBrains Mono', monospace",
          fontSize: 13,
        }}
      >
        {error}
      </div>
    );
  }

  if (!q) return null;

  const progPct = Math.round((idx / queue.length) * 100);
  const correctN = results.filter((r) => r.answer.correct).length;

  const topicTagColor = '#34d399';

  const evStyle: Record<string, { icon: string; color: string }> = {
    miss: { icon: '◵', color: '#7ad0fb' },
    flag: { icon: '⚑', color: '#c0aefb' },
    up: { icon: '★', color: '#f5b945' },
    down: { icon: '⊘', color: '#f0888c' },
  };

  const voteBtn = (kind: 'up' | 'down' | 'flag', label: string, activeColor: string, activeBg: string) => (
    <button
      onClick={() => handleVote(kind)}
      style={{
        fontFamily: "'JetBrains Mono', monospace",
        fontSize: 11.5,
        padding: '6px 11px',
        borderRadius: 8,
        cursor: 'pointer',
        transition: 'all .14s',
        border: `1px solid ${vote === kind ? activeColor : 'rgba(120,140,135,.2)'}`,
        background: vote === kind ? activeBg : '#0b1112',
        color: vote === kind ? activeColor : '#9aa8a4',
      }}
    >
      {label}
    </button>
  );

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 296px', gap: 18, alignItems: 'start' }}>
      {/* Main card */}
      <div
        style={{
          border: '1px solid rgba(120,140,135,.16)',
          borderRadius: 16,
          background: 'linear-gradient(180deg,#11181a,#0d1314)',
          overflow: 'hidden',
          animation: 'fadeIn .2s ease',
        }}
      >
        {/* Progress bar */}
        <div style={{ height: 5, background: '#13191a' }}>{bar(progPct, '#34d399')}</div>

        <div style={{ padding: '24px 28px 28px' }}>
          {/* Header */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 12 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
              <span style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 11, color: '#7e8d89' }}>
                QUESTION {idx + 1} / {queue.length}
              </span>
              <span
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 10.5,
                  padding: '3px 9px',
                  borderRadius: 6,
                  border: `1px solid ${topicTagColor}66`,
                  background: `${topicTagColor}14`,
                  color: topicTagColor,
                }}
              >
                {q.topic_name}
              </span>
              <span
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 10.5,
                  padding: '3px 9px',
                  borderRadius: 6,
                  border: '1px solid rgba(120,140,135,.2)',
                  color: '#9aa8a4',
                }}
              >
                {isMcq ? 'multiple choice' : 'free text · LLM-graded'}
              </span>
            </div>
          </div>

          {/* Stem */}
          <h2
            style={{
              margin: '18px 0 0',
              fontSize: 23,
              fontWeight: 600,
              lineHeight: 1.4,
              color: '#f2f8f5',
              letterSpacing: -0.3,
            }}
          >
            {q.stem}
          </h2>

          {/* MCQ options */}
          {isMcq && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginTop: 22 }}>
              {q.options.map((text, i) => {
                const sel = selected === i;
                const isAns = revealed && i === q.options.indexOf(currentResult ? currentResult.model_answer : '');
                // derive answer index from model_answer string match
                const answerIdx = q.options.findIndex(
                  (o) => o.toLowerCase() === currentResult?.model_answer?.toLowerCase()
                );
                const isCorrectOpt = revealed && i === answerIdx;
                const isWrongSel = revealed && sel && !isCorrectOpt;

                let bd = 'rgba(120,140,135,.2)',
                  bg = '#0b1112',
                  fg = '#cdd6d3',
                  kbg = '#161d1e',
                  kfg = '#7e8d89',
                  mark = '',
                  mc = 'transparent';

                if (!revealed && sel) {
                  bd = 'rgba(52,211,153,.5)';
                  bg = 'rgba(52,211,153,.08)';
                  fg = '#eafff6';
                  kbg = 'rgba(52,211,153,.2)';
                  kfg = '#5fe3aa';
                }
                if (revealed) {
                  if (isCorrectOpt) {
                    bd = 'rgba(52,211,153,.55)';
                    bg = 'rgba(52,211,153,.1)';
                    fg = '#d6fff0';
                    kbg = 'rgba(52,211,153,.25)';
                    kfg = '#5fe3aa';
                    mark = '✓';
                    mc = '#5fe3aa';
                  } else if (isWrongSel) {
                    bd = 'rgba(229,72,77,.5)';
                    bg = 'rgba(229,72,77,.08)';
                    fg = '#f5c0c2';
                    kbg = 'rgba(229,72,77,.2)';
                    kfg = '#f0888c';
                    mark = '✕';
                    mc = '#f0888c';
                  } else {
                    fg = '#7e8d89';
                  }
                }

                return (
                  <button
                    key={i}
                    onClick={() => !revealed && setSelected(i)}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 13,
                      width: '100%',
                      textAlign: 'left',
                      padding: '14px 16px',
                      borderRadius: 11,
                      cursor: revealed ? 'default' : 'pointer',
                      fontFamily: "'Space Grotesk', sans-serif",
                      fontSize: 14.5,
                      transition: 'all .14s ease',
                      border: `1px solid ${bd}`,
                      background: bg,
                      color: fg,
                    }}
                  >
                    <span
                      style={{
                        fontFamily: "'JetBrains Mono', monospace",
                        fontSize: 12,
                        fontWeight: 600,
                        width: 24,
                        height: 24,
                        borderRadius: 6,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        flex: 'none',
                        background: kbg,
                        color: kfg,
                      }}
                    >
                      {String.fromCharCode(65 + i)}
                    </span>
                    <span style={{ flex: 1, textAlign: 'left' }}>{text}</span>
                    <span
                      style={{
                        fontFamily: "'JetBrains Mono', monospace",
                        fontSize: 15,
                        color: mc,
                      }}
                    >
                      {mark}
                    </span>
                  </button>
                );
              })}
            </div>
          )}

          {/* Free text */}
          {isFree && (
            <div style={{ marginTop: 22 }}>
              <textarea
                value={freeText}
                onChange={(e) => !revealed && setFreeText(e.target.value)}
                disabled={revealed}
                placeholder="Type your answer — Ollama grades it 0–1 against the model answer…"
                style={{
                  width: '100%',
                  minHeight: 120,
                  resize: 'vertical',
                  padding: '14px 16px',
                  borderRadius: 11,
                  fontSize: 14.5,
                  lineHeight: 1.55,
                  color: '#eafff6',
                  background: '#0b1112',
                  border: `1px solid ${revealed ? 'rgba(120,140,135,.16)' : 'rgba(52,211,153,.3)'}`,
                  opacity: revealed ? 0.7 : 1,
                  fontFamily: "'Space Grotesk', sans-serif",
                }}
              />
            </div>
          )}

          {/* Primary button */}
          <div style={{ marginTop: 20 }}>
            {!revealed ? (
              <button
                onClick={submit}
                disabled={!canSubmit || grading}
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 13.5,
                  fontWeight: 600,
                  padding: '12px 22px',
                  borderRadius: 10,
                  border: `1px solid ${canSubmit ? 'rgba(52,211,153,.5)' : 'rgba(120,140,135,.18)'}`,
                  background: canSubmit ? 'rgba(52,211,153,.14)' : '#0e1415',
                  color: canSubmit ? '#9af7cf' : '#54625f',
                  cursor: canSubmit ? 'pointer' : 'not-allowed',
                  transition: 'all .15s',
                }}
              >
                {grading
                  ? 'Grading…'
                  : isFree
                  ? 'Grade with Ollama →'
                  : 'Submit answer'}
              </button>
            ) : (
              <button
                onClick={next}
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 13.5,
                  fontWeight: 600,
                  padding: '12px 22px',
                  borderRadius: 10,
                  border: '1px solid rgba(120,140,135,.3)',
                  background: '#161d1e',
                  color: '#dfe7e4',
                  cursor: 'pointer',
                  transition: 'all .15s',
                }}
              >
                {isLast ? 'Finish session →' : 'Next question →'}
              </button>
            )}
          </div>

          {/* Feedback */}
          {revealed && currentResult && (
            <div
              style={{
                marginTop: 22,
                borderTop: '1px solid rgba(120,140,135,.13)',
                paddingTop: 20,
                animation: 'fadeIn .2s ease',
              }}
            >
              {/* Verdict */}
              <div style={{ display: 'flex', alignItems: 'center', gap: 11 }}>
                {isMcq ? (
                  <div
                    style={{
                      width: 34,
                      height: 34,
                      borderRadius: 9,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: 17,
                      fontWeight: 700,
                      color: currentResult.correct ? '#06140e' : '#fff',
                      background: currentResult.correct ? '#34d399' : '#e5484d',
                    }}
                  >
                    {currentResult.correct ? '✓' : '✕'}
                  </div>
                ) : (
                  <div
                    style={{
                      minWidth: 42,
                      height: 34,
                      padding: '0 9px',
                      borderRadius: 9,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontFamily: "'JetBrains Mono', monospace",
                      fontSize: 15,
                      fontWeight: 700,
                      color: '#06140e',
                      background:
                        currentResult.score >= 0.6
                          ? '#5fe3aa'
                          : currentResult.score >= 0.35
                          ? '#f5b945'
                          : '#f0888c',
                    }}
                  >
                    {currentResult.score.toFixed(1)}
                  </div>
                )}
                <div>
                  <div
                    style={{
                      fontSize: 15,
                      fontWeight: 600,
                      color:
                        currentResult.correct
                          ? '#5fe3aa'
                          : isFree && currentResult.score >= 0.35
                          ? '#f5b945'
                          : '#f0888c',
                    }}
                  >
                    {isMcq
                      ? currentResult.correct
                        ? 'Correct'
                        : 'Not quite'
                      : `Graded ${currentResult.score.toFixed(2)} / 1.00`}
                  </div>
                  <div
                    style={{
                      fontFamily: "'JetBrains Mono', monospace",
                      fontSize: 11,
                      color: '#7e8d89',
                    }}
                  >
                    {isMcq
                      ? currentResult.correct
                        ? `Logged · ${q.topic_name} accuracy nudged up`
                        : 'Logged · this topic gets weighted up next time'
                      : currentResult.rationale}
                  </div>
                </div>
              </div>

              {/* Model answer (free text only) */}
              {isFree && (
                <div
                  style={{
                    marginTop: 14,
                    border: '1px solid rgba(56,189,248,.2)',
                    borderRadius: 10,
                    background: 'rgba(56,189,248,.04)',
                    padding: '12px 15px',
                  }}
                >
                  <div
                    style={{
                      fontFamily: "'JetBrains Mono', monospace",
                      fontSize: 10,
                      letterSpacing: 1,
                      color: '#7ad0fb',
                      marginBottom: 5,
                    }}
                  >
                    MODEL ANSWER
                  </div>
                  <div style={{ fontSize: 13.5, color: '#cdd6d3', lineHeight: 1.5 }}>
                    {currentResult.model_answer}
                  </div>
                </div>
              )}

              {/* Explanation */}
              <div
                style={{
                  marginTop: 14,
                  border: '1px solid rgba(120,140,135,.16)',
                  borderRadius: 10,
                  background: '#0b1112',
                  padding: '12px 15px',
                }}
              >
                <div
                  style={{
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 10,
                    letterSpacing: 1,
                    color: '#9aa8a4',
                    marginBottom: 5,
                  }}
                >
                  EXPLANATION
                </div>
                <div style={{ fontSize: 13.5, color: '#cdd6d3', lineHeight: 1.55 }}>
                  {currentResult.explanation}
                </div>
              </div>

              {/* Vote buttons */}
              <div
                style={{
                  marginTop: 16,
                  display: 'flex',
                  alignItems: 'center',
                  gap: 12,
                  flexWrap: 'wrap',
                }}
              >
                <span
                  style={{
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 11,
                    color: '#7e8d89',
                  }}
                >
                  Train the engine &rarr;
                </span>
                {voteBtn('up', '👍 Good question', '#f5b945', 'rgba(245,185,69,.12)')}
                {voteBtn('down', '👎 Weak', '#f0888c', 'rgba(229,72,77,.1)')}
                {voteBtn('flag', '🚩 Flag / confusing', '#c0aefb', 'rgba(167,139,250,.12)')}
                {vote && (
                  <span
                    style={{
                      fontFamily: "'JetBrains Mono', monospace",
                      fontSize: 11,
                      color: '#a78bfa',
                    }}
                  >
                    ✓ signal recorded
                  </span>
                )}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Right rail */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 16, position: 'sticky', top: 88 }}>
        {/* Session stats */}
        <div
          style={{
            border: '1px solid rgba(120,140,135,.16)',
            borderRadius: 14,
            background: '#0d1314',
            padding: '16px 18px',
          }}
        >
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 11,
              letterSpacing: 1,
              color: '#7e8d89',
              marginBottom: 12,
            }}
          >
            THIS SESSION
          </div>
          <div style={{ display: 'flex', gap: 18, marginBottom: 14 }}>
            <div>
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 26,
                  fontWeight: 700,
                  color: '#5fe3aa',
                  lineHeight: 1,
                }}
              >
                {correctN}
              </div>
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 10,
                  color: '#7e8d89',
                  marginTop: 2,
                }}
              >
                correct
              </div>
            </div>
            <div>
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 26,
                  fontWeight: 700,
                  color: '#eef5f2',
                  lineHeight: 1,
                }}
              >
                {results.length}
              </div>
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 10,
                  color: '#7e8d89',
                  marginTop: 2,
                }}
              >
                answered
              </div>
            </div>
          </div>
          <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
            {queue.map((qq, i) => {
              let color = '#1c2426';
              if (i < idx) {
                const rr = results[i];
                color = rr ? (rr.answer.correct ? '#34d399' : '#e5484d') : '#3a4648';
              } else if (i === idx) {
                color = '#5fe3aa';
              }
              return (
                <div
                  key={i}
                  style={{
                    width: 14,
                    height: 14,
                    borderRadius: 5,
                    background: color,
                    boxShadow: i === idx ? '0 0 0 2px rgba(52,211,153,.25)' : undefined,
                  }}
                />
              );
            })}
          </div>
        </div>

        {/* Live engine events */}
        <div
          style={{
            border: '1px solid rgba(167,139,250,.22)',
            borderRadius: 14,
            background: 'linear-gradient(180deg,#130f1c,#0c0a14)',
            padding: '16px 18px',
            minHeight: 150,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 12 }}>
            <span
              style={{
                width: 7,
                height: 7,
                borderRadius: '50%',
                background: '#a78bfa',
                boxShadow: '0 0 8px #a78bfa',
                display: 'inline-block',
              }}
            />
            <span
              style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 11,
                letterSpacing: 1,
                color: '#c0aefb',
              }}
            >
              ENGINE · LIVE
            </span>
          </div>
          {liveEvents.length === 0 ? (
            <div
              style={{
                fontSize: 11.5,
                color: '#6a7873',
                lineHeight: 1.5,
                fontFamily: "'JetBrains Mono', monospace",
              }}
            >
              Answer &amp; rate questions — the engine logs item stats and queues refinements here
              in real time.
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 9 }}>
              {liveEvents.map((e, i) => {
                const st = evStyle[e.type] ?? { icon: '•', color: '#9aa8a4' };
                return (
                  <div key={i} style={{ display: 'flex', gap: 8 }}>
                    <span
                      style={{
                        fontFamily: "'JetBrains Mono', monospace",
                        fontSize: 12,
                        color: st.color,
                        flex: 'none',
                      }}
                    >
                      {st.icon}
                    </span>
                    <span style={{ fontSize: 11.5, color: '#bcc8c4', lineHeight: 1.4 }}>{e.text}</span>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
