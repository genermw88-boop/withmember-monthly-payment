import streamlit as st
import time
import hashlib
import hmac
import base64
import requests
import json

# 1. 페이지 기본 설정
st.set_page_config(page_title="위드멤버 마케팅 자동화 툴", page_icon="📊", layout="wide")

st.title("위드멤버 마케팅 자동화 및 리포트 툴 🚀")
st.write("네이버 검색광고 API 데이터와 AI를 활용하여 키워드 분석 리포트를 생성합니다.")

# 2. Streamlit Secrets에서 API 키 불러오기
try:
    NAVER_CLIENT_ID = st.secrets["NAVER_CLIENT_ID"]
    NAVER_CLIENT_SECRET = st.secrets["NAVER_CLIENT_SECRET"]
    NAVER_CUSTOMER_ID = str(st.secrets["NAVER_CUSTOMER_ID"])
    OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", "")
except KeyError as e:
    st.error(f"⚠️ Streamlit Secrets 설정에 누락된 항목이 있습니다: {e}")
    st.stop()

# 3. 네이버 검색광고 API 인증 서명(Signature) 생성 함수
def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(int(time.time() * 1000))
    message = f"{timestamp}.{method}.{uri}"
    signature = base64.b64encode(hmac.new(secret_key.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).digest()).decode("utf-8")
    
    return {
        "Content-Type": "application/json",
        "X-Timestamp": timestamp,
        "X-API-KEY": api_key,
        "X-Customer": customer_id,
        "X-Signature": signature
    }

# 4. 네이버 검색광고 API 호출 함수 (파라미터 수정 완료)
def get_naver_keyword_data(hint_keyword):
    BASE_URL = "https://api.searchad.naver.com"
    URI = "/keywordstool"
    METHOD = "GET"
    
    headers = get_header(METHOD, URI, NAVER_CLIENT_ID, NAVER_CLIENT_SECRET, NAVER_CUSTOMER_ID)
    
    # 네이버 API 규격에 맞게 콤마로 분리 및 공백 제거 처리
    clean_keyword = hint_keyword.strip()
    params = {"hintKeywords": clean_keyword, "showDetail": 1}
    
    response = requests.get(BASE_URL + URI, headers=headers, params=params)
    
    if response.status_code == 200:
        return True, response.json().get("keywordList", [])
    else:
        return False, f"Code: {response.status_code}, Message: {response.text}"

# 5. 앱 UI 및 실행 로직
st.subheader("🔍 네이버 연관 키워드 및 검색량 실시간 조회")
keyword_input = st.text_input("분석할 키워드를 입력하세요 (예: 광주 술집, 플레이스최적화 등)")

if st.button("데이터 분석 실행"):
    if keyword_input:
        with st.spinner(f"'{keyword_input}' 키워드 데이터를 네이버에서 불러오는 중입니다..."):
            success, api_data = get_naver_keyword_data(keyword_input)
            
            if success and api_data:
                st.success("데이터 연동 성공! 실시간 네이버 검색광고 통계입니다.")
                
                for item in api_data[:5]:
                    kw = item.get("relKeyword")
                    pc_q = item.get("monthlyPcQcCnt")
                    mo_q = item.get("monthlyMobileQcCnt")
                    comp = item.get("compIdx")
                    
                    pc_cnt = str(pc_q) if isinstance(pc_q, int) else "10 미만"
                    mo_cnt = str(mo_q) if isinstance(mo_q, int) else "10 미만"
                    
                    st.markdown(f"""
                    ---
                    * **연관 키워드:** `{kw}`
                    * **PC 월간검색수:** {pc_cnt}회 | **모바일 월간검색수:** {mo_cnt}회
                    * **경쟁정도:** `{comp}`
                    """)
            else:
                st.error("데이터 연동 실패 원인:")
                st.code(api_data)
    else:
        st.warning("키워드를 먼저 입력해주세요.")
