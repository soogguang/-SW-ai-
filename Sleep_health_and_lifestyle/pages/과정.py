import streamlit as st

pdf_path = "Sleep_health_and_lifestyle/pages/Notebooks.pdf"
with open(pdf_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

st.download_button(label="Download PDF", data=pdf_bytes, file_name="Notebooks.pdf")
st.markdown(f'<iframe src="{pdf_path}" width="700" height="900"></iframe>', unsafe_allow_html=True)
