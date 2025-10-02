

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
