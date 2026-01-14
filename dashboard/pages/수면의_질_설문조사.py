import streamlit as st
import pandas as pd
import joblib

# =========================
# 모델 로드
# =========================
@st.cache_resource
def load_model():
    return joblib.load("dashboard/sleep_quality_model.pkl")

model = load_model()

# =========================
# 페이지 제목
# =========================
st.title("생활습관 기반 수면 질 예측 설문")
st.write("아래 설문을 입력하면 수면의 질 저하 가능성을 예측합니다")

st.divider()

# =========================
# 설문 입력
# =========================
age = st.number_input("나이", min_value=18, max_value=80, value=30)

sleep_duration = st.slider(
    "평균 수면 시간 (시간)",
    min_value=3.0,
    max_value=10.0,
    value=7.0,
    step=0.5
)

activity = st.slider(
    "신체 활동 수준",
    min_value=0,
    max_value=100,
    value=50
)

stress = st.slider(
    "스트레스 수준 (1~10)",
    min_value=1,
    max_value=10,
    value=5
)

heart_rate = st.number_input(
    "평균 심박수 (bpm)",
    min_value=40,
    max_value=120,
    value=70
)

steps = st.number_input(
    "하루 평균 걸음 수",
    min_value=0,
    max_value=30000,
    value=8000
)

# =========================
# 입력 데이터 → DataFrame
# (컬럼명 반드시 학습 때와 동일)
# =========================
input_df = pd.DataFrame([{
    "Age": age,
    "Sleep Duration": sleep_duration,
    "Physical Activity Level": activity,
    "Stress Level": stress,
    "Heart Rate": heart_rate,
    "Daily Steps": steps
}])

st.divider()

# =========================
# 예측 버튼
# =========================
if st.button("수면 질 예측"):
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.subheader("예측 결과")

    if pred == 1:
        st.error(
            f"생활 습관으로 인해 수면의 질이 나쁠 가능성이 높습니다\n\n"
            f"예상 위험도: {prob:.1%}"
        )
    else:
        st.success(
            f"현재 생활 습관은 비교적 양호합니다\n\n"
            f"예상 위험도: {prob:.1%}"
        )

    st.caption(
        "본 결과는 머신러닝 모델의 예측 결과이며 "
        "의료적 진단을 대체하지 않습니다"
    )
