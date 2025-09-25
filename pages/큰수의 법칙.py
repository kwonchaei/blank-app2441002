

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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Matplotlib 스타일 설정
plt.style.use('ggplot')
plt.rcParams['font.family'] = 'AppleGothic' if 'darwin' in __import__('sys').platform else 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False # 마이너스 폰트 깨짐 방지

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="중심 극한 정리 시뮬레이터",
    page_icon="🔔",
    layout="wide"
)

# --- 제목 및 설명 ---
st.title("🔔 중심 극한 정리 (Central Limit Theorem) 시뮬레이터")
st.markdown("""
'큰 수의 법칙'이 표본의 크기가 커질수록 **하나의 표본 평균**이 모집단 평균에 가까워지는 것을 보여줬다면,  
**중심 극한 정리**는 여기서 한 걸음 더 나아갑니다.

> 모집단이 어떤 분포를 따르든, **표본의 크기(Sample Size)가 충분히 크다면**, 여러 번 추출한 **표본 평균들의 분포**는 **정규분포(종 모양🔔)를 따른다**는 놀라운 정리입니다.

아래에서 모집단의 분포와 표본의 크기를 바꿔가며 직접 확인해보세요!
""")
st.markdown("---")

# --- 사용자 입력 (사이드바) ---
st.sidebar.header("⚙️ 실험 조건 설정")

population_dist = st.sidebar.selectbox(
    "1. 분석할 모집단의 분포를 선택하세요",
    ("균등 분포 (Uniform)", "편향된 분포 (Skewed)", "쌍봉 분포 (Bimodal)")
)

sample_size = st.sidebar.slider(
    "2. 각 표본의 크기 (Sample Size)를 조절하세요",
    min_value=1,
    max_value=200,
    value=30, # 기본값
    help="한 번에 몇 개의 데이터를 뽑을지 결정합니다. 이 값이 커질수록 마법이 일어납니다!"
)

num_samples = st.sidebar.slider(
    "3. 표본 추출 횟수를 조절하세요",
    min_value=100,
    max_value=10000,
    value=1000, # 기본값
    help="표본 추출을 몇 번 반복할지 결정합니다."
)

# --- 모집단 데이터 생성 ---
if population_dist == "균등 분포 (Uniform)":
    # 0과 1 사이의 숫자가 모두 같은 확률로 나옴
    population = np.random.uniform(0, 1, 100000)
    pop_mean = np.mean(population)
    pop_std = np.std(population)
elif population_dist == "편향된 분포 (Skewed)":
    # 오른쪽으로 긴 꼬리를 가진 분포 (Beta 분포 활용)
    population = np.random.beta(a=2, b=8, size=100000) * 10
    pop_mean = np.mean(population)
    pop_std = np.std(population)
else: # 쌍봉 분포 (Bimodal)
    # 두 개의 정규분포를 합쳐서 봉우리가 두 개인 분포 생성
    pop1 = np.random.normal(loc=2, scale=1, size=50000)
    pop2 = np.random.normal(loc=8, scale=1, size=50000)
    population = np.concatenate([pop1, pop2])
    pop_mean = np.mean(population)
    pop_std = np.std(population)


# --- 표본 추출 및 평균 계산 ---
sample_means = []
for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(np.mean(sample))

# --- 결과 시각화 ---
st.header("📊 시뮬레이션 결과")
col1, col2 = st.columns(2)

# 1. 모집단 분포 그래프
with col1:
    st.subheader(f"1. 모집단 분포 ({population_dist})")
    fig1, ax1 = plt.subplots()
    sns.histplot(population, bins=50, kde=True, ax=ax1)
    ax1.axvline(pop_mean, color='red', linestyle='--', label=f'모평균: {pop_mean:.2f}')
    ax1.set_title("모집단 데이터의 분포")
    ax1.legend()
    st.pyplot(fig1)

# 2. 표본 평균의 분포 그래프
with col2:
    st.subheader("2. 표본 평균의 분포 (Distribution of Sample Means)")
    fig2, ax2 = plt.subplots()
    sns.histplot(sample_means, bins=50, kde=True, ax=ax2)
    mean_of_means = np.mean(sample_means)
    ax2.axvline(mean_of_means, color='red', linestyle='--', label=f'표본 평균의 평균: {mean_of_means:.2f}')
    ax2.set_title(f"표본 크기={sample_size}일 때의 표본 평균 분포")
    ax2.legend()
    st.pyplot(fig2)

# --- 결론 ---
st.markdown("---")
st.success(f"""
**결과 해석:**
- **왼쪽**은 우리가 데이터를 추출하는 전체 **모집단**의 모습입니다. 선택에 따라 모양이 제각각입니다.
- **오른쪽**이 바로 **표본 평균들이 모여서 만든 분포**입니다.
- **표본의 크기(Sample Size) 슬라이더**를 오른쪽으로 움직여보세요. 모집단 모양과 상관없이 오른쪽 그래프가 점점 아름다운 **종 모양(정규분포)**으로 변하는 것을 볼 수 있습니다. 이것이 바로 **중심 극한 정리**의 힘입니다!
""")
