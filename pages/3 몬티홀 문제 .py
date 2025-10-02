import streamlit as st
import random
import pandas as pd

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="몬티 홀 문제 시뮬레이터",
    page_icon="🧠"
)

# --- 제목과 설명 ---
st.title("🧠 몬티 홀 문제 시뮬레이터")
st.markdown("""
세 개의 문 뒤에는 **자동차 🚗** 한 대와 **염소 🐐** 두 마리가 있습니다.
1.  당신이 문 하나를 선택합니다.
2.  정답을 아는 진행자가 남은 문 중에서 염소가 있는 문을 열어 보여줍니다.
3.  이제 당신에게 마지막 기회가 주어집니다. 처음 선택을 **유지**하시겠습니까, 아니면 남은 문으로 **바꾸**시겠습니까?

이 시뮬레이터는 수많은 게임을 대신 플레이하여 어떤 전략이 자동차를 얻을 확률이 더 높은지 보여줍니다!
""")

# --- 사용자 입력 (사이드바) ---
st.sidebar.header("🕹️ 게임 설정")
num_simulations = st.sidebar.number_input(
    label="시뮬레이션 횟수를 입력하세요",
    min_value=100,
    max_value=100000,
    value=1000, # 기본값
    step=100
)

# --- 시뮬레이션 함수 ---
def run_simulation(strategy_to_switch):
    wins = 0
    for _ in range(num_simulations):
        doors = [1, 2, 3]
        car_door = 1 # 자동차는 항상 1번에 있다고 가정
        player_choice = random.choice(doors)
        doors_to_open = [door for door in doors if door != car_door and door != player_choice]
        opened_door = random.choice(doors_to_open)
        if strategy_to_switch:
            final_choice = [door for door in doors if door != player_choice and door != opened_door][0]
        else:
            final_choice = player_choice
        if final_choice == car_door:
            wins += 1
    return wins

# --- 실행 버튼 ---
if st.button("🚀 시뮬레이션 시작!"):
    stay_wins = run_simulation(strategy_to_switch=False)
    switch_wins = run_simulation(strategy_to_switch=True)
    st.header("📊 시뮬레이션 결과")
    results_df = pd.DataFrame({
        '전략': ['선택을 유지하기', '선택을 바꾸기'],
        '승리 횟수': [stay_wins, switch_wins]
    }).set_index('전략')
    stay_win_rate = round((stay_wins / num_simulations) * 100, 2)
    switch_win_rate = round((switch_wins / num_simulations) * 100, 2)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("선택을 유지했을 때")
        st.metric(label="🏆 승률", value=f"{stay_win_rate}%")
        st.write(f"({num_simulations}번 중 {stay_wins}번 승리)")
    with col2:
        st.subheader("선택을 바꿨을 때")
        st.metric(label="🏆 승률", value=f"{switch_win_rate}%")
        st.write(f"({num_simulations}번 중 {switch_wins}번 승리)")
    st.subheader("📈 전체 결과 비교")
    st.bar_chart(results_df)
    st.info("결과가 놀랍지 않나요? 선택을 바꾸는 것이 승리할 확률이 약 **두 배**나 높습니다!")
else:
    st.info("게임 횟수를 설정하고 '시뮬레이션 시작' 버튼을 눌러 결과를 확인해보세요.")