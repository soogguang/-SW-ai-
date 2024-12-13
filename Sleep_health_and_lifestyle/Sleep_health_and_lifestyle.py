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

# 공간 띄우기
st.write("")
st.write("")

# 숙면을 위한 팁
container = st.container()
container.markdown("---")

st.header(" 숙면하기 위한 스트레스 줄이는 방법 💤")


st.markdown(""" <br>
        <div style="padding: 20px; border-radius: 15px; border: 2px solid #ccc;">
        <h3><b>✅  일관성 갖기</b></h3> 
        휴일에도 빠짐없이 매일 같은 시간에 잠자리에 들고 일어나면 우리 몸이 규칙적인 수면 각성 주기를 강화합니다. 결국 우리 몸은 잠잘 시간을 자동으로 알게 되어 잠들기가 훨씬 쉬워지는데요. 이렇게 습관이 들면 알람이 울리기 전에 몸이 먼저 일어날 시간을 알아 개운하게 일어날 수 있습니다. 이에 일관성을 가지고 수면을 취할 필요가 있습니다.
        <h3><b>✅  잠들기 전 스크린을 피하기</b></h3>
        텔레비전이나 컴퓨터, 태블릿, 휴대폰 스크린 조명은 우리 수면에 엄청난 영향을 미친다는 연구가 많이 있습니다. 스크린에서 나오는 빛은 졸음이 오는 수준을 인공적으로 바꾸고 멜라토닌 수치를 낮춰 잠들기 더 어렵게 하며 수면의 질을 떨어뜨린다고 합니다. 심지어 잠들기 전 텔레비전 시청이나 이메일 확인은 겉보기에 무해한 것 같아도 스크린 조명 때문만이 아니라 그 내용 자체의 자극 때문에 수면에 영향을 미칠 수 있다고 합니다. 우리 뇌는 텔레비전을 끄거나 책을 덮은 후에도 보고 읽은 내용을 계속 처리하기 때문에 편안히 쉬고 잠들기가 어렵습니다. 이에 잠들기 전에 스크린을 보는 것은 숙면을 방해할 수 있으므로 가능한 스크린을 피하는 것이 좋겠습니다.
        <h3><b>✅  취침 의식 만들기</b></h3>
        잠들기 전 간단한 의식을 만들면 우리 뇌와 몸이 긴장을 풀 시간을 알게 하는데 효과적이라고 합니다. 양치나 잠옷 입기처럼 간단해도 좋지만 숙면을 취하는데 문제가 있다면 이 의식에 좀 더 노력을 들여야 합니다. 허브티 마시기나 아로마 오일 바르기, 15~20분 동안 책 읽기(전자책 제외), 혹은 가볍게 그림 그리기도 좋습니다. 오래 걸리지 않는 간단한 과정이지만 긴장 상태와 상관없이 내 몸과 뇌가 잠들 준비를 하기에 충분한 나만의 취침 의식을 만들어 보는 것이 좋습니다.
        <h3><b>✅  정오 이후로 카페인 삼가기</b></h3>
        카페인 과다 복용은 숙면 시간을 단축시키고 자다가 자주 깨게 하여 수면을 방해한다고 합니다. 한 연구에 따르면 소량의 카페인도 수면을 방해할 수 있다고 하며, 취침 전 6시간 이내에 섭취한 카페인이 가장 해롭다고 합니다. 그러므로 오후에는 카페인을 피한다면 전반적인 수면의 질을 향상시킬 수 있습니다.
    </div>
            """, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("출처: [스트레스 해소 방법 - 숙면](http://www.samsunghospital.com/webzine/smcdmedu/279/webzine_279_5.html)")

