import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="큰 수의 법칙 종합 탐구",
    page_icon="🎲",
    layout="wide"
)

# --- 1. 제목 및 소개 ---
st.title("🎲 큰 수의 법칙: 체험하고 이해하기")
st.markdown("""
'큰 수의 법칙'은 통계학의 가장 기본이 되는 중요한 원리입니다.  
먼저 간단한 주사위 던지기 시뮬레이션으로 이 법칙을 직접 **체험**해보고,  
아래에서 그 원리가 무엇인지 자세히 **이해**해 봅시다.
""")
st.markdown("---")


# --- 2. 체험 시뮬레이션 ---
st.header("1. 주사위 던지기로 '큰 수의 법칙' 체험하기")

# 사용자 입력
col_input1, col_input2 = st.columns([2,1])
with col_input1:
    num_rolls = st.slider(
        "주사위를 몇 번 던져볼까요?",
        min_value=10,
        max_value=10000,
        value=1000,
        step=10,
        help="슬라이더를 오른쪽으로 움직일수록 '큰 수의 법칙'이 뚜렷하게 나타납니다."
    )
with col_input2:
    selected_number = st.selectbox(
        "확률을 추적할 주사위 눈을 선택하세요",
        (1, 2, 3, 4, 5, 6),
        index=5 # 기본값으로 6 선택
    )


# 시뮬레이션 실행 버튼
if st.button("🚀 주사위 던지기 시뮬레이션 시작!"):
    # 1부터 6까지의 정수를 랜덤으로 생성
    rolls = np.random.randint(1, 7, num_rolls)
    
    # --- 라인 차트 데이터 계산 ---
    # 선택한 숫자가 나온 경우를 True(1)로 변환
    is_selected_number = (rolls == selected_number)
    # 누적 합계 계산 (선택한 숫자가 나온 횟수)
    cumulative_counts = np.cumsum(is_selected_number)
    # 각 시행 횟수별로 선택한 숫자가 나온 비율(통계적 확률) 계산
    cumulative_ratio = cumulative_counts / (np.arange(1, num_rolls + 1))
    
    # --- 시각화를 위한 데이터프레임 생성 ---
    line_chart_data = pd.DataFrame({
        '시행 횟수': range(1, num_rolls + 1),
        f'숫자 {selected_number}의 비율': cumulative_ratio
    })
    
    # --- 막대 차트 데이터 계산 ---
    unique, counts = np.unique(rolls, return_counts=True)
    bar_chart_data = pd.DataFrame(counts, index=[f"{i}번" for i in unique], columns=["횟수"])


    # --- 결과 시각화 ---
    st.subheader("📊 시뮬레이션 결과")
    
    # 라인 차트
    st.write(f"### 시행 횟수에 따른 '숫자 {selected_number}의 비율' 변화")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(line_chart_data['시행 횟수'], line_chart_data[f'숫자 {selected_number}의 비율'])
    ax.axhline(y=1/6, color='r', linestyle='--', label='수학적 확률 (1/6 ≈ 16.7%)')
    ax.set_xlabel('시행 횟수')
    ax.set_ylabel('선택한 숫자가 나온 비율')
    ax.set_ylim(0, 1) # y축 범위를 0과 1 사이로 고정
    ax.legend()
    st.pyplot(fig)
    st.info(f"""
    **그래프 해석:** 처음에는 숫자 **{selected_number}**의 비율이 매우 불규칙하게 움직입니다.  
    하지만 **시행 횟수가 늘어날수록(그래프가 오른쪽으로 갈수록)**, 비율이 점점 **수학적 확률인 1/6 (약 16.7%)** 선에 안정적으로 수렴하는 것을 볼 수 있습니다.
    """)

    # 막대 차트
    st.write("### 최종 각 눈이 나온 횟수 분포")
    st.bar_chart(bar_chart_data)
    st.info("시행 횟수가 충분히 크다면, 각 눈이 나온 횟수(막대그래프의 높이)가 거의 비슷해지는 것을 확인할 수 있습니다.")

else:
    st.info("슬라이더와 선택상자로 조건을 조절하고 버튼을 눌러 시뮬레이션을 시작하세요.")

st.markdown("\n\n---")


# --- 3. 개념 설명 ---
st.header("2. 큰 수의 법칙, 원리 파헤치기")

st.error("""
**"주사위를 6번 던졌는데 '6'이 한 번도 안 나왔다. 이 주사위는 불량품이 아닐까?"**
""")
st.write("""
위 시뮬레이션에서 보았듯이, 적은 횟수의 시도에서는 이런 일이 흔하게 발생합니다.  
'큰 수의 법칙'은 이처럼 **단기적인 우연**과 **장기적인 예측** 사이의 관계를 설명해주는 매우 중요한 통계 원리입니다.
""")

st.subheader("🤔 세상에는 두 가지 확률이 있다?")
col_exp1, col_exp2 = st.columns(2)
with col_exp1:
    st.info("""
    #### ① 수학적 확률 (이상)
    머릿속으로 계산한 **완벽하고 이상적인 확률**입니다.
    -   **예시:** 완벽한 주사위의 각 눈이 나올 확률은 항상 **1/6** 입니다.
    -   **특징:** 변하지 않고, 이론적으로 완벽합니다.
    """)

with col_exp2:
    st.warning("""
    #### ② 통계적 확률 (현실)
    실제로 여러 번 실험해서 얻은 **현실적인 결과값**입니다.
    -   **예시:** 주사위를 6번 던졌더니 '3'은 한 번도 안 나오고 '5'가 두 번 나올 수 있습니다.
    -   **특징:** 실행할 때마다 결과가 바뀌며, 예측하기 어렵습니다.
    """)

st.subheader("🌉 두 확률을 이어주는 다리: 큰 수의 법칙")
st.success(
    "**\"시행 횟수를 아주 많이 늘리면, 통계적 확률은 결국 수학적 확률에 놀랍도록 가까워진다.\"**"
)
st.write("바로 위에서 여러분이 직접 체험한 현상입니다!")

st.subheader("🏢 그래서 이게 왜 중요할까? (실생활 예시)")
st.markdown("큰 수의 법칙은 카지노, 보험, 여론조사 등 **거대한 불확실성을 다루는 모든 산업의 핵심 원리**입니다.")

col_exp3, col_exp4 = st.columns(2)
with col_exp3:
    st.markdown("""
    ##### 🎰 카지노는 어떻게 돈을 벌까?
    카지노는 단 한 명의 손님이 돈을 딸지 잃을지는 전혀 예측할 수 없습니다.  
    하지만 **수백만 번의 게임**이 진행되면, 미세한 확률적 우위 덕분에 **결과적으로는 반드시 돈을 벌게 된다는 사실**을 '큰 수의 법칙'을 통해 알고 있습니다.
    """)
with col_exp4:
    st.markdown("""
    ##### 📋 보험회사는 어떻게 보험료를 정할까?
    보험회사는 특정 고객 한 명이 올해 사고를 당할지 아닐지는 전혀 예측할 수 없습니다.  
    하지만 **수백만 명의 고객 데이터**를 분석하면, 특정 연령대의 사람들이 1년에 몇 % 정도 사고를 당하는지를 매우 정확하게 예측할 수 있습니다. 이를 이용해 손해 보지 않을 만큼의 보험료를 책정합니다.
    """)

st.balloons()