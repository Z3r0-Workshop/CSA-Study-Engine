'use client';

type View = 'dashboard' | 'quiz' | 'engine';

interface Props {
  view: View;
  examReadiness: number;
  onNav: (v: View) => void;
}

const readinessLabel = (pct: number) =>
  pct >= 75 ? 'exam-ready' : pct >= 60 ? 'on track' : pct >= 45 ? 'getting there' : 'early days';

const readinessColor = (pct: number) =>
  pct >= 75 ? '#5fe3aa' : pct >= 60 ? '#9af7cf' : pct >= 45 ? '#f5b945' : '#f0888c';

export default function TopBar({ view, examReadiness, onNav }: Props) {
  const pct = Math.round(examReadiness * 100);
  const color = readinessColor(pct);

  const navBtn = (label: string, target: View) => {
    const active = view === target;
    return (
      <button
        key={target}
        onClick={() => onNav(target)}
        style={{
          fontFamily: "'JetBrains Mono', monospace",
          fontSize: 13,
          fontWeight: 600,
          padding: '8px 16px',
          borderRadius: 8,
          cursor: 'pointer',
          transition: 'all .15s ease',
          border: `1px solid ${active ? 'rgba(52,211,153,.5)' : 'rgba(120,140,135,.2)'}`,
          background: active ? 'rgba(52,211,153,.12)' : 'transparent',
          color: active ? '#5fe3aa' : '#7e8d89',
        }}
      >
        {label}
      </button>
    );
  };

  return (
    <div
      style={{
        position: 'sticky',
        top: 0,
        zIndex: 20,
        display: 'flex',
        alignItems: 'center',
        gap: 18,
        padding: '14px 26px',
        background: 'rgba(11,16,17,.86)',
        backdropFilter: 'blur(10px)',
        borderBottom: '1px solid rgba(120,140,135,.14)',
      }}
    >
      {/* Logo */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 11 }}>
        <div
          style={{
            width: 30,
            height: 30,
            borderRadius: 8,
            background: 'linear-gradient(135deg,#34d399,#0f8a5e)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontFamily: "'JetBrains Mono', monospace",
            fontWeight: 700,
            fontSize: 15,
            color: '#06140e',
            boxShadow: '0 0 0 1px rgba(52,211,153,.3)',
          }}
        >
          C
        </div>
        <div>
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 14,
              fontWeight: 600,
              color: '#eef5f2',
              lineHeight: 1,
            }}
          >
            CSA Engine
          </div>
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 10,
              color: '#54625f',
              lineHeight: 1.4,
            }}
          >
            study · local · v0.4
          </div>
        </div>
      </div>

      {/* Nav tabs */}
      <div
        style={{
          display: 'flex',
          gap: 4,
          marginLeft: 14,
          padding: 4,
          borderRadius: 11,
          border: '1px solid rgba(120,140,135,.16)',
          background: '#0a0f10',
        }}
      >
        {navBtn('Dashboard', 'dashboard')}
        {navBtn('Study', 'quiz')}
        {navBtn('Engine', 'engine')}
      </div>

      {/* Readiness */}
      <div style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: 14 }}>
        <div style={{ textAlign: 'right' }}>
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 10,
              color: '#7e8d89',
              letterSpacing: 1,
            }}
          >
            EXAM READINESS
          </div>
          <div
            style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize: 13,
              fontWeight: 600,
              color,
            }}
          >
            {pct}% · {readinessLabel(pct)}
          </div>
        </div>
        <div
          style={{
            width: 120,
            height: 8,
            borderRadius: 6,
            background: '#13191a',
            overflow: 'hidden',
            border: '1px solid rgba(120,140,135,.14)',
          }}
        >
          <div
            style={{
              height: '100%',
              width: `${pct}%`,
              borderRadius: 6,
              background: `linear-gradient(90deg,${color}cc,${color})`,
              transition: 'width .5s ease',
            }}
          />
        </div>
      </div>
    </div>
  );
}
