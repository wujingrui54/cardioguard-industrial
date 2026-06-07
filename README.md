# 工心守护 · CardioGuard Industrial
### 工业场所心脏急救响应平台 · 산업 현장 심정지 응급 대응 플랫폼

> **数字健康医疗竞赛参赛作品**  ·  **주제: 产业安全 / 산업 안전 (Industrial Safety)**

[![Tech](https://img.shields.io/badge/Stack-HTML%2FCSS%2FJS-blue)]() [![Lang](https://img.shields.io/badge/i18n-中文%20%2F%20한국어-red)]() [![PDF](https://img.shields.io/badge/PDF-Korean%20Export-orange)]() [![License](https://img.shields.io/badge/License-MIT-green)]()

> 🌐 **在线访问 / 라이브 데모 / Live demo:** <https://wujingrui54.github.io/cardioguard-industrial/>

---

## 📌 项目简介 / 프로젝트 개요

**中文：** 本平台是一个面向工业园区与厂矿场所的"心脏急救智能响应"演示网站，融合 AHA 2025 ECC 指南、AI 风险预测、AED 物联网络与 CPR 数字培训，构建"监测 - 预警 - 响应 - 培训 - 数据"全链路解决方案。

**한국어:** 본 플랫폼은 산업단지와 공장을 위한 "심정지 스마트 응급 대응" 데모 사이트로, AHA 2025 ECC 가이드라인, AI 위험도 예측, AED IoT 네트워크, CPR 디지털 교육을 통합하여 "감지-예측-대응-교육-데이터"의 전 주기 솔루션을 구축합니다.

---

## 🌐 提交物 / 제출물 (Deliverables)

| # | 项目 | 文件 / URL |
|---|---|---|
| 1 | **网站 URL** | 🌐 <https://wujingrui54.github.io/cardioguard-industrial/> |
| 2 | **源代码** | 本仓库（index.html · css/ · js/ · assets/） |
| 3 | **论文** | [`PAPER_ZH.md`](PAPER_ZH.md) · [`PAPER_KR.md`](PAPER_KR.md) |
| 4 | **韩文 PDF** | 站点右上角 **"한국어 PDF 다운로드"** 按钮一键导出 |

---

## ✨ 核心特性 / 핵심 기능

- 🌏 **中韩双语一键切换** — 右上角 `中文 / 한국어` 切换按钮
- 📥 **韩文 PDF 一键导出** — 右上角下载按钮，客户端 html2pdf.js 生成
  - PDF 包含必备 4 章：
    1. 웹사이트 설계 및 개발 방법 (网站设计与开发方法)
    2. 웹사이트 주요 기능 소개 (网站主要功能介绍)
    3. 기대 효과 및 응용 가치 (预期效果与应用价值)
    4. 기타 관련 설명 (其他相关说明)
- 📊 **数据可视化仪表盘** — 4 张 Chart.js 图表
  1. 工业场所心脏骤停月度发生率（线图）
  2. 急救响应时间分布（柱图）
  3. AED 4 分钟可达覆盖率（环形对比图）
  4. 心脏事件风险因素 SHAP 权重（横向柱图）
- ⚡ **零后端依赖** — 纯静态 HTML / CSS / JS，本地双击 `index.html` 即可运行
- 🛡 **隐私优先** — 前端零数据留存，PDF 本地生成不上传

---

## 🏗 技术栈 / 기술 스택

```
Frontend    : HTML5 · CSS3 (Custom Properties · Grid · Flexbox) · Vanilla JavaScript (ES6+)
Chart       : Chart.js 4.4 (CDN)
PDF Export  : html2pdf.js 0.10.1 (CDN)
Typography  : Google Fonts · Noto Sans SC / Noto Sans KR / Inter
i18n        : Custom data-i18n attribute mapping (~430 keys)
A11y        : Semantic HTML · ARIA labels · keyboard nav · WCAG 2.1 AA contrast
Deploy      : GitHub Pages / Netlify / Vercel · zero-config static
```

---

## 📁 目录结构 / 디렉터리 구조

```
数字健康竞赛_工业心脏急救平台/
├── index.html              # 主页面 (含中韩双语 + 韩文 PDF 源)
├── css/
│   └── style.css           # 全部样式
├── js/
│   ├── i18n.js             # 中韩双语字典 (~430 keys)
│   ├── main.js             # 语言切换 + PDF 导出 + 交互
│   └── charts.js           # Chart.js 4 张仪表盘
├── assets/                 # （预留）图片资源
├── PAPER_ZH.md             # 中文论文
├── PAPER_KR.md             # 韩文论文
├── LICENSE                 # MIT License
└── README.md
```

---

## 🚀 快速开始 / 빠른 시작

### 方式 1：本地双击运行
直接双击 `index.html` 即可在浏览器中打开。

### 方式 2：本地 HTTP 服务器（推荐，便于 CDN 字体加载）
```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve .
```
然后访问 [http://localhost:8000](http://localhost:8000)

### 方式 3：一键部署到云端

**GitHub Pages:**
```bash
git init && git add . && git commit -m "Initial commit"
git remote add origin https://github.com/wujingrui54/cardioguard-industrial.git
git push -u origin main
# Settings → Pages → Source: main / root
```

**Netlify（拖拽即可）：** 将整个文件夹拖到 [app.netlify.com](https://app.netlify.com/drop)

**Vercel CLI:**
```bash
npx vercel --prod
```

---

## 📷 截图说明 / 스크린샷 안내

| 区域 | 说明 |
|---|---|
| **顶部导航栏** | 品牌 Logo + 6 个章节锚点 + 中韩切换 + 一键下载 PDF |
| **Hero 主视觉** | 渐变标题 + 4 项核心数据指标 + 心跳脉冲动画 |
| **章节 01 开发方法** | 6 张方法卡 + 技术栈徽章 |
| **章节 02 核心功能** | 6 大功能模块（监测/AI预测/AED网/急救响应/培训/驾驶舱）|
| **章节 03 急救演示** | AHA + KDCA 官方 CPR 教学视频 2 则（YouTube 官方嵌入）|
| **章节 04 数据仪表盘** | 4 张交互图表 |
| **章节 05 应用价值** | 6 张量化效果卡（+25% 生存率、-60% 响应时间、ROI > 5 等）|
| **章节 06 其他说明** | 团队/标准/数据/合规/联系/路线图 |

---

## 🧪 浏览器兼容性 / 호환성

| Browser | Version | Status |
|---------|---------|--------|
| Chrome / Edge | ≥ 90 | ✅ Fully supported |
| Firefox | ≥ 88 | ✅ Fully supported |
| Safari | ≥ 14 | ✅ Fully supported |
| Mobile Safari / Chrome | iOS 14+ / Android 10+ | ✅ Responsive |

---

## 📑 许可 / 라이선스

MIT License — 详见 [`LICENSE`](LICENSE)。

数据来源（演示数据）：基于 AHA Heart Disease & Stroke Statistics 2025、KACPR 年报、ILO 职业安全统计公开数据的**模拟示例**，不代表真实生产数据。

---

## 👤 作者 / 작성자

**Wu Jingrui (吴静蕊)**
- 西安医学高等专科学校 / Kyungwoon University (PhD candidate, Public Health)
- 시안의학고등전문학교 / 경운대학교 보건학 박사과정
- ✉️ 253207006@ikw.ac.kr

---

## 🤖 AI 使用披露 / AI 사용 공개

本项目代码与文案在开发过程中借助生成式 AI 进行了语法润色与样式样板生成。
所有医学指南引用、应用价值数据、技术架构决策均由作者审定。
**没有任何患者或受试者数据被输入到 AI 中。**

본 프로젝트의 코드와 문안은 개발 과정에서 생성형 AI를 통해 문법 다듬기와 스타일 보일러플레이트 생성을 보조받았습니다.
모든 의학 가이드라인 인용, 응용 가치 데이터, 기술 아키텍처 결정은 저자가 직접 검토·확정하였습니다.
**환자 또는 피험자의 데이터는 일체 AI에 입력되지 않았습니다.**
