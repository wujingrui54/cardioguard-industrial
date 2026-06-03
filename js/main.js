/* ============================================================
   main.js · 语言切换 + PDF 导出 + UI 交互
   ============================================================ */
(function(){
  'use strict';

  const html = document.documentElement;
  const STORAGE_KEY = 'cardioguard.lang';

  // ---------------- i18n apply ----------------
  function applyLang(lang){
    if (!window.I18N || !window.I18N[lang]) return;
    const dict = window.I18N[lang];

    // text content
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const val = dict[key];
      if (val !== undefined) {
        if (el.tagName === 'TITLE') el.textContent = val;
        else el.textContent = val;
      }
    });

    // html attributes
    document.querySelectorAll('[data-i18n-attr]').forEach(el => {
      const map = el.getAttribute('data-i18n-attr');
      map.split(',').forEach(pair => {
        const [attr, key] = pair.split(':').map(s => s.trim());
        const val = dict[key];
        if (val !== undefined) el.setAttribute(attr, val);
      });
    });

    // html lang
    html.setAttribute('lang', lang === 'zh' ? 'zh-CN' : 'ko-KR');
    html.setAttribute('data-lang', lang);

    // language button states
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // persist
    try { localStorage.setItem(STORAGE_KEY, lang); } catch(e){}

    // notify charts to re-render labels
    if (window.CardioCharts && typeof window.CardioCharts.refresh === 'function') {
      window.CardioCharts.refresh(lang);
    }

    // toast
    const key = lang === 'zh' ? 'toast.langZh' : 'toast.langKo';
    showToast(dict[key]);
  }

  // ---------------- toast ----------------
  let toastTimer = null;
  function showToast(msg){
    const t = document.getElementById('toast');
    if (!t) return;
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.classList.remove('show'), 1800);
  }

  // ---------------- PDF download ----------------
  // Strategy: prefer the pre-generated static PDF (assets/CardioGuard_Industrial_KR.pdf)
  // built by `python generate_pdf.py` — perfect Korean rendering via Malgun Gothic,
  // 100% reliable, no font/canvas race conditions.
  // If the static file is missing (e.g. file:// without server), fall back to
  // html2pdf.js with HTML-string input (DOM-element input rasterizes a blank
  // canvas in many Chromium environments).
  const STATIC_PDF = 'assets/CardioGuard_Industrial_KR.pdf';

  async function downloadPdf(){
    const btn = document.getElementById('downloadPdfBtn');
    const dict = window.I18N[html.getAttribute('data-lang') || 'zh'];
    if (btn) btn.setAttribute('disabled', 'true');
    showToast(dict['toast.pdfGen']);

    // Try static PDF first
    try {
      const resp = await fetch(STATIC_PDF, { cache: 'no-store' });
      if (resp.ok && resp.headers.get('content-type')?.includes('pdf')) {
        const blob = await resp.blob();
        if (blob.size > 10000) {
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = 'CardioGuard_Industrial_KR.pdf';
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
          setTimeout(() => URL.revokeObjectURL(url), 1000);
          if (btn) btn.removeAttribute('disabled');
          showToast(dict['toast.pdfDone']);
          return;
        }
      }
    } catch (e) {
      console.warn('[Static PDF unavailable, falling back to html2pdf]', e);
    }

    // Fallback: client-side generation
    _generatePdfClientSide(btn, dict);
  }

  function _generatePdfClientSide(btn, dict){
    const src = document.getElementById('pdfSource');
    if (!src) {
      showToast(dict['toast.pdfErr']);
      if (btn) btn.removeAttribute('disabled');
      return;
    }

    const stamp = new Date().toISOString().slice(0, 10);
    const filename = `CardioGuard_Industrial_KR_${stamp}.pdf`;

    // Loading overlay so the user sees progress feedback
    const overlay = document.createElement('div');
    overlay.id = 'pdfOverlay';
    overlay.style.cssText = [
      'position:fixed','inset:0','z-index:99999',
      'background:rgba(11,17,32,0.94)',
      'backdrop-filter:blur(6px)','-webkit-backdrop-filter:blur(6px)',
      'display:flex','align-items:center','justify-content:center',
      'flex-direction:column','gap:18px',
      'color:#F8FAFC','font-size:16px','font-weight:600',
      'font-family:"Noto Sans SC","Noto Sans KR","Inter",sans-serif'
    ].join(';');
    overlay.innerHTML =
      '<div style="width:48px;height:48px;border:4px solid rgba(255,255,255,.15);border-top-color:#EF4444;border-radius:50%;animation:pdfspin 1s linear infinite;"></div>' +
      '<div>' + dict['toast.pdfGen'] + '</div>' +
      '<style>@keyframes pdfspin{to{transform:rotate(360deg)}}</style>';
    document.body.appendChild(overlay);

    // Build an inline-styled wrapper around #pdfSource.innerHTML so the PDF is
    // self-contained and does not depend on the external stylesheet (which
    // html2pdf's clone iframe may or may not load).
    const wrapper =
      '<div style="' +
        'width:794px;padding:48px 56px;' +
        'background:#ffffff;color:#111;' +
        'font-family:\'Noto Sans KR\',\'Malgun Gothic\',\'Noto Sans SC\',sans-serif;' +
        'line-height:1.65;font-size:12.5px;' +
      '">' + src.innerHTML + '</div>';

    const opt = {
      margin: [12, 12, 14, 12],
      filename: filename,
      image: { type: 'jpeg', quality: 0.96 },
      html2canvas: {
        scale: 2,
        useCORS: true,
        letterRendering: true,
        backgroundColor: '#ffffff',
        logging: false,
        windowWidth: 794
      },
      jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait', compress: true },
      pagebreak: { mode: ['css', 'legacy'] }
    };

    html2pdf().set(opt).from(wrapper, 'string').save().then(() => {
      if (document.body.contains(overlay)) document.body.removeChild(overlay);
      if (btn) btn.removeAttribute('disabled');
      showToast(dict['toast.pdfDone']);
    }).catch(err => {
      console.error('[PDF generation failed]', err);
      if (document.body.contains(overlay)) document.body.removeChild(overlay);
      if (btn) btn.removeAttribute('disabled');
      showToast(dict['toast.pdfErr']);
    });
  }

  // ---------------- reveal on scroll ----------------
  function setupReveal(){
    const els = document.querySelectorAll('.section .method-card, .section .feature-card, .section .chart-card, .section .effect-card, .section .other-card');
    els.forEach(el => el.classList.add('reveal'));
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12 });
    els.forEach(el => io.observe(el));
  }

  // ---------------- bind ----------------
  document.addEventListener('DOMContentLoaded', () => {
    // Lang precedence: ?lang=xx URL param > localStorage > default 'zh'.
    // URL param is preferred so links like /?lang=ko share the Korean view
    // and so headless screenshot tools can request a specific locale.
    let lang = 'zh';
    try {
      const url = new URLSearchParams(location.search).get('lang');
      if (url === 'zh' || url === 'ko') {
        lang = url;
      } else {
        lang = localStorage.getItem(STORAGE_KEY) || 'zh';
      }
    } catch(e){}
    applyLang(lang);

    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.addEventListener('click', () => applyLang(btn.getAttribute('data-lang')));
    });

    const dl = document.getElementById('downloadPdfBtn');
    if (dl) dl.addEventListener('click', downloadPdf);

    setupReveal();
  });

  // export for charts module
  window.CardioApp = {
    getLang: () => html.getAttribute('data-lang') || 'zh',
    t: (key) => {
      const lang = html.getAttribute('data-lang') || 'zh';
      return (window.I18N[lang] && window.I18N[lang][key]) || key;
    }
  };
})();
