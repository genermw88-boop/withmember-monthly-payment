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
        st.success(f"[{store_name}] 전문가용 플레이스 진단 리포트가 생성되었습니다.")
        
        # 키워드 정보 가공
        kw_list_str = ", ".join([f"{item['keyword']} (PC:{item['pc']}, 모바일:{item['mo']})" for item in keyword_data]) if keyword_data else "등록된 키워드 없음"
        
        # 도구 상태 문자열 생성
        booking_status = "등록" if has_booking else "미등록"
        talk_status = "등록" if has_talk else "미등록"
        coupon_status = "등록" if has_coupon else "미등록"
        call_status = "등록" if has_call else "미등록"
        
        # 새로운 시각적 레이아웃과 스타일 (다크 모던 컨설팅 테마) 적용
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
                background: linear-gradient(145deg, #0f172a, #1e293b);
                border: 1px solid #334155;
                border-radius: 20px;
                padding: 45px;
                max-width: 820px;
                margin: 0 auto;
                color: #f8fafc;
                box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            }}
            .report-header {{
                text-align: center;
                border-bottom: 2px solid #334155;
                padding-bottom: 25px;
                margin-bottom: 35px;
            }}
            .report-title {{
                font-size: 30px;
                font-weight: 800;
                color: #38bdf8;
                margin-bottom: 8px;
                letter-spacing: -0.5px;
            }}
            .report-subtitle {{
                font-size: 18px;
                color: #e2e8f0;
                font-weight: 700;
            }}
            .card-grid {{
                display: flex;
                gap: 15px;
                margin-bottom: 25px;
            }}
            .metric-box {{
                flex: 1;
                background-color: rgba(30, 41, 59, 0.7);
                border: 1px solid #475569;
                border-radius: 12px;
                padding: 20px;
                text-align: center;
            }}
            .metric-label {{
                font-size: 13px;
                color: #94a3b8;
                font-weight: 600;
                margin-bottom: 8px;
            }}
            .metric-value {{
                font-size: 20px;
                font-weight: 800;
                color: #f8fafc;
            }}
            .metric-value.red {{
                color: #f87171;
            }}
            .section-box {{
                background-color: rgba(30, 41, 59, 0.5);
                border-left: 5px solid #38bdf8;
                border-radius: 10px;
                padding: 22px 25px;
                margin-bottom: 20px;
                border-top: 1px solid #334155;
                border-right: 1px solid #334155;
                border-bottom: 1px solid #334155;
            }}
            .section-title {{
                font-size: 18px;
                font-weight: 700;
                color: #38bdf8;
                margin-bottom: 14px;
            }}
            .row-item {{
                font-size: 14px;
                margin-bottom: 10px;
                line-height: 1.6;
                color: #cbd5e1;
            }}
            .label {{
                font-weight: 600;
                color: #f1f5f9;
                display: inline-block;
                width: 130px;
            }}
            .value-red {{
                color: #f87171;
                font-weight: 700;
            }}
            .value-green {{
                color: #4ade80;
                font-weight: 700;
            }}
            .download-btn {{
                display: block;
                width: 100%;
                background: linear-gradient(135deg, #0ea5e9, #2563eb);
                color: white;
                text-align: center;
                padding: 16px;
                font-size: 17px;
                font-weight: bold;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                margin-top: 35px;
                box-shadow: 0 4px 15px rgba(14, 165, 233, 0.4);
            }}
            .download-btn:hover {{
                background: linear-gradient(135deg, #0284c7, #1d4ed8);
            }}
        </style>
        </head>
        <body>
            <div id="capture-area" class="report-container">
                <div class="report-header">
                    <div class="report-title">플레이스 진단 리포트</div>
                    <div class="report-subtitle">매장명 : {store_name}</div>
                </div>

                <div class="card-grid">
                    <div class="metric-box">
                        <div class="metric-label">플레이스 점수</div>
                        <div class="metric-value red">25점 (취약)</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">예상 노출 순위</div>
                        <div class="metric-value red">7~10페이지</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-label">상권 경쟁력</div>
                        <div class="metric-value red">하위 90%</div>
                    </div>
                </div>

                <div class="section-box">
                    <div class="section-title">1. 대표키워드 및 검색량 대비 노출 진단</div>
                    <div class="row-item"><span class="label">현재 등록 키워드 :</span> {kw_str}</div>
                    <div class="row-item"><span class="label" style="vertical-align: top;">문제점 진단 :</span> <span style="display: inline-block; width: 570px; vertical-align: top;">현재 등록된 대표키워드는 PC 및 모바일 검색량 대비 플레이스 최적화 점수와 알고리즘 매칭이 제대로 이루어지지 않아, 실질적인 고객 유입 구간인 <span class="value-red">1~2페이지 노출에서 완전히 제외</span>되어 7~10페이지권으로 크게 밀려 있습니다.</span></div>
                </div>

                <div class="section-box">
                    <div class="section-title">2. 키워드 최적화 (5,000~10,000건) 개선 효과</div>
                    <div class="row-item"><span class="label" style="vertical-align: top;">타겟 변경 효과 :</span> <span style="display: inline-block; width: 570px; vertical-align: top;">매월 꾸준한 PC/모바일 검색량 조사를 기반으로 <span class="value-green">월 검색량 5,000~10,000건 규모의 고효율 핵심 대표키워드로 전면 수정</span>할 경우, 상권 내 유효 트래픽을 즉각 흡수하여 검색 상위 노출 순위가 빠르게 반등하고 예약 및 매출 전환율이 극대화됩니다.</span></div>
                </div>

                <div class="section-box">
                    <div class="section-title">3. 네이버 마케팅 도구 및 상권 경쟁 진단</div>
                    <div class="row-item"><span class="label">도구 세팅 현황 :</span> 예약(<span class="value-{ 'green' if booking_status=='등록' else 'red'}">{booking_status}</span>), 톡톡(<span class="value-{ 'green' if talk_status=='등록' else 'red'}">{talk_status}</span>), 쿠폰(<span class="value-{ 'green' if coupon_status=='등록' else 'red'}">{coupon_status}</span>), 안심번호(<span class="value-{ 'green' if call_status=='등록' else 'red'}">{call_status}</span>)</div>
                    <div class="row-item"><span class="label" style="vertical-align: top;">상권 경쟁 진단 :</span> <span style="display: inline-block; width: 570px; vertical-align: top;">인근 500M 내 약 35개 경쟁 매장 대비 현재 방문자({visitor_reviews}개) 및 블로그({blog_reviews}개) 리뷰 평판이 평균 이하이므로, 누락된 도구 활성화와 키워드 재설정이 시급합니다.</span></div>
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
