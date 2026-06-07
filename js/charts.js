/* ============================================================
   charts.js · Chart.js 数据可视化仪表盘
   4 charts: Incidence trend / Response time / AED coverage / Risk SHAP
   ============================================================ */
(function(){
  'use strict';

  // Graceful degradation: if the Chart.js CDN is blocked/offline, do not throw.
  if (typeof Chart === 'undefined') {
    window.CardioCharts = { refresh: function(){} };
    return;
  }

  const t = (k) => (window.CardioApp ? window.CardioApp.t(k) : k);

  // Common styles
  const GRID = 'rgba(148,163,184,0.15)';
  const TICK = '#94A3B8';
  const FONT = "'Noto Sans SC','Noto Sans KR','Inter',system-ui,sans-serif";

  Chart.defaults.color = TICK;
  Chart.defaults.font.family = FONT;
  Chart.defaults.font.size = 12;

  let chartIncidence, chartResponse, chartCoverage, chartRisk;

  function monthLabels(){
    return ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
      .map(m => t('chart.month.' + m));
  }

  // ----- 1. Incidence trend (line) -----
  function buildIncidence(){
    const ctx = document.getElementById('chartIncidence');
    if (!ctx) return;
    const grad = ctx.getContext('2d').createLinearGradient(0, 0, 0, 280);
    grad.addColorStop(0, 'rgba(239,68,68,0.45)');
    grad.addColorStop(1, 'rgba(239,68,68,0.00)');

    chartIncidence = new Chart(ctx, {
      type: 'line',
      data: {
        labels: monthLabels(),
        datasets: [{
          label: t('chart.incidence.label'),
          data: [3.2, 3.5, 3.1, 2.9, 2.7, 3.4, 4.1, 4.3, 3.6, 3.2, 3.0, 3.8],
          borderColor: '#EF4444',
          backgroundColor: grad,
          borderWidth: 2.5,
          tension: 0.4,
          fill: true,
          pointRadius: 4,
          pointHoverRadius: 6,
          pointBackgroundColor: '#fff',
          pointBorderColor: '#EF4444',
          pointBorderWidth: 2
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: '#0F172A',
            borderColor: '#334155',
            borderWidth: 1,
            padding: 10,
            callbacks: {
              label: (c) => ` ${c.parsed.y.toFixed(1)} / 10⁵ h`
            }
          }
        },
        scales: {
          x: { grid: { color: GRID }, ticks: { color: TICK } },
          y: { grid: { color: GRID }, ticks: { color: TICK }, beginAtZero: true }
        }
      }
    });
  }

  // ----- 2. Response time (bar) -----
  function buildResponse(){
    const ctx = document.getElementById('chartResponse');
    if (!ctx) return;

    const labels = [
      t('chart.response.bin1'), t('chart.response.bin2'),
      t('chart.response.bin3'), t('chart.response.bin4'), t('chart.response.bin5')
    ];

    chartResponse = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: t('chart.response.label'),
          data: [42, 68, 35, 18, 9],
          backgroundColor: [
            'rgba(16,185,129,0.85)',
            'rgba(59,130,246,0.85)',
            'rgba(245,158,11,0.85)',
            'rgba(239,68,68,0.85)',
            'rgba(127,29,29,0.85)'
          ],
          borderRadius: 8,
          borderSkipped: false
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: '#0F172A',
            borderColor: '#334155',
            borderWidth: 1,
            padding: 10
          }
        },
        scales: {
          x: { grid: { display: false }, ticks: { color: TICK } },
          y: { grid: { color: GRID }, ticks: { color: TICK }, beginAtZero: true }
        }
      }
    });
  }

  // ----- 3. AED Coverage (doughnut comparison) -----
  function buildCoverage(){
    const ctx = document.getElementById('chartCoverage');
    if (!ctx) return;

    chartCoverage = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: [
          t('chart.coverage.before') + ' · ' + t('chart.coverage.covered'),
          t('chart.coverage.before') + ' · ' + t('chart.coverage.uncovered'),
          t('chart.coverage.after')  + ' · ' + t('chart.coverage.covered'),
          t('chart.coverage.after')  + ' · ' + t('chart.coverage.uncovered')
        ],
        datasets: [
          {
            label: t('chart.coverage.before'),
            data: [38, 62, 0, 0],
            backgroundColor: ['rgba(59,130,246,0.85)', 'rgba(59,130,246,0.18)', 'transparent', 'transparent'],
            borderWidth: 0,
            cutout: '60%'
          },
          {
            label: t('chart.coverage.after'),
            data: [0, 0, 91, 9],
            backgroundColor: ['transparent', 'transparent', 'rgba(239,68,68,0.9)', 'rgba(239,68,68,0.18)'],
            borderWidth: 0,
            cutout: '60%'
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { color: TICK, padding: 12, font: { size: 11 }, boxWidth: 12 }
          },
          tooltip: {
            backgroundColor: '#0F172A',
            borderColor: '#334155',
            borderWidth: 1,
            padding: 10,
            callbacks: { label: (c) => ` ${c.label}: ${c.parsed}%` }
          }
        }
      }
    });
  }

  // ----- 4. Risk factor weights (horizontal bar) -----
  function buildRisk(){
    const ctx = document.getElementById('chartRisk');
    if (!ctx) return;

    chartRisk = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [
          t('chart.risk.f1'), t('chart.risk.f2'), t('chart.risk.f3'),
          t('chart.risk.f4'), t('chart.risk.f5'), t('chart.risk.f6')
        ],
        datasets: [{
          label: 'SHAP',
          data: [0.28, 0.24, 0.19, 0.13, 0.09, 0.07],
          backgroundColor: [
            'rgba(239,68,68,0.85)',
            'rgba(245,158,11,0.85)',
            'rgba(139,92,246,0.85)',
            'rgba(59,130,246,0.85)',
            'rgba(6,182,212,0.85)',
            'rgba(16,185,129,0.85)'
          ],
          borderRadius: 6
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: '#0F172A',
            borderColor: '#334155',
            borderWidth: 1,
            padding: 10,
            callbacks: { label: (c) => ` SHAP = ${c.parsed.x.toFixed(2)}` }
          }
        },
        scales: {
          x: { grid: { color: GRID }, ticks: { color: TICK }, beginAtZero: true, max: 0.32 },
          y: { grid: { display: false }, ticks: { color: TICK } }
        }
      }
    });
  }

  function buildAll(){
    buildIncidence();
    buildResponse();
    buildCoverage();
    buildRisk();
  }

  function refresh(){
    [chartIncidence, chartResponse, chartCoverage, chartRisk].forEach(c => { if (c) c.destroy(); });
    buildAll();
  }

  // Expose to main.js so language switch can refresh charts
  window.CardioCharts = { refresh: refresh };

  document.addEventListener('DOMContentLoaded', () => {
    // small delay to ensure i18n applied first
    setTimeout(buildAll, 50);
  });
})();
