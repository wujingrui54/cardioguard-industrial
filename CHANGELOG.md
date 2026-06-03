# Changelog

All notable changes to **CardioGuard Industrial** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-06-03 · Competition Submission

### Added
- **Bilingual site (中文 / 한국어)** with right-aligned one-click language switcher and persistent preference via `localStorage`.
- **Five core narrative sections** matching the competition rubric: Method · Features · Data Dashboard · Effects · Other Information.
- **Four interactive Chart.js dashboards** (incidence trend, response time distribution, AED coverage doughnut, SHAP risk weights), with labels that re-render on language change.
- **One-click Korean PDF download** at the top-right corner. Primary path: pre-generated static PDF via Python + Malgun Gothic; fallback: `html2pdf.js` HTML-string mode.
- **Production-grade SEO/PWA assets**: Open Graph, Twitter Cards, JSON-LD (`SoftwareApplication` + `CreativeWork`), `manifest.json`, inline SVG favicon, `robots.txt`, `sitemap.xml`, polished `404.html`.
- **WCAG 2.1 AA accessibility**: semantic landmarks, ARIA labels, keyboard navigation, ≥ 4.5:1 contrast, skip links.
- **Static PDF generator** `generate_pdf.py` (fpdf2 + Windows Malgun Gothic) producing a 122 KB Korean PDF that contains all four required sections.
- **Academic documentation**: `PAPER_ZH.md`, `PAPER_KR.md`, `PAPER_EN.md`, `CITATION.cff`, `LICENSE` (MIT), `README.md`, `SUBMISSION.md`.

### Security & Privacy
- Front-end stores no personal data; all interactions are stateless.
- HTTPS-enforceable; CDN dependencies pinned to specific minor versions.
- AI disclosure: generative AI was used only for prose polishing and boilerplate; **no patient or subject data was ever fed to AI**.

### Reproducibility
- Pure static HTML5 / CSS3 / Vanilla JavaScript — no build step required.
- Local development: `python -m http.server 8765`.
- One-click deployment targets: Netlify Drop, GitHub Pages, Vercel.

---

## Verified Browsers

| Browser | Min Version | Status |
|---|---|---|
| Chrome / Edge | 90+ | ✅ Full support |
| Firefox | 88+ | ✅ Full support |
| Safari | 14+ | ✅ Full support |
| Mobile Safari (iOS) | 14+ | ✅ Responsive |
| Chrome Mobile (Android) | 90+ | ✅ Responsive |

---

## Roadmap (post-submission)

- **2026 Q3** — Pilot at two China-Korea joint-venture factories.
- **2026 Q4** — Complete 500-participant prospective cohort data collection.
- **2027 Q1** — MFDS (Korea) digital medical device pre-market notification.
- **2027 Q2** — Submit primary SCI paper; deploy at 10 industrial parks.
- **2027 Q4** — Southeast Asia extension (Vietnamese / Thai / English).
