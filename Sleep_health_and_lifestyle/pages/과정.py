import streamlit as st

# 이미지 파일 경로
image_path = "/Users/jangsooin/Library/Mobile Documents/com~apple~CloudDocs/숭실대학교/숭실대학교(1-2)/AI와데이터기초/프로젝트/pages/Notebooks_page.jpg"  # 실제 이미지 파일 경로를 입력하세요.

# 이미지 표시
st.image(image_path, caption="Smart Bug Trap 이미지", use_container_width=True)
