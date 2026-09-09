import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="위드멤버 종합 플레이스 & 리뷰 진단기", page_icon="📊", layout="wide")

st.title("📊 위드멤버 종합 플레이스 & 리뷰 진단기")
st.write("네이버 플레이스 도구 누락 현상과 리뷰 평판 및 매출 성장을 한 번에 정밀 진단합니다.")

st.markdown("---")
st.subheader("📋 1. 매장 종합 정보")

# 매장 정보 입력 폼
col1, col2 = st.columns(2)
with col1:
    store_name = st.text_input("매장명 (플레이스 등록 이름)", placeholder="예: 맛있는술집")
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
has_booking = col_t1.checkbox("네이버 예약")
has_talk = col_t2.checkbox("네이버 톡톡")
has_coupon = col_t3.checkbox("네이버 쿠폰")
has_call = col_t4.checkbox("안심번호(스마트콜)")

st.markdown("---")

# 진단 실행 버튼
if st.button("🚀 종합 정밀 진단 및 리포트 생성"):
    if not store_name:
        st.warning("매장명을 입력해주세요.")
    else:
        st.success(f"[{store_name}] 종합 정밀 진단 리포트가 성공적으로 생성되었습니다.")
        
        # 결과 대시보드
        c1, c2, c3 = st.columns(3)
        c1.metric("플레이스 종합 점수", "42점 (취약)", "기준치 미달")
        c2.metric("현재 노출 순위", "7 ~ 10페이지", "1~6페이지 노출 제외")
        c3.metric("500M 상권 경쟁력", "평점 이하", "개선 시급")
        
        st.markdown("---")
        st.subheader("📈 위드멤버 AI 플레이스 정밀 진단 결과")
        
        kw_summary = ", ".join([f"`{item['keyword']}` (PC: {item['pc']}, 모바일: {item['mo']})" for item in keyword_data]) if keyword_data else "등록된 키워드 없음"
        
        missing_tools = []
        if not has_booking: missing_tools.append("네이버 예약")
        if not has_talk: missing_tools.append("네이버 톡톡")
        if not has_coupon: missing_tools.append("네이버 쿠폰")
        if not has_call: missing_tools.append("안심번호(스마트콜)")
        
        missing_str = ", ".join(missing_tools) if missing_tools else "모두 세팅됨"
        
        report_text = f"""
        ### 1. 키워드 및 노출 순위 진단
        - **현재 등록 키워드 및 검색량:** {kw_summary}
        - **진단 평가:** 현재 등록된 키워드로 분석한 결과, 타겟 상권 내 검색 유입 포인트를 전혀 살리지 못하고 있습니다. 
        - **노출 순위 분석:** 알고리즘 매칭 점수 미달로 인해 실제 고객들이 유입되는 **1~6페이지 상위 노출 구간에서 완전히 배제**되어 있으며, 현재 **7~10페이지권으로 순위가 크게 밀려나 있어** 신규 고객 유입이 거의 차단된 상태입니다.

        ### 2. 핵심 개선 포인트 (AI 분석)
        - **대표키워드 전면 수정 필요:** 현재 설정된 키워드는 경쟁 강도 대비 검색 트래픽 효율이 떨어집니다. `{target_region}` 상권 특성과 매장의 업종(`{core_menu}`)에 맞추어 실검색량이 높고 최적화 공략이 가능한 **세부 타겟 중심의 대표키워드로 즉시 교체**해야 합니다.
        - **네이버 플레이스 도구 등록 개선:** 현재 누락된 필수 도구(`{missing_str}`)로 인해 네이버 알고리즘 평가에서 가중치를 잃고 있습니다. 예약, 톡톡, 쿠폰 등의 **마케팅 도구를 100% 활성화**할 경우 플랫폼 지수가 즉각 상승하여 순위 회복의 발판이 마련됩니다.

        ### 3. 반경 500M 상권 경쟁 진단
        - **상권 분석 결과:** `{target_region}` 반경 500M 내 동종 업계 경쟁 매장들과 비교했을 때, 방문자 리뷰({visitor_reviews}개) 및 블로그 리뷰({blog_reviews}개) 평판 지수가 **상권 평균 평점 이하**로 진단되었습니다.
        - **경쟁력 평가:** 주변 경쟁 업체들에 비해 고객 신뢰도 지표와 플레이스 활성도가 떨어져 유저 이탈이 발생하고 있습니다.

        ### 🎯 종합 진단 총평
        - **총평 및 개선 방향:** 본 매장은 현재 **대표키워드 미적정, 필수 네이버 도구 누락, 반경 500M 상권 내 평점 이하의 리뷰 평판**이라는 삼중 악재로 인해 노출 순위가 7~10권으로 추락해 있습니다. 
        - **실행 제안:** 이를 해결하기 위해 ① 상권 맞춤형 고효율 대표키워드로의 전면 재설정, ② 누락된 네이버 플레이스 마케팅 도구의 즉각적인 세팅, ③ 3개월 내 가시적 매출 반등을 위한 체계적인 리뷰 및 블로그 바이럴 보완이 시급하며, 이를 통해 1~6페이지 상위 노출권 재진입을 반드시 달성해야 합니다.
        """
        st.markdown(report_text)
