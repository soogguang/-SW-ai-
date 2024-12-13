import streamlit as st

st.set_page_config(layout="wide")

# 이미지 파일 경로
image_path = "Sleep_health_and_lifestyle/pages/Notebooks_page.jpg"  # 실제 이미지 파일 경로를 입력하세요.

# 이미지 표시
st.image(image_path, caption="Smart Bug Trap 이미지", use_container_width=True)
