import streamlit as st
import urllib.request
import json
import datetime
import hashlib
import hmac
import base64
import re

# 1. 페이지 기본 설정
st.set_page_config(page_title="위드멤버 마케팅 자동화 툴", page_icon="📊", layout="wide")

st.title("위드멤버 마케팅 자동화 및 리포트 툴 🚀")
st.write("네이버 검색광고 API 데이터와 AI를 활용하여 키워드 분석 리포트를 생성합니다.")

# 2. Streamlit Secrets에서 API 키 불러오기
try:
    API_KEY = st.secrets["NAVER_CLIENT_ID"]
    SECRET_KEY = st.secrets["NAVER_CLIENT_SECRET"]
    CUSTOMER_ID = str(st.secrets["NAVER_CUSTOMER_ID"])
except KeyError as e:
    st.error(f"⚠️ Streamlit Secrets 설정에 누락된 항목이 있습니다: {e}")
    st.stop()

# 3. 네이버 API 시그니처 생성
def generate_signature(timestamp, method, uri):
    message = f"{timestamp}.{method}.{uri}"
    hash_val = hmac.new(SECRET_KEY.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).digest()
    return base64.b64encode(hash_val).decode("utf-8")

# 4. 네이버 키워드툴 API 호출 함수 (정제 로직 강화)
def fetch_naver_keywords(keyword):
    method = "GET"
    uri = "/keywordstool"
    timestamp = str(int(datetime.datetime.now().timestamp() * 1000))
    
    signature = generate_signature(timestamp, method, uri)
    
    # 특수문자 및 연속 공백 제거 (네이버 API 규격 에러 방지)
    cleaned_keyword = re.sub(r'[\s]+', ' ', keyword).strip()
    
    encoded_keyword = urllib.parse.quote(cleaned_keyword)
    url = f"https://api.searchad.naver.com{uri}?hintKeywords={encoded_keyword}&showDetail=1"
    
    headers = {
        "X-Timestamp": timestamp,
        "X-API-KEY": API_KEY,
        "X-Customer": CUSTOMER_ID,
        "X-Signature": signature
    }
    
    try:
        req = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return True, data.get("keywordList", [])
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        return False, f"HTTP Error {e.code}: {error_body}"
    except Exception as e:
        return False, str(e)

# 5. 앱 UI 및 실행 로직
st.subheader("🔍 네이버 연관 키워드 및 검색량 실시간 조회")
keyword_input = st.text_input("분석할 키워드를 입력하세요 (예: 광주술집, 플레이스최적화 등 - 띄어쓰기 주의)")

if st.button("데이터 분석 실행"):
    if keyword_input:
        with st.spinner(f"'{keyword_input}' 키워드 데이터를 네이버에서 불러오는 중입니다..."):
            success, result = fetch_naver_keywords(keyword_input)
            
            if success and result:
                st.success("데이터 연동 성공! 실시간 네이버 검색광고 통계입니다.")
                
                for item in result[:10]:
                    kw = item.get("relKeyword")
                    pc_q = item.get("monthlyPcQcCnt")
                    mo_q = item.get("monthlyMobileQcCnt")
                    comp = item.get("compIdx")
                    
                    pc_cnt = str(pc_q) if isinstance(pc_q, (int, float)) and pc_q >= 10 else "10 미만"
                    mo_cnt = str(mo_q) if isinstance(mo_q, (int, float)) and mo_q >= 10 else "10 미만"
                    
                    st.markdown(f"""
                    ---
                    * **연관 키워드:** `{kw}`
                    * **PC 월간검색수:** {pc_cnt}회 | **모바일 월간검색수:** {mo_cnt}회
                    * **경쟁정도:** `{comp}`
                    """)
            else:
                st.error("데이터 연동 실패 원인:")
                st.code(result)
                st.info("💡 Tip: 만약 코드를 고쳐도 이 에러가 지속된다면, 네이버 검색광고 시스템(searchad.naver.com)의 [도구] -> [API 사용 관리] 메뉴에서 '키워드 도구' API 권한이 정상적으로 체크/신청되어 있는지 확인해 주세요.")
    else:
        st.warning("키워드를 먼저 입력해주세요.")
