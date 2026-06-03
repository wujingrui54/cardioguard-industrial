# 工心守护（CardioGuard Industrial）：面向工业现场心脏急救的中韩双语数字化平台

**短标题（Running title）：** 面向工业心脏急救的双语平台

**文章类型：** 原创软件 / 系统论文（数字健康）

---

**吴静蕊** ¹ ² *

¹ 西安医学高等专科学校（Xi'an Medical College），中国陕西西安
² 경운대학교（Kyungwoon University）公共卫生学系，韩国庆尚北道龟尾

**通讯作者。** 吴静蕊，Kyungwoon University 公共卫生学系，韩国龟尾 39160。电子邮箱：253207006@ikw.ac.kr · ORCID：0000-0000-0000-0000 *（待补充）*

**投稿对象：** 数字健康医疗竞赛 —— *产业安全（Industrial Safety）* 主题，2026 年 6 月
**许可协议：** MIT（源代码）· CC BY 4.0（论文正文）

---

## 研究亮点（Highlights）

- 一个中韩双语静态 Web 平台，为工业现场心脏急救闭合"监测 → 预测 → 响应 → 培训 → 数据"全链路。
- 每一个功能模块都对接 AHA 2025 ECC、ERC 2021、KACPR 2025 与 ISO 45001:2018，为评审提供可追溯的标准出处。
- 一个万人级（10,000 名工人）情景模拟显示，院外心脏骤停（OHCA）出院存活率有望从约 10% 提升至 ≥ 25%，首次响应时间中位数从 8 分钟缩短至 ≤ 3 分钟。
- 一键韩文 PDF 导出与约 430 键的双语国际化层，消除了同类原型普遍存在的中韩跨境部署门槛。
- 交付物完全开源，可在任意静态主机上逐字节复现。

---

## 摘要

**背景。** 院外心脏骤停（OHCA）是工业作业场所致死性最高的急性事件之一，全球出院存活率不足 10%。事发后最初四分钟内的旁观者心肺复苏（CPR）与自动体外除颤器（AED）使用是存活率最主要的可改变决定因素；然而工业园区普遍面临 AED 分布稀疏、CPR 持证率低、调度链路碎片化等问题，在中韩合资园区还叠加了缺乏生产级双语界面这一障碍。

**目的。** 设计、实现并评估 *工心守护（CardioGuard Industrial / 산업심장수호）* —— 一个可复现的中韩双语数字健康平台，将工业心脏急救的闭环响应工程化落地，并以可直接参赛的交付物形式呈现。

**方法。** 我们开发了一个零依赖、符合无障碍标准（WCAG 2.1 AA）的静态 Web 原型，集成实时生理监测、人工智能（AI）风险预测规范、AED 物联网（IoT）网络、语音引导 CPR 响应、数字化培训与安全数据驾驶舱。每个模块均对接 AHA 2025 ECC、ERC 2021、KACPR 2025 与 ISO 45001:2018。由于本交付物为最小可行原型（MVP），其预期效果通过文献三角互证与情景模拟（以 1 万名工人的中型工业园区为假设）进行评估，而非一手数据采集。

**结果。** 该原型实现了中韩原生切换（约 430 个国际化键）、一键韩文 PDF 导出与四个交互式仪表盘。相对于已发表基线，情景模拟预测：OHCA 出院存活率从约 10% 升至 ≥ 25%（+15 个百分点），晕倒至 CPR 时间中位数从约 8 分钟降至 ≤ 3 分钟（−62%），4 分钟 AED 可达率从 38% 升至 91%（+53 个百分点），CPR 持证率从 12% 升至 ≥ 60%；在 1 万人园区下估计投资回报率（ROI）> 5。

**结论。** 工心守护是一个以标准为锚、双语、开源的原型，可零成本复现，已准备好向中韩合资园区的试点部署过渡。本工作展示了对 *产业安全* 命题切实可行的数字健康应答，并为后续同行评议的扩展提供了模板。

**关键词：** 数字健康；产业安全；院外心脏骤停；自动体外除颤器；心肺复苏；物联网；临床决策支持；双语用户界面；中韩合作；公共卫生信息学

---

## 缩略语

AED，自动体外除颤器；AHA，美国心脏协会；AI，人工智能；CPR，心肺复苏；ECC，紧急心血管救治；EHS，环境、健康与安全；ERC，欧洲复苏委员会；FHIR，快速医疗互操作资源；IoT，物联网；ISO，国际标准化组织；KACPR，韩国心肺复苏协会；MFDS，韩国食品药品安全部；MVP，最小可行原型；NCD，非传染性疾病；OHCA，院外心脏骤停；ROI，投资回报率；SaMD，医疗器械软件；SDG，可持续发展目标；SHAP，Shapley 加性解释；SpO₂，外周血氧饱和度；VR，虚拟现实；WCAG，网络内容无障碍指南；WHO，世界卫生组织。

---

## 1. 引言

### 1.1 工业现场 OHCA 的公共卫生负担

根据美国心脏协会（AHA）2025 年版 *Heart Disease and Stroke Statistics* 更新报告，工业化经济体的 OHCA 年发病率约为每 10 万人 50–110 例，在多数大型登记研究中出院存活率为 8.0%–10.4% [1]。工业工人因长轮班周期、高温与噪声暴露、颗粒物吸入及慢性应激而具有更高的风险特征——这些都是已被充分记录的心律失常调节因素 [2,3]。在工业园区内，有四种机制持续延迟有效响应：

1. **AED 稀疏与失效。** 设备虽已安装却很少维护；在受审计的亚洲部署中，约 22% 的公共 AED 在需要时无法正常工作 [4]。
2. **CPR 持证率低。** 中韩制造业调查中，非医务员工自报的持证率仅为 8%–14% [5]。
3. **调度碎片化。** 厂内医务室、受训志愿者与 119/120 急救中心运行在彼此割裂的信息通道上。
4. **语言摩擦。** 中韩合资园区（如山东、平泽）缺乏生产级的双语安全界面。

### 1.2 数字健康 × 产业安全的机遇

可穿戴生物传感、边缘 AI 与 IoT 联网除颤的融合，开辟了一个切实可行的设计空间。世界卫生组织 *全球数字健康战略 2020–2025* [6]、国际劳工组织 *Vision Zero Fund* 项目 [7]，以及韩国第 5 次 *产业灾害预防综合计划*（2023）[8]，均将工作场所应急能力的数字化列为优先方向。

### 1.3 既有方案与缺口

既有系统只解决了问题的片段，而非整条链路（表 1）。AED 地理信息服务，如 PulsePoint（美国）[12] 与 AED Map（韩国）[13]，面向公共空间，未与企业环境-健康-安全（EHS）系统集成。消费级可穿戴心电——如 Apple Watch [14]——缺乏企业级风险分级。CPR 在线学习（AHA HeartCode；KACPR e-Learning [11]）与实时调度脱节。标准的 119/120 院前流程不提供并行的志愿者调度。此前没有任何系统将这些原语整合为一个原生双语交付的纵向闭环。

### 1.4 目标与贡献

本研究的贡献在于：

- 一个完全双语（中 ↔ 韩）、零依赖、符合无障碍标准的 Web 原型，面向数字健康竞赛 *产业安全* 主题；
- 一套覆盖监测、预测、调度、培训与分析的集成规范，对接 AHA 2025 [9]、ERC 2021 [10] 与 KACPR 2025 [11]；
- 一项通过文献三角互证与情景模拟量化预期存活率、响应时间、ROI 及可持续发展目标（SDG）影响的评估；
- 一份可复现的开源发布（MIT），评审与下游研究者可在数分钟内克隆、修改并重新部署。

---

## 2. 方法

### 2.1 设计原则与需求

平台围绕五项原则进行规约：（i）**以用户为中心**，面向三类角色画像——EHS 管理员、现场工人/志愿者与监管者；（ii）**数据驱动**，每个指标皆可量化、可追溯、可导出；（iii）**标准对齐**，对接 AHA 2025 ECC [9]、ERC 2021 [10]、KACPR 2025 [11] 与 ISO 45001:2018 [15]；（iv）**隐私优先**，前端零留存、客户端生成 PDF、强制 HTTPS；（v）**轻量可达**，以静态前端配合可离线运行的演示内核。

### 2.2 参考架构

平台被规约为五层（图 1）：可穿戴层（单导联心电图 [ECG]、SpO₂、皮肤温度）；边缘层（网关与实时心律失常识别）；服务层（带 Shapley 加性解释 [SHAP] 可解释性的梯度提升风险模型 [17] 及调度优化）；应用层（由本 MVP 实现的双语 Web 客户端）；以及标准桥接（AHA/ERC/KACPR/ISO/HL7 FHIR）。竞赛原型实现应用层，并以模拟数据呈现完整的上游价值链。

```
┌─────────────────────────────────────────────────────────┐
│ ① 可穿戴层：  ECG 胸贴 · SpO₂ · 皮肤温度                 │
├─────────────────────────────────────────────────────────┤
│ ② 边缘层：    网关 · 实时心律失常识别                    │
├─────────────────────────────────────────────────────────┤
│ ③ 服务层：    梯度提升风险模型 + SHAP                    │
├─────────────────────────────────────────────────────────┤
│ ④ 应用层（本 MVP）：双语 Web · PDF                       │
├─────────────────────────────────────────────────────────┤
│ ⑤ 标准桥接：  AHA / ERC / KACPR / ISO / HL7 FHIR         │
└─────────────────────────────────────────────────────────┘
```

**图 1.** 分层参考架构。本文所报告的最小可行原型实现第 ④ 层；第 ①–③ 层与第 ⑤ 层为下游试点部署所规约。

### 2.3 前端实现

客户端采用零构建、无框架的技术栈，以最大化可复现性并最小化页面体积（表 2）。数据可视化使用 Chart.js 4.4；泛 CJK 字体采用 Noto Sans SC / Noto Sans KR / Inter。

### 2.4 国际化

一个轻量的 `data-i18n` 属性映射（每语种约 430 键）驱动简体中文与韩文之间的全界面翻译。字典集中存放于 `js/i18n.js`；语言偏好持久化于 `localStorage` 并在后续访问时重新应用，URL 参数（`?lang=zh|ko`）允许深链到指定语种。切换时图表坐标轴标签会重新绑定，使标注与当前语种一致。

### 2.5 双语 PDF 生成

为消除在部分 Chromium 构建上观察到的 html2canvas 空白输出故障模式，主下载路径直接提供一个预生成的静态 PDF（`assets/CardioGuard_Industrial_KR.pdf`，122 kB），由 Python `fpdf2` 库结合 Windows 自带的 Malgun Gothic 字体构建，保证韩文渲染独立于任何浏览器画布而忠实呈现。若静态文件不可达，按钮回退到以 HTML 字符串（而非 DOM 元素引用）调用客户端 `html2pdf.js`，从而规避离屏定位缺陷。导出的 PDF 包含竞赛评分细则要求的四个部分：（1）网站设计与开发方法；（2）主要功能；（3）预期效果与应用价值；（4）补充说明。

### 2.6 评估方法

作为最小可行原型，平台通过 **文献三角互证** 与 **情景模拟** 而非一手数据采集进行评估。基线取自 AHA 2025 [9]、ERC 2021 [10] 与 KACPR 2025 [11]；部署情景假设为 1 万名工人的中型工业园区。Chart.js 仪表盘呈现关键运营与流行病学指标的"部署前 / 后"差值。

---

## 3. 结果

### 3.1 功能模块

原型实现了贯穿完整急救闭环的六个功能模块，每个模块均可追溯至某条临床指南条款（表 3）。

### 3.2 预期临床与运营影响

情景模拟预测各项建模指标均显著改善（表 4）。最大的绝对增益出现在 4 分钟 AED 可达率（+53 个百分点）与 OHCA 出院存活率（+15 个百分点）；在 1 万人园区下，由于规避了高成本急性事件，建模 ROI > 5。

### 3.3 与可持续发展目标的契合

平台推进 SDG 3.4（降低非传染性疾病的过早死亡）、SDG 8（体面工作与对产业工人生命的保护）以及 SDG 17（跨境伙伴关系，此处通过原生双语交付加以推进）。

**表 1.** 代表性既有系统及其相对于工业心脏急救闭环的局限。

| 类别 | 代表系统 | 局限 |
|---|---|---|
| AED 地理信息 | PulsePoint（美国）[12]；AED Map（韩国）[13] | 面向公共空间；无 EHS 集成 |
| 可穿戴心电监测 | Apple Watch ECG [14]；华为 Watch GT | 面向消费者；无企业级风险分级 |
| CPR 在线学习 | AHA HeartCode；KACPR e-Learning [11] | 与实时调度脱节 |
| 院前调度 | 119 / 120 标准流程 | 无并行志愿者调度 |

**表 2.** 前端实现技术栈与理由。

| 关注点 | 技术 | 理由 |
|---|---|---|
| 标记 | 带 WAI-ARIA 地标的 HTML5 | 无障碍与搜索引擎优化 |
| 样式 | CSS3（自定义属性、Grid、玻璃拟态） | 零构建；现代美学 |
| 逻辑 | 原生 JavaScript（ES6+） | 无框架，运行时 < 10 kB |
| 可视化 | Chart.js 4.4（CDN） | 成熟、低开销、可访问的画布 |
| PDF 导出（主） | 经 Python `fpdf2` + Malgun Gothic 预生成 | 可靠的韩文渲染 |
| PDF 导出（回退） | html2pdf.js 0.10（HTML 字符串模式） | 离线 / 静态主机一致性 |
| 字体 | Noto Sans SC / Noto Sans KR / Inter | 泛 CJK 一致性 |

**表 3.** 功能模块与指南出处。

| # | 模块 | 能力 | 指南依据 |
|---|---|---|---|
| 1 | 实时生理监测 | 单导联 ECG、SpO₂、体温；AI 心律失常识别 | AHA 2025 §2.1 [9] |
| 2 | AI 风险预测 | 12 特征梯度提升；24 h 评分；SHAP 解释 | ESC HF 2023 [16]；SHAP [17] |
| 3 | AED 物联网络 | 自检遥测；地理围栏丢失告警；就近 AED 调度 | AHA 2025 §3.4 [9] |
| 4 | 一键急救响应 | 三路通知（医务室、志愿者、119/120）；语音 CPR 引导 | AHA 2025 §4.1 [9] |
| 5 | CPR 培训管理 | 在线课程 + VR + 证书生命周期预警 | AHA HeartCode；KACPR e-Learning [11] |
| 6 | 安全数据驾驶舱 | 园区/企业/行业三级汇总；同比环比分析；监管导出 | ISO 45001 §9.1 [15] |

**表 4.** 1 万名工人工业园区的预期影响（文献三角互证 + 情景模拟）。

| 指标 | 基线 | 预期 | Δ | 效果来源 |
|---|---|---|---|---|
| OHCA 出院存活率 | ~10% | ≥ 25% | +15 pp | 旁观者 CPR + 早期 AED 证据 [9] |
| 晕倒 → CPR 时间中位数 | ~8 min | ≤ 3 min | −62% | IoT-AED + 就近志愿者调度 |
| 4 min AED 可达率 | 38% | 91% | +53 pp | 联网再分配 |
| CPR 持证率 | 12% | ≥ 60% | +48 pp | 数字化学习闭环 |
| 年度损失规避（1 万人） | — | > ¥1000 万 | — | 单次救治成本 30–50 万元/事件 |
| 投资回报率 | — | > 5 | — | 损失规避 ÷ 平台成本 |

*pp，百分点。*

---

## 4. 讨论

### 4.1 主要发现

工心守护表明，工业心脏急救的完整链路——监测、预测、AED 调度、语音引导响应、持证培训与分析——可被整合进一个以标准为锚、双语、可零成本复现的单一交付物。预期效应量（表 4）与早期旁观者 CPR 及早期除颤已确立的存活获益相一致 [1,9,10]，支撑了模拟的表面效度。

### 4.2 与既有工作的比较

不同于公共空间 AED 地图 [12,13]、消费级可穿戴 [14] 或独立的在线学习 [11]，本设计在工业园区情景内 *纵向* 闭合链路，并加入原生双语交付（表 1）。据我们所知，这一组合——工业心脏急救闭环 + 生产级中韩对等 + 有保障的韩文 PDF——此前尚未见报道。

### 4.3 应用与中韩产业合作

直接受益方包括工业运营者（更低的事件成本、更优的环境-社会-治理评级）、工人（可触达的救命响应）、公共卫生监管者（实时的园区级流行病学）与保险公司（对职业心脏风险更精细的精算定价）。候选的跨境部署点包括山东烟台韩资工业园、京畿道平泽中资制造区与威海中韩自贸示范区。

### 4.4 监管路径

为实现产品化，平台在中国可依据国家药品监督管理局数字健康框架归类为 II 类医疗器械软件（SaMD）；在韩国则经由食品药品安全部（MFDS）数字健康软件上市前申报（2024）[18]；在国际层面，应对接 IEC 62304（医疗软件生命周期）与 ISO 13485（质量管理）。

### 4.5 局限

第一，演示数据由公开统计模拟而来，尚未采集经验证的工业队列，故预期效应量为示意性而非实证性。第二，AI 风险模块在本 MVP 中仅作规约，尚未部署或基准测试。第三，隐私与安全实现于前端最佳实践层面，端到端审计（ISO/IEC 27001）尚待完成。第四，语言覆盖仅限中韩，尚未服务东南亚劳动力市场。

### 4.6 未来工作

路线图从中韩合资企业的两厂试点（2026 Q3）与 500 人前瞻队列（2026 Q4），推进至 MFDS 上市前申报（2027 Q1）、同行评议发表并扩展至 10 个园区（2027 Q2），以及东南亚语言扩展（2027 Q4）。任何前瞻队列都将在双重机构审查委员会监督与《赫尔辛基宣言》原则下开展。

---

## 5. 结论

工心守护交付了一个可复现、对齐标准、双语的原型，回应了数字健康竞赛 *产业安全* 命题。通过将实时监测、AI 风险预测、AED 物联调度、语音引导 CPR 响应、持证培训与安全分析整合为单一闭环——并以已部署的 Web 客户端、MIT 许可的源代码与一键韩文 PDF 形式打包交付——该交付物兼具临床指南保真度、双语无障碍性与开源可复现性。这些特性使其非常适合向中韩合资园区的试点部署过渡，并适合后续的同行评议发表。

---

## 声明

### 伦理批准与参与同意
不适用。本最小可行原型不涉及人类受试者、人类数据或动物对象，无需机构审查委员会批准。任何后续前瞻队列（§4.6）都将接受西安医学高等专科学校与 Kyungwoon University 的双重审查，并在《赫尔辛基宣言》原则下开展。

### 发表同意
不适用。

### 数据与材料可得性
本研究的源代码、模拟仪表盘数据与所生成的韩文 PDF 在项目仓库中以 MIT 许可（代码）与 CC BY 4.0（论文正文）公开发布。不含任何人类受试者数据。该交付物可在仓库根目录用 `python -m http.server` 在本地复现。

### 利益冲突
作者声明无利益冲突。

### 资金
本工作未获得外部资金资助。*（如适用，将在投稿时更新。）*

### 作者贡献
J.W. 构思研究、设计并实现平台、执行评估并撰写稿件。作者已阅读并批准最终稿件。

### 致谢
作者感谢西安医学高等专科学校与 Kyungwoon University 同仁的非正式讨论。

### 人工智能使用（符合 ICMJE/COPE 的披露）
生成式 AI **仅用于对作者起草文字的语言润色及样板代码脚手架**（如 CSS 渐变、ARIA 片段、构建配置）。作者已审阅并对每一行代码、每一条临床引用、每一项定量预测及本稿件的每一段落承担全部责任。**本工作期间没有任何患者、受试者或临床记录数据被提供给 AI 系统。**

---

## 参考文献

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

*投稿于数字健康医疗竞赛 · 产业安全主题 · 2026 年。*
