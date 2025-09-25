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

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="순열과 조합 심화 학습",
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