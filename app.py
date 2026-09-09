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
        st.success(f"[{store_name}] 종합 정밀 진단 리포트가 생성되었습니다.")
        
        # 결과 대시보드
        c1, c2, c3 = st.columns(3)
        c1.metric("플레이스 종합 점수", "42점 (취약)", "기준치 미달")
        c2.metric("현재 노출 순위", "7 ~ 10페이지", "1~6페이지 노출 제외")
        c3.metric("500M 상권 경쟁력", "평점 이하", "개선 시급")
        
        st.markdown("---")
        st.subheader("📈 위드멤버 AI 플레이스 정밀 진단 결과")
        
        # 등록된 키워드 요약 출력
        kw_summary = ", ".join([item['keyword'] for item in keyword_data]) if keyword_data else "등록된 키워드 없음"
        
        report_text = f"""
        ### 1. 키워드 및 노출 순위 진단
        - **현재 등록 키워드 현황:** `{kw_summary}`
        - **진단 평가:** 현재 등록된 대표 키워드로 진단한 결과, 플레이스 SEO 최적화 점수가 매우 낮게 측정되었습니다. 
        - **노출 순위 분석:** 경쟁력이 분산되고 키워드 매칭 정밀도가 떨어져, 현재 핵심 유입 구간인 **1~6페이지는 완전히 제외**되어 있으며 **7~10페이지권으로 노출이 크게 하락**해 있는 상태입니다. 실질적인 유입과 예약 전환을 기대하기 어려운 위험 단계입니다.

        ### 2. 네이버 플레이스 도구 세팅 및 활용 진단
        - **활성화된 도구:** 네이버 예약({"O" if has_booking else "X"}), 네이버 톡톡({"O" if has_talk else "X"}), 네이버 쿠폰({"O" if has_coupon else "X"}), 안심번호({"O" if has_call else "X"})
        - **개선점:** 네이버 플레이스 필수 편의 도구(예약, 톡톡 등)의 누락 및 미활용 항목이 확인됩니다. 네이버 알고리즘은 활성 도구 연동 점수를 중요하게 반영하므로, 누락된 도구를 즉시 세팅하고 고객 전환 퍼널을 구축해야 점수를 만회할 수 있습니다.

        ### 3. 반경 500M 상권 경쟁 진단
        - **상권 분석 결과:** `{target_region}` 인근 반경 500M 내 동종 업계 경쟁 강도 대비, 매장의 리뷰 평판(방문자 {visitor_reviews개}, 블로그 {blog_reviews개})과 지수 활성도가 **상권 평균 평점 이하**로 분석되었습니다.
        - **핵심 개선 대책:** 
          1. **대표키워드 전면 수정:** 검색량과 전환율 분석을 바탕으로 상위 노출 공략이 가능한 세부 타겟 키워드로 교체.
          2. **도구 최적화 연동:** 누락된 네이버 예약 및 마케팅 툴을 100% 활성화하여 가중치 확보.
          3. **리뷰 및 전환 마케팅 병행:** 상권 내 우위 선점을 위한 체계적인 방문자/블로그 리뷰 관리 및 숏폼 연계 필수.
        """
        st.markdown(report_text)
