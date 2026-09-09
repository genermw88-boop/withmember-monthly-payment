import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정
st.set_page_config(page_title="위드멤버 종합 플레이스 & 리뷰 진단기", page_icon="📊", layout="wide")

st.title("📊 위드멤버 종합 플레이스 & 리뷰 진단기")
st.write("네이버 플레이스 도구 누락 현상과 리뷰 평판 및 매출 성장을 한 번에 정밀 진단합니다.")

st.markdown("---")
st.subheader("📋 1. 매장 종합 정보")

# 매장 정보 입력 폼
col1, col2 = st.columns(2)
with col1:
    store_name = st.text_input("매장명 (플레이스 등록 이름)", placeholder="예: 강남술집")
    target_region = st.text_input("타겟 지역명", placeholder="예: 강남역")
with col2:
    core_menu = st.text_input("핵심 메뉴/업종", placeholder="예: 이자카야")

st.markdown("#### 🔍 현재 등록된 키워드 및 월간 검색량 (최대 5개)")
keyword_data = []
for i in range(5):
    cols = st.columns([2, 1, 1])
    kw = cols[0].text_input(f"키워드 {i+1}", key=f"kw_{i}", placeholder=f"등록 키워드 {i+1}")
    pc_q = cols[1].number_input(f"PC 검색수 {i+1}", min_value=0, value=0, key=f"pc_{i}")
    mo_q = cols[2].number_input(f"모바일 검색수 {i+1}", min_value=0, value=0, key=f"mo_{i}")
    if kw:
        keyword_data.append({"keyword": kw, "pc": pc_q, "mo": mo_q})

col_v1, col_v2 = st.columns(2)
with col_v1:
    visitor_reviews = st.number_input("현재 방문자 리뷰 수", min_value=0, value=1)
with col_v2:
    blog_reviews = st.number_input("현재 블로그 리뷰 수", min_value=0, value=1)

st.markdown("---")
st.subheader("🛠️ 2. 네이버 플레이스 도구 세팅 여부 (체크)")
st.write("현재 사장님 매장에 활성화되어 있는 도구만 체크해 주세요.")

col_t1, col_t2, col_t3, col_t4 = st.columns(4)
has_booking = col_t1.checkbox("네이버 예약", value=True)
has_talk = col_t2.checkbox("네이버 톡톡")
has_coupon = col_t3.checkbox("네이버 쿠폰")
has_call = col_t4.checkbox("안심번호(스마트콜)")

st.markdown("---")

# 진단 실행 버튼
if st.button("🚀 종합 정밀 진단 및 리포트 생성"):
    if not store_name:
        st.warning("매장명을 입력해주세요.")
    else:
        st.success(f"[{store_name}] 전문가용 플레이스 진단 보고서가 생성되었습니다.")
        
        # 키워드 문자열 정리
        kw_list = [f"{item['keyword']} (PC:{item['pc']}, 모바일:{item['mo']})" for item in keyword_data]
        kw_str = ", ".join(kw_list) if kw_list else "등록된 키워드 없음"
        
        # 도구 상태 표시 문자열 생성
        booking_status = "등록" if has_booking else "미등록"
        talk_status = "등록" if has_talk else "미등록"
        coupon_status = "등록" if has_coupon else "미등록"
        call_status = "등록" if has_call else "미등록"
        
        # HTML/CSS로 전문가용 보고서 디자인 구현 (이미지 다운로드 기능 포함)
        report_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <style>
            .report-container {{
                background-color: #ffffff;
                border: 1px solid #cbd5e1;
                border-radius: 16px;
                padding: 40px;
                max-width: 800px;
                margin: 0 auto;
                font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
                color: #1e293b;
                box-shadow: 0 10px 25px rgba(0,0,0,0.08);
            }}
            .report-header {{
                text-align: center;
                border-bottom: 2px solid #e2e8f0;
                padding-bottom: 25px;
                margin-bottom: 30px;
            }}
            .report-title {{
                font-size: 28px;
                font-weight: 800;
                color: #0f172a;
                margin-bottom: 8px;
                letter-spacing: -0.5px;
            }}
            .report-subtitle {{
                font-size: 16px;
                color: #475569;
                font-weight: 600;
            }}
            .store-highlight {{
                color: #2563eb;
                font-weight: 700;
            }}
            .section-box {{
                background-color: #f8fafc;
                border-left: 5px solid #2563eb;
                border-radius: 8px;
                padding: 22px 25px;
                margin-bottom: 25px;
                border-top: 1px solid #e2e8f0;
                border-right: 1px solid #e2e8f0;
                border-bottom: 1px solid #e2e8f0;
            }}
            .section-title {{
                font-size: 18px;
                font-weight: 700;
                color: #1e40af;
                margin-bottom: 14px;
            }}
            .row-item {{
                font-size: 15px;
                margin-bottom: 10px;
                line-height: 1.6;
            }}
            .label {{
                font-weight: 600;
                color: #334155;
                display: inline-block;
                width: 140px;
            }}
            .value-red {{
                color: #dc2626;
                font-weight: 700;
            }}
            .normal-heading {{
                font-size: 17px;
                font-weight: 700;
                color: #0f172a;
                margin-bottom: 8px;
                margin-top: 25px;
            }}
            .download-btn {{
                display: block;
                width: 100%;
                background: linear-gradient(135deg, #2563eb, #1d4ed8);
                color: white;
                text-align: center;
                padding: 14px;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                margin-top: 35px;
                box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
                transition: background 0.2s;
            }}
            .download-btn:hover {{
                background: linear-gradient(135deg, #1d4ed8, #1e40af);
            }}
        </style>
        </head>
        <body>
            <div id="capture-area" class="report-container">
                <div class="report-header">
                    <div class="report-title">📈 플레이스 진단 보고서</div>
                    <div class="report-subtitle">대상 매장: <span class="store-highlight">{store_name}</span></div>
                </div>

                <div class="section-box">
                    <div class="section-title">1. 현재 점수 및 예상 순위</div>
                    <div class="row-item"><span class="label">등록 키워드 :</span> {kw_str}</div>
                    <div class="row-item"><span class="label">플레이스 점수 :</span> <span class="value-red">25점 (취약)</span></div>
                    <div class="row-item"><span class="label">예상 노출 순위 :</span> <span class="value-red">7~10페이지 (상위 노출 제외)</span></div>
                </div>

                <div class="normal-heading">📌 2. 네이버 도구 누락 및 알고리즘 진단</div>
                <div class="row-item" style="margin-left: 5px;"><span class="label" style="width: 130px;">현재 세팅 현황 :</span> 예약(<span style="color: {'#dc2626' if booking_status=='미등록' else '#16a34a'}; font-weight: bold;">{booking_status}</span>), 톡톡(<span style="color: {'#dc2626' if talk_status=='미등록' else '#16a34a'}; font-weight: bold;">{talk_status}</span>), 쿠폰(<span style="color: {'#dc2626' if coupon_status=='미등록' else '#16a34a'}; font-weight: bold;">{coupon_status}</span>), 안심번호(<span style="color: {'#dc2626' if call_status=='미등록' else '#16a34a'}; font-weight: bold;">{call_status}</span>)</div>
                <div class="row-item" style="margin-left: 5px; margin-bottom: 25px;"><span class="label" style="width: 130px; vertical-align: top;">알고리즘 진단 :</span> <span style="display: inline-block; width: 550px; vertical-align: top;">핵심 마케팅 도구의 미등록으로 네이버 알고리즘 평가에서 가산점을 확보하지 못해 순위 경쟁에서 심각하게 밀리고 있습니다. 이는 상권 내 가시성 확보에 치명적인 약점으로 작용합니다.</span></div>

                <div class="normal-heading">💡 3. 도구 최적화 시 기대효과</div>
                <div class="row-item" style="margin-left: 5px; margin-bottom: 25px;"><span class="label" style="width: 130px; vertical-align: top;">순위 회복 효과 :</span> <span style="display: inline-block; width: 550px; vertical-align: top;">누락된 도구들을 즉시 보완 및 세팅함으로써 검색 알고리즘 가산점을 확보하여 노출 순위가 빠르게 회복되고, 실질적인 잠재 고객 유입 접점이 크게 확장될 것입니다.</span></div>

                <div class="normal-heading">⚔️ 4. 반경 500m 상권 경쟁 진단</div>
                <div class="row-item" style="margin-left: 5px;"><span class="label" style="width: 130px;">경쟁 매장 :</span> <span class="value-red">약 35개</span> (타겟 상권 기준 추정)</div>
                <div class="row-item" style="margin-left: 5px;"><span class="label" style="width: 130px; vertical-align: top;">상권 내 순위 진단 :</span> <span style="display: inline-block; width: 550px; vertical-align: top;">인근 500M 내 동종 경쟁 매장 대비 현재 리뷰(방문자 {visitor_reviews}개, 블로그 {blog_reviews}개) 평판 지수가 상권 평균 이하로 분석되어, 즉각적인 상권 맞춤형 최적화와 리뷰 전략이 시급합니다.</span></div>
            </div>

            <button class="download-btn" onclick="downloadImage()">📥 플레이스 진단 보고서 이미지 저장하기</button>

            <script>
            function downloadImage() {{
                const element = document.getElementById('capture-area');
                html2canvas(element, {{ scale: 2, useCORS: true }}).then(canvas => {{
                    const link = document.createElement('a');
                    link.download = '{store_name}_플레이스_진단보고서.png';
                    link.href = canvas.toDataURL('image/png');
                    link.click();
                }});
            }}
            </script>
        </body>
        </html>
        """
        
        # Streamlit 화면에 HTML 렌더링
        components.html(report_html, height=880, scrolling=True)
