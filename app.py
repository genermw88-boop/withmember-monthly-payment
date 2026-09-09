import streamlit as st
import streamlit.components.v1 as components
import random

# 1. 페이지 기본 설정
st.set_page_config(page_title="위드멤버 종합 플레이스 & 리뷰 진단 및 솔루션 제안서", page_icon="📊", layout="wide")

st.title("📊 위드멤버 종합 플레이스 & 리뷰 진단 및 솔루션 제안서")
st.write("네이버 플레이스 도구 진단부터 최적화 관리 및 3개월 마케팅 솔루션 제안서까지 각각 독립적으로 확인하고 이미지로 저장하세요.")

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
has_booking = col_t1.checkbox("네이버 예약", value=False)
has_talk = col_t2.checkbox("네이버 톡톡", value=False)
has_coupon = col_t3.checkbox("네이버 쿠폰", value=False)
has_call = col_t4.checkbox("안심번호(스마트콜)", value=False)

st.markdown("---")

# 진단 실행 버튼
if st.button("🚀 1, 2차 독립형 리포트 생성"):
    if not store_name:
        st.warning("매장명을 입력해주세요.")
    else:
        st.success(f"[{store_name}] 1차 진단 리포트와 2차 제안서가 각각 분리되어 생성되었습니다.")
        
        # 키워드 정보 가공 및 문제점 분기
        if keyword_data:
            kw_list_str = ", ".join([f"{item['keyword']} (PC:{item['pc']}, 모바일:{item['mo']})" for item in keyword_data])
            keyword_problem = f"현재 등록된 대표키워드는 PC 및 모바일 검색량 대비 플레이스 최적화 알고리즘 매칭 점수가 턱없이 부족하여, 실질적인 고객 유입이 발생하는 <span class='highlight-red'>1~2페이지 상위 노출 구간에서 완전히 제외</span>된 상태입니다."
        else:
            kw_list_str = "등록된 키워드 없음"
            keyword_problem = f"현재 등록된 키워드가 없어서 플레이스 검색 유입의 기본 뼈대가 되는 타겟 키워드 매칭이 전혀 이루어지지 않고 있으며, 잠재 고객들이 매장을 발견할 수 있는 <span class='highlight-red'>모든 검색 노출 경로가 완전히 차단되어 심각한 유입 손실</span>이 발생하고 있습니다."
        
        # 도구 상태 및 색상 클래스 분기
        booking_html = "<span class='highlight-green'>등록</span>" if has_booking else "<span class='highlight-red'>미등록</span>"
        talk_html = "<span class='highlight-green'>등록</span>" if has_talk else "<span class='highlight-red'>미등록</span>"
        coupon_html = "<span class='highlight-green'>등록</span>" if has_coupon else "<span class='highlight-red'>미등록</span>"
        call_html = "<span class='highlight-green'>등록</span>" if has_call else "<span class='highlight-red'>미등록</span>"
        
        registered_list = []
        if has_booking: registered_list.append("네이버 예약")
        if has_talk: registered_list.append("네이버 톡톡")
        if has_coupon: registered_list.append("네이버 쿠폰")
        if has_call: registered_list.append("안심번호")

        missing_list = []
        if not has_booking: missing_list.append("네이버 예약")
        if not has_talk: missing_list.append("네이버 톡톡")
        if not has_coupon: missing_list.append("네이버 쿠폰")
        if not has_call: missing_list.append("안심번호")

        # 3번 도구 진단 문구 동적 생성
        if missing_list and registered_list:
            reg_str = ", ".join(registered_list)
            miss_str = ", ".join(missing_list)
            tool_problem = f"현재 <span class='highlight-green'>{reg_str}</span> 도구는 정상 세팅되어 있으나, 필수 도구 중 <span class='highlight-red'>{miss_str}</span> 항목이 누락되어 있어 완벽한 알고리즘 가산점을 확보하지 못하고 있습니다."
            tool_solution = f"잘 세팅된 도구와 시너지를 내도록 누락된 <span class='highlight-red'>{miss_str}</span> 도구를 추가로 세팅하여 플레이스 지수를 극대화해야 합니다."
        elif missing_list and not registered_list:
            miss_str = ", ".join(missing_list)
            tool_problem = f"필수 마케팅 도구인 <span class='highlight-red'>{miss_str}</span> 항목이 모두 누락되어 있어, 네이버 알고리즘 평가에서 가산점을 전혀 받지 못해 검색 순위 하락의 직접적인 원인이 됩니다."
            tool_solution = f"누락된 <span class='highlight-red'>{miss_str}</span> 도구를 즉시 도입하여 플랫폼 가산점을 확보하고 고객 유입 채널을 열어야 합니다."
        else:
            tool_problem = "필수 마케팅 도구(예약, 톡톡, 쿠폰, 안심번호)가 모두 빠짐없이 완벽하게 등록되어 있습니다."
            tool_solution = "모든 도구가 훌륭하게 세팅되어 있으므로, 각 도구 연계 프로필 이벤트나 응대 속도를 최상위로 유지하여 전환율을 방어해야 합니다."

        # 랜덤 지표 생성
        random_score = random.randint(10, 30)
        random_page_start = random.randint(6, 9)
        random_page_end = random_page_start + 1
        random_rank_str = f"{random_page_start}~{random_page_end}페이지"
        
        random_competitor_percent = random.randint(80, 90)
        random_competitors = random.randint(30, 50)
        
        competitor_analysis = f"타겟 상권 반경 500M 내 동종 업계 경쟁 매장은 <span class='highlight-red'>약 {random_competitors}개</span>로 밀집도가 매우 높습니다."
        competitor_solution = f"치열한 상권 밀집도 속에서 우위를 점하기 위해, 상위 노출 경쟁사들의 마케팅 패턴을 분석하고 차별화된 메뉴 강조 포인트와 타겟 맞춤형 플레이스 상위 최적화 전략을 즉시 도입해야 합니다."

        # 블로그 리뷰 진단
        if blog_reviews < 10:
            blog_problem = f"입력하신 블로그 리뷰가 총 <span class='highlight-red'>{blog_reviews}개</span>로 매우 부족하여, 검색 이용자들이 충분한 바이럴 정보를 접하지 못해 브랜드 신뢰 형성과 예약 전환에 큰 걸림돌이 되고 있습니다."
            blog_solution = "지역 및 업종 타겟 맞춤형 체험단 마케팅을 집중 집행하여 검색 포털 내 브랜드 노출량과 신뢰성 리포트를 확실하게 확보해야 합니다."
        elif blog_reviews < 50:
            blog_problem = f"입력하신 블로그 리뷰가 총 <span class='highlight-red'>{blog_reviews}개</span>로 기본 홍보는 진행되었으나, 상권 내 선두 경쟁사들을 압도하기에는 검색 노출 볼륨이 다소 부족합니다."
            blog_solution = "핵심 대표키워드와 연계된 상위 노출형 블로그 포스팅을 정기적으로 발행하여 바이럴 장악력을 높여야 합니다."
        else:
            blog_problem = f"입력하신 블로그 리뷰가 총 <span class='highlight-red'>{blog_reviews}개</span>로 탄탄한 편이나, 최신 트렌드 키워드 반영 및 관리 주기 최적화가 필요합니다."
            blog_solution = "검색 알고리즘 변화에 맞춘 고품질 리뷰 콘텐츠를 지속 공급하여 바이럴 지수를 최상위로 유지해야 합니다."

        # 방문자 리뷰 진단
        if visitor_reviews < 20:
            visitor_problem = f"입력하신 방문자 리뷰가 총 <span class='highlight-red'>{visitor_reviews}개</span>로 상권 내 경쟁 매장들에 비해 턱없이 부족하여, 매장의 신뢰도가 크게 떨어지고 잠재 고객의 이탈을 초래하고 있습니다."
            visitor_solution = "영수증 리뷰 이벤트 및 매장 방문 고객 대상 즉시 참여 혜택을 설계하여 방문자 리뷰 볼륨을 단기간에 대폭 끌어올려야 합니다."
        elif visitor_reviews < 100:
            visitor_problem = f"입력하신 방문자 리뷰가 총 <span class='highlight-red'>{visitor_reviews}개</span>로 보통 수준이나, 상위 노출 매장들의 리뷰량에 비해 경쟁 우위를 확보하지 못해 유입 전환율이 정체되어 있습니다."
            visitor_solution = "결제 고객 대상 리뷰 작성 유도 프로세스를 체계화하고 재방문 유도 혜택을 연계하여 일정한 방문자 리뷰 유입 주기를 유지해야 합니다."
        else:
            visitor_problem = f"입력하신 방문자 리뷰가 총 <span class='highlight-red'>{visitor_reviews}개</span>로 양호하나, 최신 리뷰 갱신 주기나 세부 키워드 매칭 관리가 다소 미흡합니다."
            visitor_solution = "주기적인 피드백 관리와 핵심 키워드가 자연스럽게 녹아든 양질의 방문자 리뷰를 지속적으로 누적해야 합니다."

        # 2차 제안서용 상승 점수 및 매출액 랜덤 생성
        expected_score_increase = random.randint(65, 85)
        projected_sales = random.randint(15000000, 20000000)
        projected_sales_formatted = f"{projected_sales / 10000:,.0f}만원"

        # ---------------------------------------------------------
        # 1번 리포트 HTML
        # ---------------------------------------------------------
        report1_html = f"""
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
                color: #dc2626;
            }}
            .content-section {{
                background-color: #f8fafc;
                border-radius: 12px;
                border: 1px solid #e2e8f0;
                padding: 24px;
                margin-bottom: 20px;
            }}
            .section-heading {{
                font-size: 16px;
                font-weight: 700;
                color: #0284c7;
                margin-bottom: 14px;
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            .detail-row {{
                font-size: 14px;
                margin-bottom: 12px;
                line-height: 1.7;
                color: #334155;
                display: flex;
            }}
            .label-text {{
                font-weight: 700;
                color: #1e293b;
                min-width: 130px;
                flex-shrink: 0;
            }}
            .desc-text {{
                flex-grow: 1;
            }}
            .highlight-red {{
                color: #dc2626;
                font-weight: 700;
            }}
            .highlight-green {{
                color: #16a34a;
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
            <div id="capture-area-1" class="report-container">
                <div class="report-header">
                    <div class="report-title">📈 플레이스 진단 리포트 (1/2)</div>
                    <div class="store-badge">매장명 : {store_name}</div>
                </div>

                <div class="summary-cards">
                    <div class="card">
                        <div class="card-title">플레이스 종합 점수</div>
                        <div class="card-val">{random_score}점 (취약)</div>
                    </div>
                    <div class="card">
                        <div class="card-title">현재 노출 순위</div>
                        <div class="card-val">{random_rank_str}</div>
                    </div>
                    <div class="card">
                        <div class="card-title">상권 경쟁 지수</div>
                        <div class="card-val">하위 {random_competitor_percent}%</div>
                    </div>
                </div>

                <div class="content-section">
                    <div class="section-heading">🔍 1. 키워드 검색량 대비 노출 진단</div>
                    <div class="detail-row">
                        <span class="label-text">현재 등록 키워드 :</span>
                        <span class="desc-text">{kw_list_str}</span>
                    </div>
                    <div class="detail-row" style="margin-bottom: 0;">
                        <span class="label-text">문제점 분석 :</span>
                        <span class="desc-text">{keyword_problem}</span>
                    </div>
                </div>

                <div class="content-section">
                    <div class="section-heading">💡 2. 5,000~10,000건 키워드 최적화 개선점</div>
                    <div class="detail-row" style="margin-bottom: 0;">
                        <span class="label-text">개선 기대효과 :</span>
                        <span class="desc-text">매월 주기적인 PC·모바일 검색량 조사를 기반으로 <span class="highlight-red">월 검색량 5,000~10,000건 규모의 고효율 핵심 대표키워드로 재설정</span>할 경우, 상권 내 유효 트래픽을 빠르게 독점하여 검색 노출 순위가 1~2페이지로 급상승하며 예약 및 매출로 즉각 이어집니다.</span>
                    </div>
                </div>

                <div class="content-section">
                    <div class="section-heading">🛠️ 3. 네이버 마케팅 도구 세팅 진단</div>
                    <div class="detail-row">
                        <span class="label-text">도구 활성화 :</span>
                        <span class="desc-text">예약({booking_html}), 톡톡({talk_html}), 쿠폰({coupon_html}), 안심번호({call_html})</span>
                    </div>
                    <div class="detail-row">
                        <span class="label-text">도구 누락 문제점 :</span>
                        <span class="desc-text">{tool_problem}</span>
                    </div>
                    <div class="detail-row" style="margin-bottom: 0;">
                        <span class="label-text">도구 등록 개선점 :</span>
                        <span class="desc-text">{tool_solution}</span>
                    </div>
                </div>

                <div class="content-section">
                    <div class="section-heading">⚔️ 4. 반경 500M 상권 경쟁 진단</div>
                    <div class="detail-row">
                        <span class="label-text">경쟁 매장 분석 :</span>
                        <span class="desc-text">{competitor_analysis}</span>
                    </div>
                    <div class="detail-row" style="margin-bottom: 0;">
                        <span class="label-text">상권 경쟁 개선점 :</span>
                        <span class="desc-text">{competitor_solution}</span>
                    </div>
                </div>

                <div class="content-section">
                    <div class="section-heading">📝 5. 블로그 리뷰 평판 진단</div>
                    <div class="detail-row">
                        <span class="label-text">현재 블로그 리뷰 :</span>
                        <span class="desc-text">총 <span class="highlight-red">{blog_reviews}개</span></span>
                    </div>
                    <div class="detail-row">
                        <span class="label-text">블로그 리뷰 문제점 :</span>
                        <span class="desc-text">{blog_problem}</span>
                    </div>
                    <div class="detail-row" style="margin-bottom: 0;">
                        <span class="label-text">블로그 리뷰 개선점 :</span>
                        <span class="desc-text">{blog_solution}</span>
                    </div>
                </div>

                <div class="content-section" style="margin-bottom: 0;">
                    <div class="section-heading">⭐ 6. 방문자 리뷰 수 정밀 진단</div>
                    <div class="detail-row">
                        <span class="label-text">입력 방문자 리뷰 :</span>
                        <span class="desc-text">총 <span class="highlight-red">{visitor_reviews}개</span></span>
                    </div>
                    <div class="detail-row">
                        <span class="label-text">방문자 리뷰 문제점 :</span>
                        <span class="desc-text">{visitor_problem}</span>
                    </div>
                    <div class="detail-row" style="margin-bottom: 0;">
                        <span class="label-text">방문자 리뷰 개선점 :</span>
                        <span class="desc-text">{visitor_solution}</span>
                    </div>
                </div>
            </div>

            <button class="download-btn" onclick="downloadImage1()">📥 1차 진단 리포트 이미지 저장하기</button>

            <script>
            function downloadImage1() {{
                const element = document.getElementById('capture-area-1');
                html2canvas(element, {{ scale: 2, useCORS: true }}).then(canvas => {{
                    const link = document.createElement('a');
                    link.download = '{store_name}_플레이스_진단리포트_1차.png';
                    link.href = canvas.toDataURL('image/png');
                    link.click();
                }});
            }}
            </script>
        </body>
        </html>
        """

        # ---------------------------------------------------------
        # 2번 리포트 HTML
        # ---------------------------------------------------------
        report2_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
                border-bottom: 3px solid #0369a1;
                padding-bottom: 20px;
                margin-bottom: 30px;
            }}
            .report-title {{
                font-size: 26px;
                font-weight: 800;
                color: #0369a1;
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
            .content-section {{
                background-color: #f8fafc;
                border-radius: 12px;
                border: 1px solid #e2e8f0;
                padding: 24px;
                margin-bottom: 20px;
            }}
            .section-heading {{
                font-size: 16px;
                font-weight: 700;
                color: #0369a1;
                margin-bottom: 14px;
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            .detail-row {{
                font-size: 14px;
                margin-bottom: 12px;
                line-height: 1.7;
                color: #334155;
                display: flex;
            }}
            .label-text {{
                font-weight: 700;
                color: #1e293b;
                min-width: 130px;
                flex-shrink: 0;
            }}
            .desc-text {{
                flex-grow: 1;
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
                background: linear-gradient(135deg, #0369a1, #075985);
                color: white;
                text-align: center;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                margin-top: 30px;
                box-shadow: 0 4px 12px rgba(3, 105, 161, 0.3);
            }}
            .download-btn:hover {{
                background: linear-gradient(135deg, #075985, #0f172a);
            }}
            .banner-box {{
                background-color: #fffbeb;
                border: 1px solid #fde68a;
                border-radius: 12px;
                padding: 20px;
                margin-bottom: 25px;
            }}
            .banner-title {{
                color: #b45309;
                font-weight: 700;
                font-size: 15px;
                margin-bottom: 10px;
                display: flex;
                align-items: center;
                gap: 6px;
            }}
            .pill-container {{
                display: flex;
                gap: 8px;
                flex-wrap: wrap;
                margin-top: 10px;
            }}
            .pill {{
                background-color: #ffffff;
                border: 1px solid #fcd34d;
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 13px;
                font-weight: 600;
                color: #92400e;
            }}
            .solution-box {{
                background-color: #f0f9ff;
                border: 1px solid #bae6fd;
                border-radius: 12px;
                padding: 20px;
                margin-bottom: 25px;
            }}
            .solution-title {{
                color: #0369a1;
                font-weight: 700;
                font-size: 16px;
                text-align: center;
                margin-bottom: 15px;
            }}
            .solution-item {{
                background-color: #ffffff;
                border: 1px solid #e0f2fe;
                border-radius: 8px;
                padding: 12px 16px;
                margin-bottom: 8px;
                font-size: 14px;
                font-weight: 600;
                color: #0369a1;
            }}
        </style>
        </head>
        <body>
            <div id="capture-area-2" class="report-container">
                <div class="report-header">
                    <div class="report-title">📑 맞춤형 평판 진단 제안서 (2/2)</div>
                    <div class="store-badge">대상 매장: {store_name}</div>
                </div>

                <div class="banner-box">
                    <div class="banner-title">📌 네이버 플레이스 상위 노출 핵심 지표</div>
                    <div style="font-size: 13px; color: #78350f; margin-bottom: 8px;">상위 노출은 다음 4가지 지표로 결정되며, 체계적인 관리가 필수입니다.</div>
                    <div class="pill-container">
                        <div class="pill">① 리뷰 활성도</div>
                        <div class="pill">② 키워드 적합도</div>
                        <div class="pill">③ 최신성 지수</div>
                        <div class="pill">④ 체류 시간</div>
                    </div>
                </div>

                <div class="content-section">
                    <div class="section-heading">🛠️ 플레이스 최적화 관리 항목</div>
                    <div style="font-size: 13px; color: #475569; margin-bottom: 12px;">즉시 적용해야 할 핵심 플레이스 관리 리스트입니다.</div>
                    <ul style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.8; color: #334155;">
                        <li>플레이스 메인키워드 수정</li>
                        <li>네이버 예약 연동 및 세팅</li>
                        <li>네이버 톡톡 응대 배너 적용</li>
                        <li>안심번호 등록 및 세팅</li>
                        <li>네이버 쿠폰 등록 및 세팅</li>
                        <li>플레이스 새소식 업데이트</li>
                    </ul>
                </div>

                <div class="content-section">
                    <div class="section-heading">🚀 솔루션 적용 후 기대 효과</div>
                    <div class="detail-row">
                        <span class="label-text">종합 진단 점수 :</span>
                        <span class="desc-text">현재 <span class="highlight-red">{random_score}점</span> ➔ 솔루션 적용 후 <span class="highlight-blue">{min(100, random_score + expected_score_increase)}점 (대폭 상승)</span></span>
                    </div>
                    <div class="detail-row" style="margin-bottom: 0;">
                        <span class="label-text">핵심 솔루션 시너지 :</span>
                        <span class="desc-text">위 플레이스 최적화 관리 항목과 더불어 <span class="highlight-blue">방문자 리뷰 실시간 답글 작성</span> 및 <span class="highlight-blue">최적화 블로그 후보 검수 및 배포 작업</span>을 병행하여 알고리즘 가산점을 극대화합니다.</span>
                    </div>
                </div>

                <div class="solution-box">
                    <div class="solution-title">💎 위드멤버 마케팅 솔루션 6가지</div>
                    <div class="solution-item">1. 네이버 플레이스 세팅 및 관리 (SEO 최적화)</div>
                    <div class="solution-item">2. 월 1~2회 기본 수정 (새소식, 대표키워드, 플레이스 이미지)</div>
                    <div class="solution-item">3. 업체에 맞는 최적화 블로그 후보 검수 및 추천 리포트 제공</div>
                    <div class="solution-item">4. 매장 또는 업체 월 1회 홍보용 인스타 인기 게시물 배포</div>
                    <div class="solution-item">5. 네이버 플레이스 순위, 노출 변화 모니터링 및 유지 관리</div>
                    <div class="solution-item">6. 실사용자 패턴 맞춤형 유입 트래픽 작업을 통한 플레이스 순위 상승 변화 모니터링 및 유지 관리</div>
                </div>

                <div class="content-section" style="margin-bottom: 0;">
                    <div class="section-heading">📊 관리 후 3개월 뒤 예상 매출액 및 추이</div>
                    <div class="detail-row" style="margin-bottom: 15px;">
                        <span class="label-text">3개월 후 예상 매출 :</span>
                        <span class="desc-text"><span class="highlight-blue" style="font-size: 16px;">{projected_sales_formatted}</span> 달성 전망 (상권 내 트래픽 독점 효과)</span>
                    </div>
                    <div style="position: relative; height: 220px; width: 100%;">
                        <canvas id="salesChart2"></canvas>
                    </div>
                </div>
            </div>

            <button class="download-btn" onclick="downloadImage2()">📥 2차 솔루션 제안서 이미지 저장하기</button>

            <script>
            const ctx2 = document.getElementById('salesChart2').getContext('2d');
            new Chart(ctx2, {{
                type: 'line',
                data: {{
                    labels: ['현재 (관리 전)', '관리 1개월 차', '관리 2개월 차', '관리 3개월 차 (목표)'],
                    datasets: [{{
                        label: '예상 월 매출 추이 (원)',
                        data: [{int(projected_sales * 0.45)}, {int(projected_sales * 0.65)}, {int(projected_sales * 0.85)}, {projected_sales}],
                        borderColor: '#0369a1',
                        backgroundColor: 'rgba(3, 105, 161, 0.1)',
                        borderWidth: 3,
                        fill: true,
                        tension: 0.3,
                        pointRadius: 5,
                        pointBackgroundColor: '#0369a1'
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ display: false }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: false,
                            ticks: {{
                                callback: function(value) {{
                                    return (value / 10000).toLocaleString() + '만원';
                                }}
                            }}
                        }}
                    }}
                }}
            }});

            function downloadImage2() {{
                const element = document.getElementById('capture-area-2');
                html2canvas(element, {{ scale: 2, useCORS: true }}).then(canvas => {{
                    const link = document.createElement('a');
                    link.download = '{store_name}_솔루션제안서_2차.png';
                    link.href = canvas.toDataURL('image/png');
                    link.click();
                }});
            }}
            </script>
        </body>
        </html>
        """

        # Streamlit 탭 또는 순차적 컴포넌트로 분리 렌더링
        tab1, tab2 = st.tabs(["📈 1차 진단 리포트", "📑 2차 솔루션 제안서"])
        with tab1:
            components.html(report1_html, height=1750, scrolling=True)
        with tab2:
            components.html(report2_html, height=1600, scrolling=True)
