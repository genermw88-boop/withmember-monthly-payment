import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="위드멤버 마케팅 자동화 툴", page_icon="📊", layout="wide")

st.title("위드멤버 마케팅 자동화 및 리포트 툴 🚀")
st.write("키워드 진단 및 AI 마케팅 리포트 자동 생성 시스템입니다.")

# 2. Streamlit Secrets에서 OpenAI 키 불러오기 (선택 사항)
try:
    OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", "")
except Exception:
    OPENAI_API_KEY = ""

# 3. 앱 UI 및 실행 로직
st.subheader("🔍 플레이스 SEO 및 키워드 진단")
keyword_input = st.text_input("분석할 업종 및 키워드를 입력하세요 (예: 광주 술집, 플레이스최적화 등)")

if st.button("마케팅 진단 리포트 생성"):
    if keyword_input:
        with st.spinner(f"'{keyword_input}' 맞춤형 마케팅 리포트를 분석 및 생성하는 중입니다..."):
            
            # 시뮬레이션 지표 출력
            col1, col2, col3 = st.columns(3)
            col1.metric("예상 월간 검색량", "약 12,400회", "+15% 증가세")
            col2.metric("경쟁 강도", "중급 (MID)", "최적화 공략 가능")
            col3.metric("플레이스 SEO 지수", "78점", "상위 노출 양호")
            
            st.markdown("---")
            st.subheader("📋 위드멤버 AI 마케팅 전략 진단 리포트")
            
            report_content = f"""
            ### [{keyword_input}] 맞춤형 플레이스 SEO 및 마케팅 전략
            
            1. **키워드 및 상권 특성 분석**
               - '{keyword_input}' 키워드는 모바일 검색 유입 비율이 매우 높으며, 주말 및 저녁 시간대 전환율이 높게 나타나는 특징이 있습니다.
               - 상위 노출을 위해 네이버 플레이스 정보(영업시간, 메뉴, 정교한 카테고리 설정)의 완결성을 높여야 합니다.
            
            2. **네이버 플레이스 SEO 핵심 실행 과제**
               - **사진 최적화:** 매장 전경, 대표 메뉴, 시그니처 서비스의 고화질 이미지 업로드 및 업로드 주기 유지
               - **리뷰 마케팅:** 방문자 리뷰 내 키워드 자연 노출 유도 (예: 맛집, 데이트코스 등 세부 키워드 동반 확보)
            
            3. **블로그 및 숏폼 연계 마케팅 제안**
               - 최적화 블로그를 통한 체험단 리뷰 배포로 바이럴 신뢰도 구축
               - 인스타그램 릴스와 유튜브 쇼츠를 활용한 15초 숏폼 영상 제작 및 플레이스 링크 연동
            """
            st.markdown(report_content)
            
    else:
        st.warning("분석할 키워드를 먼저 입력해주세요.")
