import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import streamlit.components.v1 as components
import plotly.express as px


# Streamlit 페이지 설정
st.set_page_config(page_title="수면 건강 및 라이프스타일 데이터셋 정리", layout="wide", menu_items={
         'About': """# AI와데이터기초 프로젝트   
         AI융합학부 
         김지율 장수인 최희우"""
     })
st.title("수면 건강 및 라이프스타일 데이터셋 📊")


# 동기
st.markdown("""수면 질은 건강에 많은 영향을 미칩니다.<br>
            수면의 질을 높이기 위하여 어떤 요소가 영향을 미치는 지를 데이터들을 정리해서 알아내는 작업은 꼭 필요하다고 생각했습니다."""
            ,unsafe_allow_html=True)
st.markdown("""일단 Quality of Sleep에 따른 다른 요소들의 데이터의 평균을 구해보았습니다.""")


# 공간 띄우기
st.write("")
st.write("")
st.write("")

# 데이터 로드
data = pd.read_csv("Sleep_health_and_lifestyle/Sleep_health_and_lifestyle_dataset.csv")


# 'Quality of Sleep'에 따라 평균값을 계산
average_values = data.groupby('Quality of Sleep').mean()

# 중요한 열을 강조하기 위한 색상 설정
def highlight_columns(s):
    color = 'background-color: #99CCFF'
    return [color if col in important_columns else '' for col in s.index]

# 강조할 열 설정
important_columns = ['Sleep Duration', 'Stress Level', 'Heart Rate']  

# 데이터프레임에 스타일 적용
average_values = average_values.style.apply(highlight_columns, axis=1)

# 평균 낸 표
st.subheader(" Quality of Sleep에 따른 평균 값 😪")
st.write(average_values)


st.markdown("""같은 Quality of sleep 값에 따라 칼럼값의 평균을 구했고 그에 따라 각각의 관계가 존재함을 알아내었습니다.""") 
st.markdown("""특히 **'Sleep** **Duration',** **'Stress** **Level',** **'Heart** **Rate'** 의 평균값들이 Quality of sleep과 눈에 띄는 관계를 보였습니다.""")
st.write("")
st.write("")
st.write("")



# 수면시간과 수면의 질의 상관관계 Part
# 박스 플롯
fig = px.box(
    data,
    x='Quality of Sleep',  # 수면 품질을 x축에 배치
    y='Sleep Duration',    # 수면 시간을 y축에 배치
    color='Quality of Sleep',  # 수면 품질에 따라 색상 구분
    points='all',  # 데이터 포인트를 모두 표시
    title='Distribution of Sleep Duration by Quality of Sleep',
    labels={
        'Quality of Sleep': 'Quality of Sleep',
        'Sleep Duration': 'Sleep Duration (hours)'
    }
)

fig.update_layout(
    title_font={'size': 25},
    xaxis_title='Quality of Sleep',
    yaxis_title='Sleep Duration (hours)'
)

#fig.show()

# 타이틀
st.subheader('Quality of Sleep과 Sleep Duration 분석 🌀')
st.markdown('수면 시간과 수면의 질의 상관관계를 구합니다.')

st.plotly_chart(fig)

#설명글
st.markdown('''수면 시간이 너무 짧거나 지나치게 길면 수면의 질이 떨어질 수 있다는 패턴이 있습니다.<br>
            또한, 수면 시간이 7-9시간일 때 수면의 질이 높음을 알 수 있습니다.<br>
            그러므로 수면 시간과 수면의 질이 상관관계가 있다는 것을 알 수 있습니다.'''
            , unsafe_allow_html=True)


# 공간 띄우기
st.write("")
st.write("")
st.write("")


# 스트레스 수준, 수면 시간, 심박수에 따른 수면의 질 산점도 Part
def plot_scatter(x, y='Quality of Sleep', xlabel='', ylabel='Quality of Sleep'):
    plt.figure(figsize=(6, 2))
    sns.scatterplot(x=x, y=y, data=data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f'{ylabel} by {xlabel}')
    st.pyplot(plt)


# 스트레스 수준에 따른 수면의 질
st.subheader(" Stress Level과 Quality of Sleep의 관계 💢")
plot_scatter('Stress Level', xlabel='Stress Level')

# 공간 띄우기
st.write("")
st.write("")
st.write("")

# 심박수에 따른 수면의 질
st.subheader(" Heart Rate과 Quality of Sleep의 관계 ❤️‍🔥")
plot_scatter('Heart Rate', xlabel='Heart Rate (bpm)')

# 공간 띄우기
st.write("")
st.write("")
st.write("")

# 서브헤더
st.subheader(" 요인별 Quality of Sleep의 결합 산점도 ➕") 

# 수면의 질 상위 그룹 필터링
high_quality_sleep = data[data['Quality of Sleep'] >= 9]  # 수면의 질이 높은 그룹 (예: 4 이상)

# 결측값 처리 (예: 제거)
data = data.dropna()

# 'Heart Rate' 값을 10으로 나누어 축소
data['Normalized Heart Rate'] = data['Heart Rate'] / 15


# 그래프 생성: 수면의 질과 세 가지 요인 (Stress Level, Sleep Duration, Normalized Heart Rate)
def plot_combined_scatter():
    plt.figure(figsize=(6, 2))

    # 각 요인의 산점도를 동일한 그래프에 그림
    sns.scatterplot(x='Stress Level', y='Quality of Sleep', data=data, color='blue', label='Stress Level')
    sns.scatterplot(x='Sleep Duration', y='Quality of Sleep', data=data, color='green', label='Sleep Duration')
    sns.scatterplot(x='Normalized Heart Rate', y='Quality of Sleep', data=data, color='red', label='Heart Rate (Normalized)')
    
    plt.xlabel('Factors (Stress Level, Sleep Duration, Normalized Heart Rate)')
    plt.ylabel('Quality of Sleep')
    plt.title('Combined Scatter Plot of Sleep Quality by Factors')
    plt.legend()
    st.pyplot(plt)
    plt.clf()  # 그래프를 출력한 후 클리어

    # 'count', 'mean', 'std'를 제외하고 수면의 질이 높은 그룹의 특징 요약
    high_quality_summary = high_quality_sleep[['Stress Level', 'Sleep Duration', 'Heart Rate', 'Quality of Sleep']].describe().drop(['count', 'mean', 'std'])

    # Streamlit에 테이블 형식으로 출력
    st.write("")
    st.write("")
    st.write("")
    st.subheader(" Quality of Sleep이 높은 개인의 특징 🥰")
    st.write(high_quality_summary)

# 그래프 그리기 함수 호출
plot_combined_scatter()



# 숙면을 위한 팁
container = st.container()
container.markdown("---")

st.header(" 숙면하기 위한 스트레스 줄이는 방법 💤")
st.write("")
st.write("")

iframe_url = "http://www.samsunghospital.com/webzine/smcdmedu/279/webzine_279_5.html"
components.iframe(iframe_url, height=1000, width=1050)


