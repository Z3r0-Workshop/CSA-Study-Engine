'use client';

import React from 'react';
import type { Stats, QualityRow } from '@/lib/api';

interface Props {
  stats: Stats;
}

function statusBadge(st: string) {
  const map: Record<string, { c: string; b: string; bg: string }> = {
    golden: { c: '#ffd479', b: 'rgba(245,185,69,.4)', bg: 'rgba(245,185,69,.1)' },
    active: { c: '#5fe3aa', b: 'rgba(52,211,153,.35)', bg: 'rgba(52,211,153,.08)' },
    'too easy': { c: '#7ad0fb', b: 'rgba(56,189,248,.35)', bg: 'rgba(56,189,248,.08)' },
    retired: { c: '#f0888c', b: 'rgba(229,72,77,.35)', bg: 'rgba(229,72,77,.07)' },
  };
  const m = map[st] || map.active;
  return (
    <span
      style={{
        fontFamily: "'JetBrains Mono', monospace",
        fontSize: 9.5,
        fontWeight: 600,
        padding: '2px 7px',
        borderRadius: 5,
        color: m.c,
        border: `1px solid ${m.b}`,
        background: m.bg,
      }}
    >
      {st}
    </span>
  );
}

function pColor(p: number | null) {
  if (p === null) return '#7e8d89';
  return p >= 0.4 && p <= 0.8 ? '#5fe3aa' : p > 0.8 ? '#7ad0fb' : '#f5b945';
}

export default function Engine({ stats }: Props) {
  const { lifecycle, quality } = stats;
  const logged = stats.total_attempts;
  const target = 1000;
  const loggedPct = Math.round(Math.min(logged / target, 1) * 100);

  const SEED_EVENTS = [
    { type: 'promote', icon: '↑', color: '#f5b945', text: 'Vote threshold reached — question promoted to golden set.' },
    { type: 'rewrite', icon: '✎', color: '#c0aefb', text: 'Explanation queued for rewrite based on miss patterns.' },
    { type: 'retire', icon: '⊘', color: '#f0888c', text: 'Question flagged twice — retirement check queued.' },
  ];

  return (
    <div style={{ animation: 'fadeIn .2s ease' }}>
      {/* Flywheels */}
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 13 }}>
        <h1
          style={{
            margin: 0,
            fontSize: 28,
            fontWeight: 700,
            letterSpacing: -0.5,
            color: '#f2f8f5',
          }}
        >
          Two flywheels
        </h1>
        <span
          style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 12, color: '#7e8d89' }}
        >
          every answer turns both
        </span>
      </div>

      <div
        style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, marginTop: 18 }}
      >
        <div
          style={{
            border: '1px solid rgba(52,211,153,.28)',
            borderRadius: 14,
            background: 'linear-gradient(180deg,#0e1a16,#0b1311)',
            padding: '20px 22px',
          }}
        >
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 12,
              color: '#5fe3aa',
              marginBottom: 8,
            }}
          >
            FLYWHEEL ① — YOU GET SMARTER
          </div>
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 12.5,
              color: '#bcc8c4',
              lineHeight: 1.9,
            }}
          >
            answer → record attempt →<br />
            scheduler reweights to weak topics →<br />
            you see more of what you miss →{' '}
            <span style={{ color: '#5fe3aa' }}>mastery rises</span>
          </div>
        </div>
        <div
          style={{
            border: '1px solid rgba(167,139,250,.28)',
            borderRadius: 14,
            background: 'linear-gradient(180deg,#150f1f,#0e0b16)',
            padding: '20px 22px',
          }}
        >
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 12,
              color: '#c0aefb',
              marginBottom: 8,
            }}
          >
            FLYWHEEL ② — THE ENGINE GETS SMARTER
          </div>
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 12.5,
              color: '#bcc8c4',
              lineHeight: 1.9,
            }}
          >
            answer + 👍/👎/🚩 → item stats →<br />
            refine · retire · promote · harder variant →<br />
            better bank →{' '}
            <span style={{ color: '#c0aefb' }}>fine-tune the generator</span>
          </div>
        </div>
      </div>

      {/* Lifecycle */}
      <div
        style={{ marginTop: 26, fontSize: 15, fontWeight: 600, color: '#eef5f2', marginBottom: 13 }}
      >
        Question lifecycle
      </div>
      <div style={{ display: 'flex', alignItems: 'stretch', gap: 10, flexWrap: 'wrap' }}>
        {[
          {
            label: 'CANDIDATE',
            count: lifecycle.candidate,
            num: '#dfe7e4',
            border: 'rgba(120,140,135,.2)',
            bg: '#0d1314',
            desc: 'freshly generated, unproven',
          },
          {
            label: 'ACTIVE',
            count: lifecycle.active,
            num: '#9af7cf',
            border: 'rgba(52,211,153,.3)',
            bg: 'rgba(52,211,153,.05)',
            desc: 'serving · stats accruing',
          },
          {
            label: 'GOLDEN',
            count: lifecycle.golden,
            num: '#ffd479',
            border: 'rgba(245,185,69,.32)',
            bg: 'rgba(245,185,69,.05)',
            desc: 'high difficulty + discrimination',
          },
          {
            label: 'RETIRED',
            count: lifecycle.retired,
            num: '#f0888c',
            border: 'rgba(229,72,77,.28)',
            bg: 'rgba(229,72,77,.04)',
            desc: 'ambiguous / too easy / disliked',
          },
        ].map((item, i, arr) => (
          <React.Fragment key={item.label}>
            <div
              style={{
                flex: 1,
                minWidth: 150,
                border: `1px solid ${item.border}`,
                borderRadius: 12,
                background: item.bg,
                padding: '16px 17px',
              }}
            >
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 11,
                  color: '#9aa8a4',
                }}
              >
                {item.label}
              </div>
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 28,
                  fontWeight: 700,
                  color: item.num,
                  marginTop: 4,
                }}
              >
                {item.count}
              </div>
              <div style={{ fontSize: 11.5, color: '#7e8d89', marginTop: 4, lineHeight: 1.4 }}>
                {item.desc}
              </div>
            </div>
            {i < arr.length - 1 && i === 1 ? (
              <div
                key={`arrow-${i}`}
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: '#54625f',
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 11,
                  gap: 2,
                }}
              >
                <span>↗</span>
                <span>↘</span>
              </div>
            ) : i < arr.length - 1 ? (
              <div
                key={`arrow-${i}`}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  color: '#54625f',
                  fontFamily: "'JetBrains Mono', monospace",
                }}
              >
                →
              </div>
            ) : null}
          </React.Fragment>
        ))}
      </div>

      {/* Quality table + Refinement log */}
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: '1.15fr 1fr',
          gap: 18,
          marginTop: 26,
          alignItems: 'start',
        }}
      >
        {/* Item quality */}
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
              padding: '15px 20px',
              borderBottom: '1px solid rgba(120,140,135,.12)',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            <div style={{ fontSize: 14.5, fontWeight: 600, color: '#eef5f2' }}>Item quality</div>
            <div
              style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 10, color: '#7e8d89' }}
            >
              p = % correct · votes = net rating
            </div>
          </div>
          <div style={{ padding: '6px 14px 10px' }}>
            {/* Header */}
            <div
              style={{
                display: 'flex',
                gap: 10,
                padding: '8px 8px',
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 10,
                color: '#54625f',
                letterSpacing: 0.5,
              }}
            >
              <span style={{ width: 48 }}>ITEM</span>
              <span style={{ flex: 1 }}>TOPIC</span>
              <span style={{ width: 40, textAlign: 'right' }}>p</span>
              <span style={{ width: 50, textAlign: 'right' }}>votes</span>
              <span style={{ width: 74, textAlign: 'right' }}>STATUS</span>
            </div>
            {quality.length === 0 ? (
              <div
                style={{
                  padding: '16px 8px',
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 11,
                  color: '#54625f',
                }}
              >
                Answer questions to populate item stats.
              </div>
            ) : (
              quality.map((q) => (
                <div
                  key={q.id}
                  style={{
                    display: 'flex',
                    gap: 10,
                    alignItems: 'center',
                    padding: '9px 8px',
                    borderTop: '1px solid rgba(120,140,135,.08)',
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 12,
                  }}
                >
                  <span style={{ width: 48, color: '#9aa8a4' }}>{q.id}</span>
                  <span
                    style={{
                      flex: 1,
                      color: '#cdd6d3',
                      fontFamily: "'Space Grotesk', sans-serif",
                      fontSize: 12.5,
                      whiteSpace: 'nowrap',
                      overflow: 'hidden',
                      textOverflow: 'ellipsis',
                    }}
                  >
                    {q.topic}
                  </span>
                  <span style={{ width: 40, textAlign: 'right', color: pColor(q.difficulty) }}>
                    {q.difficulty !== null ? q.difficulty.toFixed(2) : '—'}
                  </span>
                  <span
                    style={{
                      width: 50,
                      textAlign: 'right',
                      color: q.net_votes >= 0 ? '#5fe3aa' : '#f0888c',
                    }}
                  >
                    {q.net_votes > 0 ? `+${q.net_votes}` : q.net_votes}
                  </span>
                  <span style={{ width: 74, textAlign: 'right' }}>{statusBadge(q.status)}</span>
                </div>
              ))
            )}
          </div>
        </div>

        {/* Refinement log */}
        <div
          style={{
            border: '1px solid rgba(120,140,135,.16)',
            borderRadius: 16,
            background: '#0d1314',
            overflow: 'hidden',
          }}
        >
          <div
            style={{ padding: '15px 20px', borderBottom: '1px solid rgba(120,140,135,.12)' }}
          >
            <div style={{ fontSize: 14.5, fontWeight: 600, color: '#eef5f2' }}>Refinement log</div>
            <div
              style={{
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 10,
                color: '#7e8d89',
                marginTop: 2,
              }}
            >
              engine events — newest first
            </div>
          </div>
          <div
            style={{
              padding: '14px 20px 18px',
              display: 'flex',
              flexDirection: 'column',
              gap: 13,
              maxHeight: 340,
              overflowY: 'auto',
            }}
          >
            {SEED_EVENTS.map((e, i) => (
              <div key={i} style={{ display: 'flex', gap: 11 }}>
                <span
                  style={{
                    fontFamily: "'JetBrains Mono', monospace",
                    fontSize: 14,
                    color: e.color,
                    flex: 'none',
                    lineHeight: 1.3,
                  }}
                >
                  {e.icon}
                </span>
                <div>
                  <span style={{ fontSize: 12.5, color: '#cdd6d3', lineHeight: 1.5 }}>{e.text}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Fine-tuning horizon */}
      <div
        style={{
          marginTop: 18,
          border: '1px dashed rgba(167,139,250,.3)',
          borderRadius: 16,
          background: '#0c0a14',
          padding: '20px 24px',
        }}
      >
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'baseline',
            flexWrap: 'wrap',
            gap: 8,
          }}
        >
          <div style={{ fontSize: 15, fontWeight: 600, color: '#eef5f2' }}>
            Fine-tuning horizon
          </div>
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 12,
              color: '#c0aefb',
            }}
          >
            {logged} / {target} logged answers
          </div>
        </div>
        <div
          style={{
            height: 9,
            borderRadius: 6,
            background: '#13191a',
            overflow: 'hidden',
            border: '1px solid rgba(120,140,135,.14)',
            marginTop: 12,
          }}
        >
          <div
            style={{
              height: '100%',
              width: `${loggedPct}%`,
              borderRadius: 6,
              background: 'linear-gradient(90deg,#a78bfacc,#a78bfa)',
              transition: 'width .5s ease',
            }}
          />
        </div>
        <div
          style={{
            fontSize: 12.5,
            color: '#9aa8a4',
            lineHeight: 1.55,
            marginTop: 12,
            maxWidth: 760,
          }}
        >
          At the threshold, the golden set plus your logged answers export as a supervised dataset
          — the generator gets fine-tuned on{' '}
          <span style={{ color: '#c0aefb' }}>your own</span> question style and misconceptions,
          the same instinct behind reaching for DistilBERT. Ollama swaps to the tuned model
          behind{' '}
          <span style={{ fontFamily: "'JetBrains Mono', monospace", color: '#bcc8c4' }}>
            ollama_client.py
          </span>{' '}
          with zero changes elsewhere.
        </div>
      </div>
    </div>
  );
}
