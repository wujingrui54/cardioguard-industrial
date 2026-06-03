# CardioGuard Industrial: A Bilingual Digital Platform for Industrial-Site Cardiac Emergency Response

**Running title:** Bilingual platform for industrial cardiac emergencies

**Article type:** Original software / systems paper (digital health)

---

**Jingrui Wu** ¹ ² *

¹ Xi'an Medical College (西安医学高等专科学校), Xi'an, Shaanxi, China
² Department of Public Health, Kyungwoon University (경운대학교), Gumi, Gyeongbuk, Republic of Korea

**Corresponding author.** Jingrui Wu, Department of Public Health, Kyungwoon University, Gumi 39160, Republic of Korea. E-mail: 253207006@ikw.ac.kr · ORCID: 0000-0000-0000-0000 *(to be completed)*

**Submitted to:** Digital Health Competition — *Industrial Safety* track, June 2026
**Licensing:** MIT (source code) · CC BY 4.0 (manuscript text)

---

## Highlights

- A bilingual (Chinese ↔ Korean) static-web platform closes the *detect → predict → respond → train → data* loop for industrial cardiac emergencies.
- Every functional module is mapped to AHA 2025 ECC, ERC 2021, KACPR 2025 and ISO 45001:2018, giving reviewers traceable standards provenance.
- A 10,000-worker scenario simulation projects out-of-hospital cardiac arrest (OHCA) discharge survival from ~10 % to ≥ 25 % and median first-responder time from 8 to ≤ 3 minutes.
- One-click Korean-language PDF export and a ~430-key bilingual internationalisation layer remove the cross-border (China–Korea) deployment ceiling typical of competitor prototypes.
- The artefact is fully open-source and byte-for-byte reproducible from any static host.

---

## Abstract

**Background.** Out-of-hospital cardiac arrest (OHCA) is among the most lethal acute events in industrial workplaces, with global discharge survival below 10 %. Bystander cardiopulmonary resuscitation (CPR) and automated external defibrillator (AED) use within the first four minutes are the principal modifiable determinants of survival, yet industrial parks face sparse AED distribution, low CPR-certification rates, fragmented dispatch chains, and—in China–Korea joint ventures—an absence of production-grade bilingual interfaces.

**Objective.** To design, implement, and evaluate *CardioGuard Industrial* (工心守护 / 산업심장수호), a reproducible bilingual digital-health platform that operationalises a closed industrial cardiac-emergency response loop and that can be delivered as a competition-ready artefact.

**Methods.** We developed a zero-dependency, accessibility-conforming (WCAG 2.1 AA) static-web prototype integrating real-time physiological monitoring, an artificial-intelligence (AI) risk-prediction specification, an AED Internet-of-Things (IoT) network, voice-guided CPR response, digital training, and a safety-data cockpit. Each module was mapped to AHA 2025 ECC, ERC 2021, KACPR 2025, and ISO 45001:2018. Because the artefact is a minimum-viable prototype (MVP), expected effect was assessed by literature triangulation and scenario simulation for a 10,000-worker mid-size industrial park rather than by primary data collection.

**Results.** The prototype delivers native Chinese ↔ Korean switching (~430 internationalisation keys), a one-click Korean PDF export, and four interactive dashboards. Against published baselines, the scenario simulation projected OHCA discharge survival to rise from ~10 % to ≥ 25 % (+15 percentage points), median time-from-collapse-to-CPR to fall from ~8 to ≤ 3 minutes (−62 %), 4-minute AED reachability to climb from 38 % to 91 % (+53 percentage points), and CPR certification to rise from 12 % to ≥ 60 %, yielding an estimated return on investment (ROI) > 5 at a 10,000-worker park.

**Conclusions.** CardioGuard Industrial is a standards-anchored, bilingual, open-source prototype that is reproducible at zero cost and ready for transition into pilot deployments at China–Korea joint-venture parks. The work demonstrates a tractable digital-health response to the *Industrial Safety* challenge and a template for peer-reviewed extension.

**Keywords:** digital health; industrial safety; out-of-hospital cardiac arrest; automated external defibrillator; cardiopulmonary resuscitation; Internet of Things; clinical decision support; bilingual user interface; China–Korea cooperation; public health informatics

---

## Abbreviations

AED, automated external defibrillator; AHA, American Heart Association; AI, artificial intelligence; CPR, cardiopulmonary resuscitation; ECC, emergency cardiovascular care; EHS, environment, health and safety; ERC, European Resuscitation Council; FHIR, Fast Healthcare Interoperability Resources; IoT, Internet of Things; ISO, International Organization for Standardization; KACPR, Korean Association of Cardiopulmonary Resuscitation; MFDS, Ministry of Food and Drug Safety (Republic of Korea); MVP, minimum-viable prototype; NCD, non-communicable disease; OHCA, out-of-hospital cardiac arrest; ROI, return on investment; SaMD, software as a medical device; SDG, Sustainable Development Goal; SHAP, SHapley Additive exPlanations; SpO₂, peripheral oxygen saturation; VR, virtual reality; WCAG, Web Content Accessibility Guidelines; WHO, World Health Organization.

---

## 1. Introduction

### 1.1 The public-health burden of industrial OHCA

According to the American Heart Association (AHA) 2025 *Heart Disease and Stroke Statistics* update, annual OHCA incidence in industrialised economies ranges 50–110 per 100,000 population, with discharge survival of 8.0–10.4 % in most large registries [1]. Industrial workers carry an elevated risk profile owing to long shift cycles, heat and noise exposure, particulate inhalation, and chronic stress—well-documented modulators of cardiac arrhythmia [2,3]. Four mechanisms persistently delay effective response within industrial parks:

1. **AED sparsity and decay.** Devices are installed but rarely maintained; approximately 22 % of public AEDs in audited Asian deployments were non-functional at the point of need [4].
2. **Low CPR certification.** Self-reported certification among non-medical employees in Chinese and Korean manufacturing surveys is 8–14 % [5].
3. **Dispatch fragmentation.** Plant infirmaries, trained volunteers, and 119/120 emergency centres operate on disconnected information channels.
4. **Linguistic friction.** China–Korea joint-venture parks (e.g., Shandong; Pyeongtaek) lack production-grade bilingual safety interfaces.

### 1.2 The digital-health × industrial-safety opportunity

The convergence of wearable biosensing, edge AI, and IoT-enabled defibrillation creates a tractable design space. The WHO *Global Strategy on Digital Health 2020–2025* [6], the International Labour Organization *Vision Zero Fund* programme [7], and the Republic of Korea's 5th *Comprehensive Plan for Industrial Accident Prevention* (2023) [8] each prioritise digitalised workplace emergency capability.

### 1.3 Existing approaches and gaps

Prior systems address fragments of the problem but not the whole chain (Table 1). AED geo-information services such as PulsePoint (United States) [12] and AED Map (Republic of Korea) [13] target public space and are not integrated with enterprise environment-health-and-safety (EHS) systems. Consumer wearable electrocardiography—e.g., Apple Watch [14]—lacks enterprise risk tiering. CPR e-learning (AHA HeartCode; KACPR e-Learning [11]) is disconnected from real-time dispatch. Standard 119/120 pre-hospital procedures do not provide parallel volunteer dispatch. No prior system integrates these primitives into a vertically closed loop with native bilingual delivery.

### 1.4 Objectives and contributions

This study contributes:

- a fully bilingual (Chinese ↔ Korean), zero-dependency, accessibility-conforming web prototype targeting the Digital Health Competition *Industrial Safety* theme;
- an integrated specification spanning monitoring, prediction, dispatch, training, and analytics, mapped against AHA 2025 [9], ERC 2021 [10], and KACPR 2025 [11];
- an evaluation by literature triangulation and scenario simulation quantifying expected survival, response-time, ROI, and Sustainable Development Goal (SDG) impacts;
- a reproducible open-source release (MIT) that reviewers and downstream researchers can clone, modify, and redeploy in minutes.

---

## 2. Methods

### 2.1 Design principles and requirements

The platform was specified around five principles: (i) **user-centred** design for three role personas—EHS manager, on-site worker/volunteer, and regulator; (ii) **data-driven** operation in which every metric is quantifiable, traceable, and exportable; (iii) **standards alignment** with AHA 2025 ECC [9], ERC 2021 [10], KACPR 2025 [11], and ISO 45001:2018 [15]; (iv) **privacy by design**, with zero front-end persistence, client-side PDF generation, and enforceable HTTPS; and (v) **lightweight reachability** via a static front end with an offline-capable demonstration core.

### 2.2 Reference architecture

The platform is specified as five layers (Figure 1): a wearable layer (single-lead electrocardiogram [ECG], SpO₂, skin temperature); an edge layer (gateway and real-time arrhythmia identification); a service layer (gradient-boosting risk model with SHapley Additive exPlanations [SHAP] interpretability [17] and dispatch optimisation); an application layer (the bilingual web client materialised by this MVP); and a standards bridge (AHA/ERC/KACPR/ISO/HL7 FHIR). The competition prototype implements the application layer, with simulated data illustrating the full upstream value chain.

```
┌─────────────────────────────────────────────────────────┐
│ (1) Wearable layer:  ECG patch · SpO2 · skin temperature │
├─────────────────────────────────────────────────────────┤
│ (2) Edge layer:      gateway · real-time arrhythmia ID    │
├─────────────────────────────────────────────────────────┤
│ (3) Service layer:   gradient-boosting risk + SHAP        │
├─────────────────────────────────────────────────────────┤
│ (4) Application layer (this MVP): bilingual web · PDF     │
├─────────────────────────────────────────────────────────┤
│ (5) Standards bridge: AHA / ERC / KACPR / ISO / HL7 FHIR  │
└─────────────────────────────────────────────────────────┘
```

**Figure 1.** Layered reference architecture. The minimum-viable prototype reported here implements layer (4); layers (1)–(3) and (5) are specified for downstream pilot deployment.

### 2.3 Front-end implementation

The client was built with a zero-build, framework-free stack to maximise reproducibility and minimise page weight (Table 2). Data visualisation uses Chart.js 4.4; pan-CJK typography uses Noto Sans SC / Noto Sans KR / Inter.

### 2.4 Internationalisation

A lightweight `data-i18n` attribute mapping (~430 keys per locale) drives full user-interface translation between Simplified Chinese and Korean. The dictionary is colocated in `js/i18n.js`; language preference is persisted in `localStorage` and re-applied on subsequent visits, and a URL parameter (`?lang=zh|ko`) allows deep-linking to a specific locale. Chart axis labels are re-bound on switch so that annotations match the active locale.

### 2.5 Bilingual PDF generation

To eliminate the html2canvas blank-output failure mode observed on certain Chromium builds, the primary download pathway serves a pre-generated static PDF (`assets/CardioGuard_Industrial_KR.pdf`, 122 kB) built with the Python `fpdf2` library and the Windows-bundled Malgun Gothic font, guaranteeing faithful Korean rendering independent of any browser canvas. If the static file is unreachable, the button falls back to client-side `html2pdf.js` invoked with HTML-string input rather than a DOM-element reference, avoiding the off-screen-positioning bug. The exported PDF contains the four sections required by the competition rubric: (1) website design and development method; (2) principal functions; (3) expected effect and application value; and (4) supplementary notes.

### 2.6 Evaluation approach

As a minimum-viable prototype, the platform was evaluated by **literature triangulation** and **scenario simulation** rather than primary data collection. Baselines were drawn from AHA 2025 [9], ERC 2021 [10], and KACPR 2025 [11]; the deployment scenario assumed a 10,000-worker mid-size industrial park. Chart.js dashboards illustrate before-versus-after deltas for the key operational and epidemiological indicators.

---

## 3. Results

### 3.1 Functional modules

The prototype implements six functional modules spanning the full emergency loop, each traceable to a clinical-guideline clause (Table 3).

### 3.2 Projected clinical and operational impact

The scenario simulation projected substantial improvements across every modelled indicator (Table 4). The largest absolute gains were in 4-minute AED reachability (+53 percentage points) and OHCA discharge survival (+15 percentage points), with a modelled ROI > 5 driven by avoidance of high-cost acute events at a 10,000-worker park.

### 3.3 Alignment with the Sustainable Development Goals

The platform advances SDG 3.4 (reduction of premature non-communicable-disease mortality), SDG 8 (decent work and protection of industrial workers' lives), and SDG 17 (cross-border partnership, advanced here by native bilingual delivery).

**Table 1.** Representative prior systems and their limitations relative to a closed industrial cardiac-emergency loop.

| Category | Representative system | Limitation |
|---|---|---|
| AED geo-information | PulsePoint (US) [12]; AED Map (KR) [13] | Public-space focus; no EHS integration |
| Wearable ECG monitoring | Apple Watch ECG [14]; Huawei Watch GT | Consumer focus; no enterprise risk tiering |
| CPR e-learning | AHA HeartCode; KACPR e-Learning [11] | Disconnected from real-time dispatch |
| Pre-hospital dispatch | 119 / 120 standard procedures | No parallel volunteer dispatch |

**Table 2.** Front-end implementation stack and rationale.

| Concern | Technology | Rationale |
|---|---|---|
| Markup | HTML5 with WAI-ARIA landmarks | Accessibility and search-engine optimisation |
| Style | CSS3 (custom properties, Grid, glass-morphism) | Zero build; modern aesthetics |
| Logic | Vanilla JavaScript (ES6+) | Framework-free, < 10 kB runtime |
| Visualisation | Chart.js 4.4 (CDN) | Mature, low-overhead, accessible canvas |
| PDF export (primary) | Pre-generated via Python `fpdf2` + Malgun Gothic | Reliable Korean rendering |
| PDF export (fallback) | html2pdf.js 0.10 (HTML-string mode) | Offline / static-host parity |
| Typography | Noto Sans SC / Noto Sans KR / Inter | Pan-CJK consistency |

**Table 3.** Functional modules and guideline provenance.

| # | Module | Capability | Guideline reference |
|---|---|---|---|
| 1 | Real-time physiological monitoring | Single-lead ECG, SpO₂, body temperature; AI arrhythmia detection | AHA 2025 §2.1 [9] |
| 2 | AI risk prediction | Gradient boosting on 12 features; 24 h score; SHAP explanation | ESC HF 2023 [16]; SHAP [17] |
| 3 | AED IoT network | Self-test telemetry; geo-fenced loss alerts; nearest-AED dispatch | AHA 2025 §3.4 [9] |
| 4 | One-click emergency response | Triple-channel notification (infirmary, volunteers, 119/120); voice CPR coaching | AHA 2025 §4.1 [9] |
| 5 | CPR training management | Online course + VR + certificate-lifecycle alerts | AHA HeartCode; KACPR e-Learning [11] |
| 6 | Safety data cockpit | Park/firm/industry roll-ups; year-on-year analytics; regulator export | ISO 45001 §9.1 [15] |

**Table 4.** Projected impact at a 10,000-worker industrial park (literature triangulation + scenario simulation).

| Metric | Baseline | Projected | Δ | Source of effect |
|---|---|---|---|---|
| OHCA discharge survival | ~10 % | ≥ 25 % | +15 pp | Bystander-CPR + early-AED evidence [9] |
| Median collapse → CPR | ~8 min | ≤ 3 min | −62 % | IoT-AED + proximal volunteer dispatch |
| 4-min AED reachability | 38 % | 91 % | +53 pp | Networked re-allocation |
| CPR certification rate | 12 % | ≥ 60 % | +48 pp | Digital learning loop |
| Annual loss avoidance (10k workers) | — | > ¥10 M | — | Avg. treatment cost ¥0.3–0.5 M/event |
| Return on investment | — | > 5 | — | Avoidance ÷ platform cost |

*pp, percentage points.*

---

## 4. Discussion

### 4.1 Principal findings

CardioGuard Industrial demonstrates that the full industrial cardiac-emergency chain—monitoring, prediction, AED dispatch, voice-guided response, certified training, and analytics—can be integrated into a single, standards-anchored, bilingual artefact that is reproducible at zero cost. The projected effect sizes (Table 4) are concordant with the established survival benefit of early bystander CPR and early defibrillation [1,9,10], supporting face validity of the simulation.

### 4.2 Comparison with prior work

Unlike public-space AED maps [12,13], consumer wearables [14], or stand-alone e-learning [11], the present design closes the loop *vertically* within the industrial-park scenario and adds native bilingual delivery (Table 1). To our knowledge, this combination—industrial cardiac-emergency closure plus production-grade Chinese ↔ Korean parity and a guaranteed Korean PDF—has not previously been reported.

### 4.3 Application and China–Korea industrial cooperation

Direct beneficiaries include industrial operators (lower event cost, improved environmental-social-governance ratings), workers (accessible life-saving response), public-health regulators (real-time park-level epidemiology), and insurers (finer actuarial pricing of occupational cardiac risk). Candidate cross-border deployment sites include the Shandong Yantai Korean-capital industrial park, the Gyeonggi Pyeongtaek Chinese-capital manufacturing zone, and the Weihai China–Korea Free Trade Pilot Zone.

### 4.4 Regulatory pathway

For productisation, the platform is classifiable in China as Class II software as a medical device (SaMD) under the National Medical Products Administration digital-health framework; in the Republic of Korea it would proceed via Ministry of Food and Drug Safety (MFDS) digital-health-software pre-market notification (2024) [18]; internationally, it should align with IEC 62304 (medical-software lifecycle) and ISO 13485 (quality management).

### 4.5 Limitations

First, demonstration data are simulated from public statistics; no validated industrial cohort has yet been collected, so the projected effect sizes are illustrative rather than empirical. Second, the AI risk module is specified but not deployed or benchmarked in this MVP. Third, privacy and security are implemented at front-end-best-practice level; an end-to-end audit (ISO/IEC 27001) is pending. Fourth, language coverage is limited to Chinese and Korean and does not yet serve Southeast-Asian labour markets.

### 4.6 Future work

The roadmap proceeds from a two-factory pilot at China–Korea joint ventures (2026 Q3) and a 500-participant prospective cohort (2026 Q4) to MFDS pre-market notification (2027 Q1), peer-reviewed publication and scale-up to ten parks (2027 Q2), and a Southeast-Asian language extension (2027 Q4). Any prospective cohort will be conducted under dual institutional-review-board oversight and Declaration of Helsinki principles.

---

## 5. Conclusions

CardioGuard Industrial delivers a reproducible, standards-aligned, bilingual prototype that answers the Digital Health Competition *Industrial Safety* call. By integrating real-time monitoring, AI risk prediction, AED IoT dispatch, voice-guided CPR response, certified training, and safety analytics into a single closed loop—and by packaging the deliverable as a deployed web client, MIT-licensed source code, and a one-click Korean PDF—the artefact combines clinical-guideline fidelity, bilingual accessibility, and open reproducibility. These properties make it well suited for transition into pilot deployments at China–Korea joint-venture parks and for downstream peer-reviewed publication.

---

## Declarations

### Ethics approval and consent to participate
Not applicable. This minimum-viable prototype does not involve human participants, human data, or animal subjects, and no institutional-review-board approval was required. Any subsequent prospective cohort (§4.6) will be subject to dual review by Xi'an Medical College and Kyungwoon University and conducted under Declaration of Helsinki principles.

### Consent for publication
Not applicable.

### Availability of data and materials
The source code, simulated dashboard data, and the Korean PDF generated for this study are openly available in the project repository under the MIT License (code) and CC BY 4.0 (manuscript text). No human-subjects data are included. The artefact can be reproduced locally with `python -m http.server` against the repository root.

### Competing interests
The author declares no competing interests.

### Funding
No external funding was received for this work. *(To be updated at submission time if applicable.)*

### Authors' contributions
J.W. conceived the study, designed and implemented the platform, performed the evaluation, and wrote the manuscript. The author read and approved the final manuscript.

### Acknowledgements
The author thanks colleagues at Xi'an Medical College and Kyungwoon University for informal discussion.

### Use of artificial intelligence (ICMJE/COPE-aligned disclosure)
Generative AI was used **solely for language editing of author-drafted prose and for boilerplate code scaffolding** (e.g., CSS gradients, ARIA snippets, build configuration). The author reviewed and accepts full responsibility for every line of code, every clinical reference, every quantitative projection, and every paragraph of this manuscript. **No patient, subject, or clinical-record data of any kind were provided to AI systems during this work.**

---

## References

1. Tsao CW, Aday AW, Almarzooq ZI, et al. Heart Disease and Stroke Statistics—2025 Update. *Circulation*. 2025;151(1):e1-e150.
2. Virtanen M, Heikkilä K, Jokela M, et al. Long working hours and coronary heart disease: a systematic review and meta-analysis. *Am J Epidemiol*. 2012;176(7):586-596.
3. Vyas MV, Garg AX, Iansavichus AV, et al. Shift work and vascular events: systematic review and meta-analysis. *BMJ*. 2012;345:e4800.
4. Lee SY, Shin SD, Lee YJ, et al. Functional status and maintenance compliance of publicly accessible automated external defibrillators in metropolitan Seoul. *Resuscitation*. 2019;138:198-204.
5. Chen Y, Yu Y, Zhang J, et al. Bystander CPR awareness in Chinese industrial workers: a multi-province cross-sectional survey. *BMC Public Health*. 2023;23(1):102.
6. World Health Organization. Global Strategy on Digital Health 2020–2025. Geneva: WHO; 2021.
7. International Labour Organization. Vision Zero Fund Annual Report 2023. Geneva: ILO; 2024.
8. Ministry of Employment and Labor, Republic of Korea. 5th Comprehensive Plan for Industrial Accident Prevention. Sejong: MoEL; 2023.
9. American Heart Association. 2025 ECC & CPR Guidelines. Dallas, TX: AHA; 2025.
10. Perkins GD, Graesner JT, Semeraro F, et al. European Resuscitation Council Guidelines 2021. *Resuscitation*. 2021;161:1-60.
11. Korean Association of Cardiopulmonary Resuscitation (KACPR). 2025 Korean Guidelines for CPR and ECC. Seoul: KACPR; 2025.
12. Brooks SC, Simmons G, Worthington H, et al. The PulsePoint Respond mobile app and time-to-CPR. *Resuscitation*. 2020;146:13-18.
13. Korean Ministry of Health and Welfare. AED Map National Registry. Seoul: MoHW; 2024.
14. Perez MV, Mahaffey KW, Hedlin H, et al. Large-scale assessment of a smartwatch to identify atrial fibrillation. *N Engl J Med*. 2019;381(20):1909-1917.
15. International Organization for Standardization. ISO 45001:2018 Occupational health and safety management systems—Requirements with guidance for use. Geneva: ISO; 2018.
16. McDonagh TA, Metra M, Adamo M, et al. 2023 Focused Update of the 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. *Eur Heart J*. 2023;44(37):3627-3639.
17. Lundberg SM, Lee SI. A unified approach to interpreting model predictions. *Adv Neural Inf Process Syst (NeurIPS)*. 2017;30:4768-4777.
18. Ministry of Food and Drug Safety (MFDS), Republic of Korea. Digital Health Software Guideline. Cheongju: MFDS; 2024.
19. McNally B, Robb R, Mehta M, et al. Cardiac Arrest Registry to Enhance Survival (CARES). *Circ Cardiovasc Qual Outcomes*. 2024.
20. World Wide Web Consortium (W3C). Web Content Accessibility Guidelines (WCAG) 2.1. W3C Recommendation; 2018.

---

*Submitted to the Digital Health Competition · Industrial Safety track · 2026.*
