import streamlit as st

st.set_page_config(layout="wide")

# 이미지 파일 경로
image_path = "Sleep_health_and_lifestyle/pages/Notebooks_page.jpg" 

# 이미지 표시
st.image(image_path, caption="colab 화면 이미지", use_container_width=True)
