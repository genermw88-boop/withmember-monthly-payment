import streamlit as st
import urllib.request
import json
import datetime

# 1. 페이지 기본 설정
st.set_page_config(page_title="위드멤버 마케팅 자동화 툴", page_icon="📊", layout="wide")

st.title("위드멤버 마케팅 자동화 및 리포트 툴 🚀")
st.write("네이버 데이터랩 API와 AI를 활용하여 키워드 검색 트렌드를 분석합니다.")

# 2. Streamlit Secrets에서 API 키 불러오기
try:
    CLIENT_ID = st.secrets["NAVER_CLIENT_ID"]
    Client_SECRET = st.secrets["NAVER_CLIENT_SECRET"]
except KeyError as e:
    st.error(f"⚠️ Streamlit Secrets 설정에 누락된 항목이 있습니다: {e}")
    st.stop()

# 3. 네이버 데이터랩 API 호출 함수
def fetch_datalab_trend(keyword):
    url = "https://openapi.naver.com/v1/datalab/search"
    
    # 최근 1년간의 월간 트렌드 분석 설정
    end_date = datetime.date.today().strftime("%Y-%m-%d")
    start_date = (datetime.date.today() - datetime.timedelta(days=365)).strftime("%Y-%m-%d")
    
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "timeUnit": "month",
        "keywordGroups": [
            {
                "groupName": keyword,
                "keywords": [keyword]
            }
        ]
    }
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", Client_SECRET)
    request.add_header("Content-Type", "application/json")
    
    try:
        response = urllib.request.urlopen(request, data=json.dumps(body).encode("utf-8"))
        rescode = response.getcode()
        if rescode == 200:
            result = json.loads(response.read().decode('utf-8'))
            return True, result.get("results", [])
        else:
            return False, f"Error Code: {rescode}"
    except Exception as e:
        return False, str(e)

# 4. 앱 UI 및 실행 로직
st.subheader("📈 네이버 검색 트렌드 분석 (데이터랩)")
keyword_input = st.text_input("분석할 키워드를 입력하세요 (예: 광주 술집, 플레이스최적화 등)")

if st.button("트렌드 분석 실행"):
    if keyword_input:
        with st.spinner(f"'{keyword_input}' 검색 트렌드 데이터를 불러오는 중입니다..."):
            success, results = fetch_datalab_trend(keyword_input.strip())
            
            if success and results:
                st.success("데이터 연동 성공! 최근 1년간 월별 검색 트렌드 비율입니다.")
                data = results[0].get("data", [])
                
                # Streamlit 내장 라인 차트로 트렌드 시각화
                chart_data = {item["period"]: item["ratio"] for item in data}
                st.line_chart(chart_data)
                
                # 상세 데이터 수치 출력
                for item in data:
                    st.markdown(f"- **{item['period']}**: 상대 검색량 지수 `{item['ratio']}`")
            else:
                st.error("데이터 연동 실패 원인:")
                st.code(results)
    else:
        st.warning("키워드를 먼저 입력해주세요.")
