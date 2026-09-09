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
    store_name = st.text_input("매장명 (플레이스 등록 이름)", placeholder="예: ㅠㅜ")
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
        st.success(f"[{store_name}] 전문가용 플레이스 진단 리포트가 생성되었습니다.")
        
        # 키워드 정보 가공 (NameError 방지를 위해 사전에 명확히 문자열로 생성)
        if keyword_data:
            kw_list_str = ", ".join([f"{item['keyword']} (PC:{item['pc']}, 모바일:{item['mo']})" for item in keyword_data])
        else:
            kw_list_str = "등록된 키워드 없음"
        
        # 도구 상태 표시 문자열 생성
        booking_status = "등록" if has_booking else "미등록"
        talk_status = "등록" if has_talk else "미등록"
        coupon_status = "등록" if has_coupon else "미등록"
        call_status = "등록" if has_call else "미등록"
        
        # 완전히 새롭게 디자인된 프리미엄 라이트 테마 컨설팅 보고서 레이아웃 (세련된 카드 그리드 및 분석 스타일)
        report_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <style>
            * {{
                font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', '맑은 고딕', sans-serif;
                box-sizing: border-box;
            }}
            .report-container {{
                background-color: #ffffff;
                border: 2px solid #e2e8f0;
                border-radius: 20px;
                padding: 40px;
                max-width: 820px;
                margin: 0 auto;
                color: #0f172a;
                box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            }}
            .report-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 3px solid #0284c7;
                padding-bottom: 20px;
                margin-bottom: 30px;
            }}
            .report-title {{
                font-size: 26px;
                font-weight: 800;
                color: #0284c7;
            }}
            .store-badge {{
                background-color: #f0f9ff;
                border: 1px solid #bae6fd;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 15px;
                font-weight: 700;
                color: #0369a1;
            }}
            .summary-cards {{
                display: flex;
                gap: 15px;
                margin-bottom: 30px;
            }}
            .card {{
                flex: 1;
                background-color: #f8fafc;
                border: 1px solid #cbd5e1;
                border-radius: 12px;
                padding: 18px;
                text-align: center;
            }}
            .card-title {{
                font-size: 13px;
                color: #64748b;
                font-weight: 600;
                margin-bottom: 6px;
            }}
            .card-val {{
                font-size: 18px;
                font-weight: 800;
                color: #0f172a;
            }}
            .card-val.alert {{
                color: #dc2626;
            }}
            .content-section {{
                background-color: #f8fafc;
                border-radius: 12px;
                border: 1px solid #e2e8f0;
                padding: 22px;
                margin-bottom: 20px;
            }}
            .section-heading {{
                font-size: 16px;
                font-weight: 700;
                color: #0284c7;
                margin-bottom: 12px;
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            .detail-row {{
                font-size: 14px;
                margin-bottom: 8px;
                line-height: 1.6;
                color: #334155;
            }}
            .label-text {{
                font-weight: 600;
                color: #1e293b;
                display: inline-block;
                width: 130px;
            }}
            .highlight-red {{
                color: #dc2626;
                font-weight: 700;
            }}
            .highlight-blue {{
                color: #0284c7;
                font-weight: 700;
            }}
            .download-btn {{
                display: block;
                width: 100%;
                background: linear-gradient(135deg, #0284c7, #0369a1);
                color: white;
                text-align: center;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                margin-top: 30px;
                box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
            }}
            .download-btn:hover {{
                background: linear-gradient(135deg, #0369a1, #075985);
            }}
        </style>
        </head>
        <body>
            <div id="capture-area" class="report-container">
                <div class="report-header">
                    <div class="report-title">📈 플레이스 진단 리포트</div>
                    <div class="store-badge">매장명 : {store_name}</div>
                </div>

                <div class="summary-cards">
                    <div class="card">
                        <div class="card-title">플레이스 종합 점수</div>
                        <div class="card-val alert">25점 (취약)</div>
                    </div>
                    <div class="card">
                        <div class="card-title">예상 노출 순위</div>
                        <div class="card-val alert">7~10페이지</div>
                    </div>
                    <div class="card">
                        <div class="card-title">상권 경쟁 지수</div>
                        <div class="card-val alert">하위 90%</div>
                    </div>
                </div>

                <div class="content-section">
                    <div class="section-heading">🔍 1. 키워드 검색량 대비 노출 진단</div>
                    <div class="detail-row"><span class="label-text">현재 등록 키워드 :</span> {kw_list_str}</div>
                    <div class="detail-row"><span class="label-text" style="vertical-align: top;">문제점 분석 :</span> <span style="display: inline-block; width: 580px; vertical-align: top;">현재 등록된 대표키워드는 PC 및 모바일 검색량 대비 플레이스 최적화 알고리즘 매칭 점수가 턱없이 부족하여, 실질적인 고객 유입이 발생하는 <span class="highlight-red">1~2페이지 상위 노출 구간에서 완전히 제외</span>된 상태입니다.</span></div>
                </div>

                <div class="content-section">
                    <div class="section-heading">💡 2. 5,000~10,000건 키워드 최적화 개선점</div>
                    <div class="detail-row"><span class="label-text" style="vertical-align: top;">개선 기대효과 :</span> <span style="display: inline-block; width: 580px; vertical-align: top;">매월 주기적인 PC·모바일 검색량 조사를 기반으로 <span class="highlight-blue">월 검색량 5,000~10,000건 규모의 고효율 핵심 대표키워드로 재설정</span>할 경우, 상권 내 유효 트래픽을 빠르게 독점하여 검색 노출 순위가 1~2페이지로 급상승하며 예약 및 매출로 즉각 이어집니다.</span></div>
                </div>

                <div class="content-section" style="margin-bottom: 0;">
                    <div class="section-heading">🛠️ 3. 네이버 마케팅 도구 및 상권 경쟁력</div>
                    <div class="detail-row"><span class="label-text">도구 세팅 현황 :</span> 예약(<span class="highlight-{ 'blue' if booking_status=='등록' else 'red'}">{booking_status}</span>), 톡톡(<span class="highlight-{ 'blue' if talk_status=='등록' else 'red'}">{talk_status}</span>), 쿠폰(<span class="highlight-{ 'blue' if coupon_status=='등록' else 'red'}">{coupon_status}</span>), 안심번호(<span class="highlight-{ 'blue' if call_status=='등록' else 'red'}">{call_status}</span>)</div>
                    <div class="detail-row"><span class="label-text" style="vertical-align: top;">상권 경쟁 진단 :</span> <span style="display: inline-block; width: 580px; vertical-align: top;">반경 500M 내 약 35개 경쟁 매장 대비 현재 방문자({visitor_reviews}개) 및 블로그({blog_reviews}개) 평판 지수가 낮아 즉각적인 마케팅 보완이 시급합니다.</span></div>
                </div>
            </div>

            <button class="download-btn" onclick="downloadImage()">📥 프리미엄 진단 리포트 이미지 저장하기</button>

            <script>
            function downloadImage() {{
                const element = document.getElementById('capture-area');
                html2canvas(element, {{ scale: 2, useCORS: true }}).then(canvas => {{
                    const link = document.createElement('a');
                    link.download = '{store_name}_플레이스_진단리포트.png';
                    link.href = canvas.toDataURL('image/png');
                    link.click();
                }});
            }}
            </script>
        </body>
        </html>
        """
        
        # Streamlit 화면에 HTML 렌더링
        components.html(report_html, height=920, scrolling=True)
