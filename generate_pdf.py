# -*- coding: utf-8 -*-
"""
CardioGuard Industrial — 韩文PDF 静态生成脚本
====================================================
依赖: fpdf2 (pip install fpdf2)
韩文字体: C:/Windows/Fonts/malgun.ttf (Windows 自带)

运行:
    python generate_pdf.py

产出:
    assets/CardioGuard_Industrial_KR.pdf
====================================================
"""
import os
from pathlib import Path
from fpdf import FPDF

# ---------- 配置 ----------
HERE = Path(__file__).parent
OUT_DIR = HERE / "assets"
OUT_DIR.mkdir(exist_ok=True)
OUT_PATH = OUT_DIR / "CardioGuard_Industrial_KR.pdf"

# Windows 韩文字体
FONT_REGULAR = r"C:\Windows\Fonts\malgun.ttf"
FONT_BOLD = r"C:\Windows\Fonts\malgunbd.ttf"
if not Path(FONT_BOLD).exists():
    FONT_BOLD = FONT_REGULAR  # fallback

# 颜色
C_RED = (220, 38, 38)
C_DARK = (15, 23, 42)
C_GREY = (100, 116, 139)
C_BG = (254, 242, 242)

# ---------- PDF 类 ----------
class CardioPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=15)
        self.add_font("Malgun", "", FONT_REGULAR, uni=True)
        self.add_font("Malgun", "B", FONT_BOLD, uni=True)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Malgun", "", 9)
        self.set_text_color(*C_GREY)
        self.cell(0, 8, "CardioGuard Industrial · 산업 현장 심정지 응급 대응 플랫폼",
                  border=0, align="L")
        self.cell(0, 8, f"{self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*C_RED)
        self.set_line_width(0.4)
        self.line(15, 18, 195, 18)
        self.ln(6)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        self.set_font("Malgun", "", 8)
        self.set_text_color(*C_GREY)
        self.cell(0, 6,
                  "© 2026 Wu Jingrui · 디지털 헬스케어 경진대회 (주제: 산업 안전) 제출작",
                  align="C")

    # 章节大标题
    def h2(self, text):
        self.ln(2)
        self.set_font("Malgun", "B", 14)
        self.set_text_color(*C_RED)
        self.cell(0, 9, text, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(254, 226, 226)
        self.set_line_width(0.3)
        y = self.get_y()
        self.line(15, y, 195, y)
        self.ln(3)
        self.set_text_color(*C_DARK)

    # 子标题
    def h3(self, text):
        self.set_font("Malgun", "B", 11)
        self.set_text_color(*C_DARK)
        self.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")

    # 正文段落
    def p(self, text):
        self.set_font("Malgun", "", 10.5)
        self.set_text_color(*C_DARK)
        self.multi_cell(0, 5.8, text)
        self.ln(1)

    # 项目符号列表
    def bullet(self, text, indent=6):
        self.set_font("Malgun", "", 10.5)
        self.set_text_color(*C_DARK)
        self.set_x(15 + indent)
        # 圆点
        self.set_font("Malgun", "B", 10.5)
        self.set_text_color(*C_RED)
        self.cell(4, 5.8, "•")
        self.set_font("Malgun", "", 10.5)
        self.set_text_color(*C_DARK)
        # multi_cell 在指定 x 上自动换行
        x = self.get_x()
        y = self.get_y()
        self.multi_cell(195 - x, 5.8, text)
        self.ln(0.5)

    # 强调段(关键术语+描述)
    def kv(self, key, val):
        self.set_font("Malgun", "B", 10.5)
        self.set_text_color(*C_DARK)
        self.set_x(21)
        self.cell(4, 5.8, "•", border=0)
        self.write(5.8, key)
        self.set_font("Malgun", "", 10.5)
        self.write(5.8, " " + val)
        self.ln(7)

    # 编号列表
    def num(self, n, text):
        self.set_font("Malgun", "B", 10.5)
        self.set_text_color(*C_RED)
        self.set_x(15)
        self.cell(8, 5.8, f"{n}.", border=0)
        self.set_text_color(*C_DARK)
        self.set_font("Malgun", "", 10.5)
        x = self.get_x()
        self.multi_cell(195 - x, 5.8, text)
        self.ln(0.5)


# ---------- 生成 ----------
def build():
    pdf = CardioPDF()
    pdf.add_page()

    # 封面页
    pdf.ln(20)
    pdf.set_font("Malgun", "B", 11)
    pdf.set_text_color(*C_GREY)
    pdf.cell(0, 6, "디지털 헬스케어 경진대회 · 주제: 산업 안전 (Industrial Safety)",
             align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)

    pdf.set_font("Malgun", "B", 22)
    pdf.set_text_color(*C_RED)
    pdf.cell(0, 12, "CardioGuard Industrial", align="C",
             new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Malgun", "B", 16)
    pdf.set_text_color(*C_DARK)
    pdf.cell(0, 10, "산업 현장 심정지 응급 대응 플랫폼", align="C",
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)

    # 가로 구분선
    pdf.set_draw_color(*C_RED)
    pdf.set_line_width(0.8)
    pdf.line(70, pdf.get_y(), 140, pdf.get_y())
    pdf.ln(8)

    # 摘요
    pdf.set_fill_color(*C_BG)
    pdf.set_font("Malgun", "", 10.5)
    pdf.set_text_color(*C_DARK)
    abstract = (
        "본 플랫폼은 미국심장협회(AHA) 2025 ECC 가이드라인과 한국심폐소생협회"
        "(KACPR) 기준에 기반하여, 산업 현장에서 발생하는 심정지(SCA)에 대한 "
        "\"감지 - 예측 - 대응 - 교육\"의 전 주기적 디지털 솔루션을 제공합니다. "
        "중국어·한국어 이중 언어를 지원하며, 정적 웹 기반으로 어디서나 즉시 "
        "배포·이용이 가능합니다."
    )
    # 左侧红条 + 浅红底色
    y0 = pdf.get_y()
    pdf.set_fill_color(254, 242, 242)
    pdf.rect(15, y0, 180, 28, style="F")
    pdf.set_fill_color(*C_RED)
    pdf.rect(15, y0, 1.5, 28, style="F")
    pdf.set_xy(20, y0 + 3)
    pdf.multi_cell(170, 5.5, abstract)
    pdf.ln(8)

    # 元信息表
    pdf.set_font("Malgun", "B", 10)
    pdf.set_text_color(*C_DARK)
    meta = [
        ("제출자", "Wu Jingrui"),
        ("소속", "시안의학고등전문학교 / Xi'an Medical College · 경운대학교"),
        ("연구 분야", "디지털 헬스, 응급의학, 역학"),
        ("연락처", "253207006@ikw.ac.kr"),
        ("작성일", "2026-06-03"),
    ]
    for k, v in meta:
        pdf.set_x(40)
        pdf.set_font("Malgun", "B", 10)
        pdf.set_text_color(*C_RED)
        pdf.cell(28, 7, k, border=0)
        pdf.set_font("Malgun", "", 10)
        pdf.set_text_color(*C_DARK)
        pdf.cell(0, 7, v, new_x="LMARGIN", new_y="NEXT")

    # ============ 1. 웹사이트 설계 및 개발 방법 ============
    pdf.add_page()
    pdf.h2("1. 웹사이트 설계 및 개발 방법")
    pdf.p(
        "본 플랫폼은 \"사용자 중심 · 데이터 기반 · 표준 연계\"의 세 가지 원칙에 "
        "따라 설계되었으며, 현대 웹 프런트엔드 스택과 경량 아키텍처를 채택하여 "
        "산업 환경에서의 안정성, 저지연, 확장성을 보장한다."
    )
    pdf.ln(2)

    pdf.kv("요구사항 정의:",
           "AHA 2025 ECC 가이드라인과 중·한 양국의 산업 현장 응급의료 공백을 "
           "분석하여, \"4분 골든타임 대응, 이중 언어 접근성, 모바일 우선\" 원칙을 "
           "도출하였다.")
    pdf.kv("기술 아키텍처:",
           "순수 정적 HTML5/CSS3/Vanilla JavaScript를 채택하여 서버 의존도를 제거"
           "하였고, Chart.js로 데이터 시각화를, html2pdf.js로 클라이언트 PDF 출력을 "
           "구현하였다. Netlify·GitHub Pages에 원클릭 배포가 가능하다.")
    pdf.kv("국제화(i18n):",
           "data-i18n 속성 매핑 방식의 경량 i18n 모듈을 자체 구현하여, 전체 UI를 "
           "중국어 ↔ 한국어로 즉시 전환할 수 있도록 하였으며 Noto Sans CJK 폰트로 "
           "모든 디바이스에서 동일한 가독성을 보장한다.")
    pdf.kv("접근성:",
           "WCAG 2.1 AA 기준을 준수하여 시맨틱 HTML, ARIA 레이블, 키보드 내비게이션, "
           "4.5:1 명도 대비를 적용하였다.")
    pdf.kv("보안·프라이버시:",
           "프런트엔드 데이터 무저장, HTTPS 강제, PDF의 로컬 생성(서버 미전송)을 "
           "통해 한국 개인정보보호법 및 GDPR 수준의 모범 사례를 따른다.")
    pdf.kv("검증·배포:",
           "Chrome / Edge / Safari 브라우저 호환성 테스트, Lighthouse 성능 점수 90 "
           "이상, 반응형 디자인을 통한 모바일 최적화, GitHub 오픈소스 공개로 심사의 "
           "재현성을 보장한다.")

    # ============ 2. 웹사이트 주요 기능 소개 ============
    pdf.add_page()
    pdf.h2("2. 웹사이트 주요 기능 소개")
    pdf.p(
        "본 플랫폼은 \"감지 - 예측 - 대응 - 교육 - 데이터\"의 5대 폐쇄 루프를 "
        "중심으로 다음 6개 모듈을 제공한다."
    )
    pdf.ln(2)

    pdf.num(1,
        "실시간 생체신호 모니터링 — 근로자가 착용한 스마트 밴드 / 흉부 패치를 "
        "통해 심박수, 단일 유도 ECG, 혈중 산소포화도, 피부 온도를 실시간 수집하며, "
        "AI 모델이 초 단위로 비정상 리듬을 식별한다.")
    pdf.num(2,
        "AI 위험도 예측 — 근속 연수, 교대 근무, 직종, 생리 지표 등 12개 핵심 "
        "특징을 결합한 그래디언트 부스팅 모델로 향후 24시간 심장 이벤트 위험 "
        "점수를 출력하며, 고·중·저 3단계 위험 등급 관리와 SHAP 기반 설명 가능성을 "
        "제공한다.")
    pdf.num(3,
        "AED 사물인터넷 네트워크 — 산업단지 내 모든 AED 장비를 네트워크에 연결"
        "하여 위치·배터리·유효기간을 시각화하고, 심정지 발생 시 가장 가까운 AED를 "
        "자동으로 안내한다.")
    pdf.num(4,
        "응급 원클릭 대응 — SOS 트리거 시 공장 의무실, 인근 훈련받은 자원봉사자, "
        "119 / 120 응급센터에 동시 알림을 발송하며 AHA 2025 가이드라인 기반의 음성 "
        "안내로 현장 CPR과 AED 사용을 지원한다.")
    pdf.num(5,
        "CPR 교육 관리 — AHA / KACPR 최신 지침에 따른 온라인 강좌·평가·인증 발급을 "
        "디지털화하여 핵심 직무자의 자격 유지를 보장하며, 중국어·한국어 이중 언어 "
        "교육 콘텐츠와 VR 시뮬레이션을 지원한다. 아울러 미국심장협회(AHA)와 "
        "질병관리청(KDCA)의 공식 CPR 시연 영상을 플랫폼에 임베드하여 누구나 바로 "
        "학습할 수 있는 표준 교육 자료로 제공한다.")
    pdf.num(6,
        "안전 데이터 콕핏 — 기업 EHS 부서 및 공공 보건 당국에 산업단지급·기업급·"
        "산업급 심장 안전 데이터를 다층적으로 집계·분석하여 제공하며, 규제 보고서를 "
        "원클릭으로 내보낼 수 있다.")

    # ============ 3. 기대 효과 및 응용 가치 ============
    pdf.add_page()
    pdf.h2("3. 기대 효과 및 응용 가치")
    pdf.p(
        "생명 구조, 기업 효율, 공공 보건, 한·중 산업 협력의 네 가지 측면에서 "
        "본 플랫폼의 핵심 가치를 정량화한다."
    )
    pdf.ln(2)
    pdf.kv("생존율 향상 (+25%p):",
           "\"인지 - CPR - AED\" 사슬의 시간을 단축함으로써 AHA 2025의 목표에 부합"
           "하는 OHCA 퇴원 생존율 25% 이상을 기대할 수 있다.")
    pdf.kv("응답 시간 단축 (-60%):",
           "AED 네트워킹과 자원봉사자 근접 디스패치를 통해 SOS 발생 ~ 현장 CPR "
           "평균 시간을 8분에서 3분 이내로 단축할 것으로 예상한다.")
    pdf.kv("3대 사용자 군 전면 지원:",
           "기업 EHS 관리자, 현장 근로자·자원봉사자, 보건 감독 당국의 3대 핵심 "
           "사용자를 모두 커버하여 사전·사중·사후의 협력 루프를 완성한다.")
    pdf.kv("한·중 산업 협력의 실질적 구현:",
           "이중 언어 네이티브 설계를 통해 산둥성 한국 자본 산업단지, 경기도 내 "
           "중국 진출 기업 등 한·중 국경 간 산업 현장에 직접 적용 가능하며 디지털 "
           "헬스 산업의 상호 연결을 촉진한다.")
    pdf.kv("UN 지속가능발전목표(SDG) 연계:",
           "SDG 3.4(비전염성 질환 조기 사망 감소) 및 SDG 8(양질의 일자리)에 직접 "
           "부응하며 국제적 확장 가치를 가진다.")
    pdf.kv("명확한 기업 투자 회수율:",
           "심정지 1건당 평균 치료 비용은 30 - 50만 위안 수준이며, 본 플랫폼이 1만 "
           "명의 근로자를 커버할 경우 연간 천만 위안 규모의 비용 절감이 가능하여 "
           "ROI > 5가 예상된다.")

    # ============ 4. 기타 관련 설명 ============
    pdf.add_page()
    pdf.h2("4. 기타 관련 설명")

    pdf.h3("연구 개발팀")
    pdf.bullet("연구 책임자: Wu Jingrui, 시안의학고등전문학교 / 경운대학교 보건학 박사과정")
    pdf.bullet("연구 분야: 디지털 헬스, 응급의학, 역학")
    pdf.bullet("협력 기관: 시안의학고등전문학교 · 경운대학교 · 한국심폐소생협회(KACPR)")
    pdf.ln(2)

    pdf.h3("참고 표준 및 가이드라인")
    pdf.bullet("AHA 2025 ECC & CPR Guidelines")
    pdf.bullet("European Resuscitation Council (ERC) 2021")
    pdf.bullet("Korean Association of CPR (KACPR) 2025")
    pdf.bullet("WHO Global Strategy on Digital Health 2020 - 2025")
    pdf.bullet("ISO 45001 Occupational Health & Safety Management")
    pdf.ln(2)

    pdf.h3("데이터 출처")
    pdf.p(
        "본 데모 사이트의 모든 수치는 AHA Heart Disease & Stroke Statistics 2025, "
        "KACPR 연차 보고서, ILO 산업 안전 통계 등 공개 자료를 기반으로 한 시뮬레이션 "
        "예시이며, 실제 생산 데이터를 대표하지 않는다."
    )
    pdf.ln(1)

    pdf.h3("규제 준수")
    pdf.p(
        "프런트엔드 무저장 · HTTPS 강제 · PDF 로컬 생성을 통해 한국 개인정보보호법 "
        "및 GDPR 수준의 보안을 준수한다. 소스 코드는 MIT 라이선스로 공개된다."
    )
    pdf.ln(1)

    pdf.h3("AI 사용 공개")
    pdf.p(
        "본 플랫폼의 개발 과정에서 AI는 코드 및 문안의 다듬기에만 사용되었으며, "
        "어떠한 환자 데이터도 AI에 입력되지 않았다."
    )
    pdf.ln(1)

    pdf.h3("향후 로드맵")
    pdf.bullet("2026 Q3 — 한·중 합자 공장 2곳에서 시범 운영 개시")
    pdf.bullet("2026 Q4 — 500명 전향적 코호트 데이터 수집 완료")
    pdf.bullet("2027 Q1 — 한국 식품의약품안전처(MFDS) 디지털 의료기기 신고")
    pdf.bullet("2027 Q2 — SCI 논문 발표 및 10개 산업단지로 확장 배포")
    pdf.ln(2)

    pdf.h3("연락처")
    pdf.bullet("Wu Jingrui — 시안의학고등전문학교 / Kyungwoon University")
    pdf.bullet("Email: 253207006@ikw.ac.kr")

    pdf.output(str(OUT_PATH))
    return OUT_PATH


if __name__ == "__main__":
    import sys
    path = build()
    size_kb = path.stat().st_size / 1024
    sys.stdout.reconfigure(encoding='utf-8')
    print(f"[OK] Korean PDF generated: {path}")
    print(f"     File size: {size_kb:.1f} KB")
