from PIL import Image
import streamlit as st

# 스크린샷 이미지 파일을 대시보드에 표시
image = Image.open("Sleep_health_and_lifestyle/pages/Notebooks.pdf")
st.image(image, caption="숙면을 위한 팁", use_column_width=True)
