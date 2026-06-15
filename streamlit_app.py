import streamlit as st

# 1. 초기 변수 설정
appliances = ["냉장고", "오븐", "세탁기"]
danger_temp = 70

# 2. 웹 앱 헤더 및 정보 표시
st.title("🔥 가전제품 화재 위험 예방 시스템")
st.info(f"⚠️ 위험 기준 온도: {danger_temp}°C")
st.markdown("---")

# 3. 온도 입력 폼 (st.form 사용)
with st.form("temp_check_form"):
    st.write("각 가전제품의 현재 온도를 입력해 주세요.")
    
    # 사용자가 입력한 온도를 저장할 딕셔너리
    temps = {}
    
    # 가전제품 리스트를 순회하며 number_input 위젯 생성
    for item in appliances:
        # st.number_input을 통해 숫자(온도) 입력받기
        temps[item] = st.number_input(f"🌡️ {item}의 현재 온도 (°C)", value=25, step=1)
        
    # 상태 확인 버튼
    submitted = st.form_submit_button("상태 확인하기")

# 4. 결과 출력 로직
if submitted:
    st.markdown("### 📊 점검 결과")
    
    for item, temp in temps.items():
        if temp >= danger_temp:
            # 위험 상태일 경우 빨간색 경고창(st.error) 출력
            st.error(f"🚨 **{item}**: {temp}°C - **화재 위험! 즉시 전원 차단!**")
        else:
            # 정상 상태일 경우 초록색 성공창(st.success) 출력
            st.success(f"✅ **{item}**: {temp}°C - 정상 작동 중입니다.")