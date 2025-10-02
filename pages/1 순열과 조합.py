import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="순열과 조합이란?",
    page_icon="🤔",
    layout="wide"
)

# --- 1. 메인 타이틀 및 도입 질문 ---
st.title("🤔 순열과 조합, 언제 어떻게 다를까?")
st.markdown("---")
st.info("""
**"4명 중에 2명을 뽑는다"**는 똑같은 상황인데, 왜 어떨 때는 **순열**을 쓰고, 어떨 때는 **조합**을 쓸까요?  
두 개념의 결정적인 차이는 바로 **'순서' 또는 '자리'의 중요성**에 있습니다. 이 페이지에서 그 차이를 확실하게 알아봅시다!
""")

# --- 2. 개념 비교 ---
st.header("🥇 순열 vs 🤝 조합: 핵심 개념 비교")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🥇 순열 (Permutation)")
    st.markdown("""
    -   **정의:** 서로 다른 n개에서 **순서를 생각하며** r개를 뽑아 나열하는 경우의 수.
    -   **핵심:** 뽑은 다음에 **'자리'를 지정**하거나 **'역할을 부여'**하는 것과 같습니다.
    -   **결과:** `(A, B)`와 `(B, A)`는 **서로 다른 경우**로 취급됩니다.
    -   **키워드:** `줄 세우기`, `배열하기`, `회장/부회장 뽑기`, `이어달리기 순서 정하기`, `비밀번호 만들기`
    """)

with col2:
    st.subheader("🤝 조합 (Combination)")
    st.markdown("""
    -   **정의:** 서로 다른 n개에서 **순서에 상관없이** r개를 뽑는 경우의 수.
    -   **핵심:** 그냥 **'그룹'**이나 **'팀'을 구성**하기만 하면 끝입니다.
    -   **결과:** `{A, B}`와 `{B, A}`는 **완전히 같은 경우**로 취급됩니다.
    -   **키워드:** `대표 뽑기`, `선발하기`, `청소 당번 뽑기`, `팀 구성하기`, `과일 바구니 만들기`
    """)
st.markdown("---")

# --- 3. 시나리오로 이해하기 ---
st.header("💼 시나리오로 배우는 순열과 조합")
st.markdown("네 명의 친구 **A, B, C, D**가 있다고 상상해봅시다. 이 중에서 **2명**을 뽑는 상황입니다.")

# 시나리오 1: 순열
st.subheader("상황 1: 반장과 부반장을 한 명씩 뽑는 경우 (순열)")
st.write("""
이 경우는 **'반장'**이라는 자리와 **'부반장'**이라는 자리가 서로 다르기 때문에 순서가 중요합니다.
-   A가 반장, B가 부반장인 경우 `(A, B)`
-   B가 반장, A가 부반장인 경우 `(B, A)`

이 두 가지는 명백히 **다른 결과**입니다. 따라서 모든 경우의 수를 나열해보면 다음과 같이 총 **12가지**가 나옵니다.
""")
st.code("""
(A, B), (A, C), (A, D)
(B, A), (B, C), (B, D)
(C, A), (C, B), (C, D)
(D, A), (D, B), (D, C)
""")
st.success("계산: **4P2** = 4 × 3 = **12**")

# 시나리오 2: 조합
st.subheader("상황 2: 교실 청소를 할 대표 2명을 뽑는 경우 (조합)")
st.write("""
이 경우는 두 명 모두 **'대표'**라는 동등한 자격이므로 순서가 중요하지 않습니다.
-   A와 B가 대표로 뽑힌 경우 `{A, B}`
-   B와 A가 대표로 뽑힌 경우 `{B, A}`

이 두 가지는 결국 **'A와 B가 청소한다'**는 동일한 결과입니다. 따라서 순열의 결과에서 중복되는 경우를 제거하면 다음과 같이 총 **6가지**가 나옵니다.
""")
st.code("""
{A, B}, {A, C}, {A, D}
{B, C}, {B, D}
{C, D}
""")
st.success("계산: **4C2** = (4 × 3) / (2 × 1) = **6**")
st.markdown("---")

# --- 4. 개념 확인 퀴즈 ---
st.header("✅ 개념 확인 퀴즈")
st.write("다음 상황은 순열과 조합 중 무엇을 사용해야 할까요? 체크해보세요.")

# 퀴즈 데이터 (문제, 순열 체크 여부, 조합 체크 여부, 해설)
quiz_data = [
    ("10명의 학생 중 3명을 뽑아 이어달리기 순서를 정하는 경우", False, False, "이어달리기는 1번, 2번, 3번 주자의 순서가 중요하므로 **순열**입니다."),
    ("서로 다른 7종류의 꽃 중에서 3종류를 뽑아 꽃다발을 만드는 경우", False, False, "꽃다발에 들어가는 꽃의 순서는 중요하지 않으므로 **조합**입니다."),
    ("5개의 숫자 카드(1,2,3,4,5)로 만들 수 있는 세 자리 자연수의 개수", False, False, "123과 321이 다른 수이듯이, 숫자의 자리가 중요하므로 **순열**입니다."),
    ("축구팀 선수 11명 중에서 경기에 나갈 5명의 선수를 선발하는 경우", False, False, "경기에 나가는 선수 5명은 역할 구분이 없으므로(일단 선발만 하는 것이므로) **조합**입니다.")
]

for i, (question, p_check, c_check, answer) in enumerate(quiz_data):
    st.subheader(question)
    cols = st.columns(2)
    p_check = cols[0].checkbox("순열", key=f"p{i}")
    c_check = cols[1].checkbox("조합", key=f"c{i}")

    if p_check or c_check:
        st.info(answer)

import streamlit as st
import math

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="순열/조합 과정 계산기",
    page_icon="🧮",
    layout="wide"
)

# --- 제목 ---
st.title("🧮 순열/조합 과정 계산기")
st.markdown("숫자 n과 r을 입력하면, 계산 과정과 결과를 단계별로 보여줍니다.")

# --- 팩토리얼 계산 및 과정 문자열을 반환하는 함수 ---
def factorial_with_steps(k):
    """팩토리얼 값을 계산하고, 계산 과정을 문자열로 반환합니다."""
    if k == 0:
        return 1, "1 (0!은 1로 정의됩니다)"
    
    # 계산 과정 문자열 생성 (예: 5 × 4 × 3 × 2 × 1)
    steps_str = " × ".join(map(str, range(k, 0, -1)))
    
    # 실제 팩토리얼 값 계산
    result = math.factorial(k)
    
    return result, steps_str

# --- 사용자 입력 (2개의 컬럼 사용) ---
col1_input, col2_input = st.columns(2)
with col1_input:
    n = st.number_input("전체 개수 (n)을 입력하세요", min_value=0, value=5, step=1)
with col2_input:
    # r은 n보다 클 수 없으므로 max_value=n으로 설정
    r = st.number_input("뽑을 개수 (r)을 입력하세요", min_value=0, max_value=n, value=3, step=1)

# --- 계산 및 결과 표시 ---
if st.button("결과 계산하기"):
    col1_result, col2_result = st.columns(2)

    # --- 순열 (Permutation) ---
    with col1_result:
        st.subheader(f"🥇 순열: {n}P{r} 계산 과정")

        # 공식 보여주기
        st.latex(fr"nPr = \frac{{n!}}{{(n-r)!}} = \frac{{{n}!}}{{({n}-{r})!}} = \frac{{{n}!}}{{{n-r}!}}")
        
        with st.expander("자세한 계산 과정 보기"):
            # 1. 분자 n! 계산 과정
            n_fact_val, n_fact_steps = factorial_with_steps(n)
            st.markdown(f"**1. 분자 `n!` 계산:**")
            st.markdown(f"`{n}!` = {n_fact_steps} = **`{n_fact_val}`**")

            # 2. 분모 (n-r)! 계산 과정
            n_minus_r = n - r
            nmr_fact_val, nmr_fact_steps = factorial_with_steps(n_minus_r)
            st.markdown(f"**2. 분모 `(n-r)!` 계산:**")
            st.markdown(f"`({n}-{r})!` = `{n_minus_r}!` = {nmr_fact_steps} = **`{nmr_fact_val}`**")
            
            # 3. 최종 계산
            st.markdown(f"**3. 최종 계산:**")
            if nmr_fact_val == 0: # 0으로 나누는 경우 방지
                st.error("오류: 0으로 나눌 수 없습니다.")
                p_result = "계산 불가"
            else:
                p_result = n_fact_val // nmr_fact_val
                st.latex(fr"\frac{{{n_fact_val}}}{{{nmr_fact_val}}} = {p_result}")

        # 최종 결과
        st.success(f"**결과: {n}P{r} = {p_result}**")

    # --- 조합 (Combination) ---
    with col2_result:
        st.subheader(f"🤝 조합: {n}C{r} 계산 과정")

        # 공식 보여주기
        st.latex(fr"nCr = \frac{{n!}}{{r!(n-r)!}} = \frac{{{n}!}}{{{r}!({n}-{r})!}} = \frac{{{n}!}}{{{r}!{n-r}!}}")

        with st.expander("자세한 계산 과정 보기"):
            # 1. 분자 n! 계산 과정 (순열에서 이미 계산했지만, 교육용으로 다시 보여줌)
            n_fact_val, n_fact_steps = factorial_with_steps(n)
            st.markdown(f"**1. 분자 `n!` 계산:**")
            st.markdown(f"`{n}!` = {n_fact_steps} = **`{n_fact_val}`**")

            # 2. 분모 r! 계산 과정
            r_fact_val, r_fact_steps = factorial_with_steps(r)
            st.markdown(f"**2. 분모 `r!` 계산:**")
            st.markdown(f"`{r}!` = {r_fact_steps} = **`{r_fact_val}`**")
            
            # 3. 분모 (n-r)! 계산 과정
            n_minus_r = n - r
            nmr_fact_val, nmr_fact_steps = factorial_with_steps(n_minus_r)
            st.markdown(f"**3. 분모 `(n-r)!` 계산:**")
            st.markdown(f"`({n}-{r})!` = `{n_minus_r}!` = {nmr_fact_steps} = **`{nmr_fact_val}`**")
            
            # 4. 최종 계산
            st.markdown(f"**4. 최종 계산:**")
            denominator = r_fact_val * nmr_fact_val
            if denominator == 0:
                st.error("오류: 0으로 나눌 수 없습니다.")
                c_result = "계산 불가"
            else:
                c_result = n_fact_val // denominator
                st.latex(fr"\frac{{{n_fact_val}}}{{{r_fact_val} \times {nmr_fact_val}}} = \frac{{{n_fact_val}}}{{{denominator}}} = {c_result}")
        
        # 최종 결과
        st.success(f"**결과: {n}C{r} = {c_result}**")

else:
    st.info("위 상자에 숫자 n과 r을 입력하고 '결과 계산하기' 버튼을 누르세요.")

    import streamlit as st
import random
import math

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="순열과 조합 연습 문제",
    page_icon="✍️",
)

# --- 직접 만든 조합/순열 함수 ---
def combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def permutations(n, k):
    return math.factorial(n) // math.factorial(n - k)


# --- 문제 은행 (새로운 문제 2개 포함) ---
problem_set = [
    {
        "question": "7명의 학생 중에서 **회장 1명, 부회장 1명**을 뽑는 경우의 수는 몇 가지일까요?",
        "type": "P", "n": 7, "r": 2,
        "explanation": """
        이 문제는 **'회장'과 '부회장'이라는 역할(자리)이 서로 다르기 때문에 순서가 중요**합니다.  
        A가 회장, B가 부회장인 것과 B가 회장, A가 부회장인 것은 다른 경우입니다.  
        따라서 **순열(Permutation)**을 사용해야 합니다.
        
        - **계산식:** ₇P₂ = 7 × 6 = 42
        """
    },
    {
        "question": "서로 다른 10권의 책 중에서 3권을 뽑아 **책꽂이에 나란히 꽂는** 경우의 수는 몇 가지일까요?",
        "type": "P", "n": 10, "r": 3,
        "explanation": """
        책꽂이에 '나란히 꽂는다'는 것은 **순서대로 줄을 세우는 것**과 같습니다.  
        (A, B, C) 순서로 꽂는 것과 (A, C, B) 순서로 꽂는 것은 다른 경우입니다.  
        따라서 **순열(Permutation)**을 사용해야 합니다.

        - **계산식:** ₁₀P₃ = 10 × 9 × 8 = 720
        """
    },
    {
        "question": "8명의 동아리 회원 중에서 **대표 3명**을 뽑는 경우의 수는 몇 가지일까요?",
        "type": "C", "n": 8, "r": 3,
        "explanation": """
        이 문제는 3명 모두 **'대표'라는 동등한 자격**을 가집니다.  
        (A, B, C) 순서로 뽑히든 (C, B, A) 순서로 뽑히든, 결국 대표는 A, B, C 세 명으로 결과가 같습니다.  
        따라서 순서가 중요하지 않으므로 **조합(Combination)**을 사용해야 합니다.

        - **계산식:** ₈C₃ = (8 × 7 × 6) / (3 × 2 × 1) = 56
        """
    },
    {
        "question": "빨간색, 노란색, 파란색, 초록색, 보라색 5가지 색깔의 구슬 중에서 **순서에 상관없이 2개**를 뽑는 경우의 수는 몇 가지일까요?",
        "type": "C", "n": 5, "r": 2,
        "explanation": """
        문제에서 **'순서에 상관없이'** 라고 명시했기 때문에, 순서가 중요하지 않습니다.  
        (빨강, 노랑)을 뽑는 것과 (노랑, 빨강)을 뽑는 것은 같은 경우입니다.  
        따라서 **조합(Combination)**을 사용해야 합니다.

        - **계산식:** ₅C₂ = (5 × 4) / (2 × 1) = 10
        """
    },
    {
        "question": "6명의 축구 선수 중에서 **승부차기를 할 1번, 2번, 3번 키커**를 정하는 경우의 수는 몇 가지일까요?",
        "type": "P", "n": 6, "r": 3,
        "explanation": """
        승부차기는 **차는 순서가 매우 중요**합니다. 1번, 2번, 3번이라는 역할이 모두 다릅니다.  
        A 선수가 1번, B 선수가 2번으로 차는 것과 B 선수가 1번, A 선수가 2번으로 차는 것은 완전히 다른 전략입니다.  
        따라서 **순열(Permutation)**을 사용해야 합니다.

        - **계산식:** ₆P₃ = 6 × 5 × 4 = 120
        """
    },
    # --- 여기에 새로운 문제 2개 추가 ---
    {
        "question": "아이스크림 가게에 8가지 맛의 아이스크림이 있습니다. 이 중에서 **서로 다른 3가지 맛**을 골라 컵에 담는 경우의 수는 몇 가지일까요?",
        "type": "C", "n": 8, "r": 3,
        "explanation": """
        이 문제는 컵에 담는 아이스크림의 **순서는 중요하지 않습니다.** (초코, 바닐라, 딸기) 순서로 담으나 (딸기, 바닐라, 초코) 순서로 담으나 결과적으로 컵에 담긴 아이스크림의 종류는 같습니다.  
        따라서 순서가 중요하지 않으므로 **조합(Combination)**을 사용해야 합니다.

        - **계산식:** ₈C₃ = (8 × 7 × 6) / (3 × 2 × 1) = 56
        """
    },
    {
        "question": "숫자 카드 1, 2, 3, 4, 5, 6이 각각 하나씩 있습니다. 이 중에서 **3장을 뽑아 만들 수 있는 세 자리 자연수**는 몇 개일까요?",
        "type": "P", "n": 6, "r": 3,
        "explanation": """
        세 자리 자연수는 각 숫자의 **자리가 중요**합니다. 백의 자리, 십의 자리, 일의 자리가 있기 때문입니다.  
        예를 들어, 1, 2, 3을 뽑더라도 '123'과 '321'은 완전히 다른 수입니다. 즉, 순서가 중요합니다.  
        따라서 **순열(Permutation)**을 사용해야 합니다.

        - **계산식:** ₆P₃ = 6 × 5 × 4 = 120
        """
    }
]

# --- Streamlit 세션 상태 초기화 ---
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = random.choice(problem_set)
    st.session_state.show_answer = False

# --- 새 문제 출제 함수 ---
def get_new_problem():
    st.session_state.current_problem = random.choice(problem_set)
    st.session_state.show_answer = False # 새 문제가 나오면 해설 숨기기

# --- 제목 ---
st.title("✍️ 순열과 조합 실전 문제 풀이")
st.markdown("---")


# --- 새 문제 출제 버튼 ---
st.button("새로운 문제 가져오기", on_click=get_new_problem)


# --- 문제 표시 ---
problem = st.session_state.current_problem
st.subheader(f"📝 문제: {problem['question']}")


# --- 사용자 답변 입력 ---
with st.form("answer_form"):
    st.write("**어떤 공식을 사용해야 할까요?**")
    user_type = st.radio(
        "유형 선택:",
        ("순열 (Permutation)", "조합 (Combination)"),
        horizontal=True
    )
    
    st.write("**계산한 답을 입력하세요.**")
    user_answer = st.number_input("정답:", min_value=0, step=1, format="%d")

    submitted = st.form_submit_button("정답 제출하기")


# --- 채점 및 해설 ---
if submitted:
    # 정답 계산
    correct_type_str = "순열 (Permutation)" if problem['type'] == 'P' else "조합 (Combination)"
    correct_answer = permutations(problem['n'], problem['r']) if problem['type'] == 'P' else combinations(problem['n'], problem['r'])

    # 채점
    is_type_correct = (user_type == correct_type_str)
    is_answer_correct = (user_answer == correct_answer)

    if is_type_correct and is_answer_correct:
        st.success("🎉 정답입니다! 완벽하게 이해했네요!")
    else:
        st.error("惜しい! 다시 한번 생각해보세요.")
        if not is_type_correct:
            st.warning(f"힌트: 이 문제는 **'{correct_type_str}'**을 사용해야 합니다.")
        elif not is_answer_correct:
            st.warning(f"힌트: 계산 실수가 있었던 것 같아요. 정답은 **{correct_answer}** 입니다.")

    # 해설 표시
    with st.expander("📖 자세한 해설 보기", expanded=True):
        st.markdown(problem['explanation'])
        st.write(f"**정답:** {correct_answer}")

        

   