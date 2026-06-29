/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}', './lib/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        bg: '#0a0d0e',
        surface: '#0d1314',
        surfaceHigh: '#11181a',
        border: 'rgba(120,140,135,0.16)',
        borderDim: 'rgba(120,140,135,0.08)',
        green: '#34d399',
        greenL: '#5fe3aa',
        greenXL: '#9af7cf',
        violet: '#a78bfa',
        violetL: '#c0aefb',
        cyan: '#38bdf8',
        cyanL: '#7ad0fb',
        amber: '#f5b945',
        red: '#e5484d',
        redL: '#f0888c',
        text: '#dfe7e4',
        textHigh: '#eef5f2',
        muted: '#9aa8a4',
        dim: '#7e8d89',
        dimmer: '#54625f',
      },
      fontFamily: {
        sans: ['Space Grotesk', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      animation: {
        'fade-in': 'fadeIn 0.2s ease',
      },
      keyframes: {
        fadeIn: {
          from: { opacity: '0', transform: 'translateY(6px)' },
          to: { opacity: '1', transform: 'none' },
        },
      },
    },
  },
  plugins: [],
};
