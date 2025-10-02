import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="이항정리란 무엇일까?",
    page_icon="🤔",
    layout="wide"
)

# --- 1. 제목 및 문제 제기 ---
st.title("🤔 이항정리, 왜 배울까요?")
st.markdown("---")

st.write("우리는 중학교 때 $(a+b)^2$을 전개하는 곱셈 공식을 배웠습니다.")
st.latex("(a+b)^2 = a^2 + 2ab + b^2")

st.write("$(a+b)^3$ 정도까지는 조금 귀찮아도 직접 전개해볼 수 있습니다.")
st.latex("(a+b)^3 = (a+b)(a^2 + 2ab + b^2) = a^3 + 3a^2b + 3ab^2 + b^3")

st.error("""
### 하지만 만약 누군가 $(a+b)^7$을 전개하라고 한다면 어떨까요?
하나씩 곱해서 계산하기에는 너무 복잡하고, 실수하기도 쉽습니다.  
**이항정리는 바로 이럴 때 사용하는, $(a+b)^n$을 손쉽게 전개하는 규칙입니다.**
""")
st.markdown("---")

# --- 2. 규칙 발견하기 ---
st.header("🔍 전개식 속에 숨겨진 규칙 발견하기")
st.markdown("먼저 $(a+b)^n$의 전개 결과를 나열해보고, 어떤 규칙이 있는지 찾아봅시다.")

st.code(f"""
n=0:  (a+b)⁰ = 1
n=1:  (a+b)¹ = 1a + 1b
n=2:  (a+b)² = 1a² + 2ab + 1b²
n=3:  (a+b)³ = 1a³ + 3a²b + 3ab² + 1b³
n=4:  (a+b)⁴ = 1a⁴ + 4a³b + 6a²b² + 4ab³ + 1b⁴
""", language='text')

st.subheader("규칙 1: 문자와 지수의 변화")
st.info("""
-   각 항은 **$a^x b^y$** 형태로 이루어져 있습니다.
-   **a의 지수**는 n부터 시작해서 1씩 감소하고, **b의 지수**는 0부터 시작해서 1씩 증가합니다.
-   각 항의 **지수의 합 (x + y)**은 항상 **n**으로 일정합니다.
""")

st.subheader("규칙 2: 계수의 변화")
st.info("""
-   각 항의 계수들만 따로 떼어놓고 보면 어떤 패턴이 보입니다.
-   `1, 4, 6, 4, 1` 은 바로 위 `1, 3, 3, 1` 에서 **서로 이웃한 두 수를 더해서** 만들어집니다. (예: 1+3=4, 3+3=6, 3+1=4)
-   이 패턴은 바로 **'파스칼의 삼각형'** 입니다!
""")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/PascalTriangleAnimated2.gif/250px-PascalTriangleAnimated2.gif",
         caption="파스칼의 삼각형: 위의 두 수를 더하면 아래 수가 됩니다.")
st.markdown("---")


# --- 3. 핵심 원리: 계수는 왜 조합(Combination)일까? ---
st.header("💡 핵심 원리: 계수는 왜 조합일까?")
st.markdown("""
$(a+b)^3 = (a+b)(a+b)(a+b)$ 를 다시 생각해봅시다.  
이 식을 전개할 때 나오는 각 항은 **3개의 괄호**에서 각각 **a 또는 b 중 하나씩**을 뽑아 곱해서 만들어집니다.
""")

col1, col2 = st.columns(2)
with col1:
    st.subheader("`a²b` 항은 어떻게 만들어질까요?")
    st.markdown("""
    `a²b` 항이 나오려면, 3개의 괄호 중 **2개에서는 a를, 1개에서는 b를** 뽑아야 합니다.
    -   `b` a a  (첫 번째 괄호에서 b를 뽑는 경우)
    -   a `b` a  (두 번째 괄호에서 b를 뽑는 경우)
    -   a a `b`  (세 번째 괄호에서 b를 뽑는 경우)
    
    총 **3가지** 경우가 나오므로, `a²b` 항의 계수는 **3**이 됩니다.
    """)

with col2:
    st.subheader("이것이 바로 '조합'입니다!")
    st.markdown("""
    "3개의 괄호 중 b를 뽑을 1개의 괄호를 선택하는 경우의 수"
    
    이것은 우리가 배운 **조합(Combination)**의 개념과 정확히 일치합니다.
    """)
    st.latex("_{3}C_{1} = \\frac{3!}{1!(3-1)!} = 3")

st.success("""
### 결론
$(a+b)^n$의 전개식에서 특정 항 $a^{n-k}b^k$의 계수는,  
**"n개의 괄호 중에서 b를 뽑을 k개의 괄호를 선택하는 경우의 수"**, 즉 **$_{n}C_{k}$** 와 같습니다.
""")
st.markdown("---")

# --- 4. 다음 페이지 안내 ---
st.header("🚀 이제 원리를 알았으니 직접 탐험해볼까요?")

import streamlit as st
import math

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="이항정리 탐험기",
    page_icon="🔨",
    layout="wide"
)

# --- 직접 만든 조합 함수 (버전 호환성 문제 해결) ---
def combinations(n, k):
    """
    math.comb 함수가 구버전 파이썬에서 오류를 일으킬 수 있어,
    팩토리얼을 이용해 직접 조합 함수를 만듭니다.
    """
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# --- 1. 제목 및 소개 ---
st.title("🔨 이항정리 탐험기")
st.markdown("""
이항정리는 $(a+b)^n$과 같은 다항식을 쉽게 전개하는 방법을 알려주는 강력한 정리입니다.  
아래 도구를 통해 이항정리의 핵심 원리인 **파스칼의 삼각형**과 **이항계수**의 관계를 탐색하고, 복잡한 식을 자동으로 계산해보세요!
""")
st.markdown("---")


# --- 2. 파스칼의 삼각형과 이항계수 ---
st.header("1. 파스칼의 삼각형과 이항계수의 관계")
st.markdown("""
파스칼의 삼각형에 있는 숫자들은 사실 **조합(Combination, C(n, k))**으로 표현할 수 있습니다.  
그리고 이 숫자들은 $(a+b)^n$을 전개했을 때 나타나는 각 항의 계수, 즉 **이항계수**가 됩니다.
""")

triangle_rows = st.slider("파스칼의 삼각형 크기 조절", 2, 12, 6)

col1, col2 = st.columns(2)
with col1:
    st.subheader("파스칼의 삼각형 (숫자)")
    triangle_str = ""
    for n in range(triangle_rows):
        # 가운데 정렬을 위한 공백
        triangle_str += " " * (triangle_rows - n - 1) * 2
        for k in range(n + 1):
            coeff = combinations(n, k)
            triangle_str += f"{coeff:<4}" # 각 숫자가 차지하는 공간을 4칸으로 통일
        triangle_str += "\n"
    st.code(triangle_str, language='text')

with col2:
    st.subheader("이항계수 (C(n, k) 형태)")
    ncr_triangle_str = ""
    for n in range(triangle_rows):
        ncr_triangle_str += " " * (triangle_rows - n - 1) * 4
        for k in range(n + 1):
            ncr_triangle_str += f"C({n},{k})".ljust(8) # 각 항목이 차지하는 공간을 8칸으로 통일
        ncr_triangle_str += "\n"
    st.code(ncr_triangle_str, language='text')

st.info(f"예를 들어, 파스칼 삼각형의 {triangle_rows}번째 줄은 $(a+b)^{triangle_rows-1}$의 계수와 정확히 일치합니다.")
st.markdown("---")


# --- 3. 자동 전개식 계산기 ---
st.header("2. $(a+b)^n$ 자동 전개식 계산기")
st.markdown("전개하려는 식의 항과 제곱수(n)를 입력하면, 이항정리를 이용해 전개된 결과를 보여줍니다.")

# 사용자 입력
exp_col1, exp_col2, exp_col3 = st.columns([1, 1, 0.8])
with exp_col1:
    a_term = st.text_input("첫 번째 항 (a)", "a")
with exp_col2:
    b_term = st.text_input("두 번째 항 (b)", "2b")
with exp_col3:
    n_val = st.number_input("제곱수 (n)", min_value=0, max_value=17, value=3, step=1)

if st.button("🚀 전개식 계산하기"):
    if not a_term or not b_term:
        st.error("첫 번째 항과 두 번째 항을 모두 입력해주세요.")
    else:
        # 이항정리 전개식 생성
        expansion_parts = []
        for k in range(n_val + 1):
            # 1. 이항계수 계산 (nCk)
            coeff = combinations(n_val, k)
            
            # 2. 각 항의 문자 부분 LaTeX 문자열 생성
            a_power = n_val - k
            b_power = k
            
            term_str = ""
            
            # 계수가 1보다 크면 계수를 추가 (1이면 생략)
            if coeff > 1:
                term_str += str(coeff)

            # a항 추가 (지수가 0이면 생략, 1이면 숫자 생략)
            if a_power > 0:
                if len(a_term) > 1:
                    term_str += f"({a_term})"
                else:
                    term_str += a_term
                if a_power > 1:
                    term_str += f"^{{{a_power}}}"
            
            # b항 추가 (지수가 0이면 생략, 1이면 숫자 생략)
            if b_power > 0:
                if len(b_term) > 1:
                    term_str += f"({b_term})"
                else:
                    term_str += b_term
                if b_power > 1:
                    term_str += f"^{{{b_power}}}"
            
            expansion_parts.append(term_str)
            
        final_expansion_str = " + ".join(expansion_parts)
        
        st.subheader("📜 계산 결과")
        # KaTeX를 이용해 수학 공식처럼 예쁘게 보여주기
        latex_display_string = f"({a_term} + {b_term})^{{{n_val}}} = {final_expansion_str}"
        st.latex(latex_display_string)

        with st.expander("결과가 나오는 원리 (이항정리 공식)"):
            st.markdown(f"**{n_val+1}개의 항**이 나타나는 이유는 **{n_val}개의 $({a_term}+{b_term})$ 괄호**에서 각각 `{a_term}` 또는 `{b_term}`를 하나씩 뽑기 때문입니다.")
            st.markdown(f"- **`{b_term}`를 0번** 뽑는 경우 (즉, `{a_term}`만 {n_val}번): $C({n_val}, 0) = {combinations(n_val, 0)}$가지")
            st.markdown(f"- **`{b_term}`를 1번** 뽑는 경우: $C({n_val}, 1) = {combinations(n_val, 1)}$가지")
            st.markdown("...")
            st.markdown(f"- **`{b_term}`를 {n_val}번** 뽑는 경우: $C({n_val}, {n_val}) = {combinations(n_val, n_val)}$가지")
            st.success("이처럼 각 항의 계수는 **'몇 개의 괄호에서 b를 뽑을 것인가'**를 결정하는 **조합(Combination)**의 수와 같습니다.")