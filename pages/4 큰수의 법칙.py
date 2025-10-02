

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# NanumGothic-Regular.ttf 경로 지정
FONT_PATH = os.path.join("fonts", "NanumGothic-Regular.ttf")
if os.path.exists(FONT_PATH):
    fontprop = fm.FontProperties(fname=FONT_PATH)
    plt.rcParams['font.family'] = fontprop.get_name()
    st.markdown(
        f"""
        <style>
        @font-face {{
            font-family: 'NanumGothic';
            src: url('fonts/NanumGothic-Regular.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }}
        html, body, [class*="css"]  {{
            font-family: 'NanumGothic', sans-serif;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


import streamlit as st
import pandas as pd
import random
import time

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="주사위 확률 시뮬레이터",
    page_icon="🎲"
)

# --- 제목과 설명 ---
st.title("🎲 주사위 확률 시뮬레이터")
st.markdown("""
이 앱은 **큰 수의 법칙**을 시각적으로 보여주는 도구입니다.  
주사위를 던지는 횟수를 늘릴수록 각 눈이 나올 확률이 수학적 확률인 **1/6 (약 16.7%)**에
가까워지는 현상을 직접 확인해보세요!
""")

# --- 사용자 입력 ---
st.sidebar.header("⚙️ 실험 조건 설정")
number_of_rolls = st.sidebar.number_input(
    label="주사위를 몇 번 던질까요?",
    min_value=10,
    max_value=1000000,
    value=100, # 기본값
    step=10,
    help="10부터 1,000,000까지 숫자를 입력할 수 있어요."
)

# '실험 시작' 버튼
if st.sidebar.button("🚀 실험 시작!"):
    # --- 시뮬레이션 로직 ---
    results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    # 진행 상황 바
    progress_bar = st.progress(0, text="주사위를 던지는 중...")

    for i in range(number_of_rolls):
        roll = random.randint(1, 6)
        results[roll] += 1
        
        # 진행 상황 업데이트 (너무 자주 업데이트하면 느려지므로 100번에 한 번씩)
        if (i + 1) % 100 == 0 or i == number_of_rolls - 1:
            progress_bar.progress((i + 1) / number_of_rolls, text=f"주사위를 던지는 중... ({i+1}/{number_of_rolls})")

    progress_bar.empty() # 진행 완료 후 바 숨기기

    # --- 결과 분석 및 표시 ---
    st.header("📊 실험 결과")

    # 데이터 프레임으로 변환
    results_df = pd.DataFrame(
        list(results.values()),
        index=[f"{i}번" for i in results.keys()],
        columns=["횟수"]
    )

    # 결과를 2개의 컬럼으로 나누어 보여주기
    col1, col2 = st.columns([1, 1.5]) # 컬럼 비율 조절

    with col1:
        st.subheader("🔢 횟수 및 확률")
        # 각 눈이 나온 확률 계산
        results_df['확률 (%)'] = round((results_df['횟수'] / number_of_rolls) * 100, 2)
        st.dataframe(results_df)

    with col2:
        st.subheader("📈 그래프")
        st.bar_chart(results_df["횟수"])

    st.success(f"총 {number_of_rolls}번의 주사위 던지기 실험이 완료되었습니다!")

else:
    st.info("왼쪽 사이드바에서 던질 횟수를 설정하고 '실험 시작' 버튼을 눌러주세요.")

    import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="큰 수의 법칙의 비밀",
    page_icon="🎲",
    layout="wide"
)

# --- 1. 제목 및 핵심 질문 ---
st.title("🎲 큰 수의 법칙, 왜 중요할까요?")
st.markdown("---")
st.error("""
**"동전을 10번 던졌는데 앞면이 7번 나왔다. 혹시 이 동전, 뭔가 속임수가 있는 건 아닐까?"**
""")
st.write("""
우리는 동전의 앞면이 나올 확률이 1/2(50%)라고 알고 있지만, 실제로는 이런 일이 흔하게 발생합니다.  
'큰 수의 법칙'은 이처럼 **단기적인 우연**과 **장기적인 예측** 사이의 관계를 설명해주는 매우 중요한 통계 원리입니다.
""")
st.markdown("---")


# --- 2. 두 가지 확률 ---
st.header("🤔 세상에는 두 가지 확률이 있다?")
st.markdown("큰 수의 법칙을 이해하려면, 먼저 두 가지 확률의 개념을 구분해야 합니다.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("① 수학적 확률 (이상)")
    st.info("""
    머릿속으로 계산한 **완벽하고 이상적인 확률**입니다.
    -   **예시:** 완벽한 주사위의 각 눈이 나올 확률은 항상 **1/6** 입니다.
    -   **특징:** 변하지 않고, 이론적으로 완벽합니다.
    """)

with col2:
    st.subheader("② 통계적 확률 (현실)")
    st.warning("""
    실제로 여러 번 실험해서 얻은 **현실적인 결과값**입니다.
    -   **예시:** 주사위를 6번 던졌더니 '3'은 한 번도 안 나오고 '5'가 두 번 나올 수 있습니다.
    -   **특징:** 실행할 때마다 결과가 바뀌며, 예측하기 어렵습니다.
    """)
st.markdown("---")


# --- 3. 큰 수의 법칙 설명 ---
st.header("🌉 두 확률을 이어주는 다리: 큰 수의 법칙")
st.markdown("""
그렇다면 서로 달라 보이는 이 두 확률은 아무 관계가 없는 걸까요? 그렇지 않습니다.  
**큰 수의 법칙(Law of Large Numbers)**은 이 둘을 강력하게 연결해 줍니다.

> **"시행 횟수를 아주 많이 늘리면, 통계적 확률은 결국 수학적 확률에 놀랍도록 가까워진다."**
""")

st.subheader("동전 던지기로 예를 들어봅시다 (앞면이 나올 확률)")
st.code("""
- 10번 던지기:  앞면 7번  (통계적 확률: 70%)  -> 수학적 확률(50%)과 차이가 크다.
- 100번 던지기: 앞면 54번 (통계적 확률: 54%)  -> 차이가 조금 줄어들었다.
- 10,000번 던지기: 앞면 5,021번 (통계적 확률: 50.21%) -> 거의 비슷해졌다!
- 1,000,000번 던지기: 앞면 500,150번 (통계적 확률: 50.015%) -> 소름 돋을 정도로 가까워졌다!
""")
st.success("이처럼 시행 횟수(표본 크기)가 **'충분히 크다면'**, 우리는 현실의 불확실한 결과 속에서도 수학적인 예측을 신뢰할 수 있게 됩니다.")
st.markdown("---")


# --- 4. 실생활 예시 ---
st.header("🏢 그래서 이게 왜 중요할까? (실생활 예시)")
st.markdown("""
큰 수의 법칙은 카지노, 보험, 여론조사 등 **거대한 불확실성을 다루는 모든 산업의 핵심 원리**입니다.
""")

col3, col4 = st.columns(2)
with col3:
    st.subheader("🎰 카지노는 어떻게 돈을 벌까?")
    st.write("""
    카지노는 룰렛 게임에서 단 한 명의 손님이 돈을 딸지 잃을지는 전혀 예측할 수 없습니다. (적은 시행 횟수)
    
    하지만 카지노는 **수백만 번의 게임**이 진행되면, 미세한 확률적 우위(예: 룰렛의 '0') 덕분에 **결과적으로는 반드시 돈을 벌게 된다는 사실**을 '큰 수의 법칙'을 통해 알고 있습니다. 장기적으로는 절대 손해 보지 않는 구조입니다.
    """)
with col4:
    st.subheader("📋 보험회사는 어떻게 보험료를 정할까?")
    st.write("""
    보험회사는 특정 고객 한 명이 올해 암에 걸릴지 아닐지는 전혀 예측할 수 없습니다.
    
    하지만 **수백만 명의 고객 데이터**를 분석하면, 특정 연령대의 사람들이 1년에 몇 % 정도 암에 걸리는지를 매우 정확하게 예측할 수 있습니다. 보험회사는 이 '큰 수의 법칙'에 기반한 통계적 확률을 이용해 손해 보지 않을 만큼의 보험료를 책정합니다.
    """)

st.balloons()
