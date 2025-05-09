import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="로또 시뮬레이터",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 사용자 정의 CSS
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Noto Sans', sans-serif;
        }
        .main {
            padding: 40px;
            text-align: center;
        }
        h1 {
            color: #333;
        }
        .stButton > button {
            background-color: #007BFF;
            color: white;
            padding: 10px 24px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# 메인 UI
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("🎯 로또 시뮬레이터")
st.markdown("###### 지난주 당첨 번호를 입력하세요")

col1, col2, col3, col4, col5, col6, col_bonus = st.columns(7)
with col1: n1 = st.number_input("①", min_value=1, max_value=45, key="n1")
with col2: n2 = st.number_input("②", min_value=1, max_value=45, key="n2")
with col3: n3 = st.number_input("③", min_value=1, max_value=45, key="n3")
with col4: n4 = st.number_input("④", min_value=1, max_value=45, key="n4")
with col5: n5 = st.number_input("⑤", min_value=1, max_value=45, key="n5")
with col6: n6 = st.number_input("⑥", min_value=1, max_value=45, key="n6")
with col_bonus: bonus = st.number_input("보너스", min_value=1, max_value=45, key="bonus")

st.markdown("---")

st.markdown("###### 시뮬레이션 횟수를 선택하세요")
sim_count = st.radio("", [100, 1000, 10000, 100000, 1000000], horizontal=True)

if st.button("▶ 시뮬레이션 시작"):
    st.markdown("---")
    st.subheader("📊 시뮬레이션 결과")

    win_counts = {i: 0 for i in range(1, 6)}
    win_lotto = None

    winning_numbers = {n1, n2, n3, n4, n5, n6}

    for i in range(sim_count):
        lotto = set(random.sample(range(1, 46), 6))
        match = len(lotto & winning_numbers)
        bonus_matched = bonus in lotto

        if match == 6:
            win_counts[1] += 1
            if not win_lotto:
                win_lotto = (i+1, lotto, "1등")
        elif match == 5 and bonus_matched:
            win_counts[2] += 1
            if not win_lotto:
                win_lotto = (i+1, lotto, "2등")
        elif match == 5:
            win_counts[3] += 1
            if not win_lotto:
                win_lotto = (i+1, lotto, "3등")
        elif match == 4:
            win_counts[4] += 1
        elif match == 3:
            win_counts[5] += 1

    for rank, count in win_counts.items():
        st.markdown(f"🎯 {rank}등: {count}장")

    if win_lotto:
        st.success(f"🎉 {win_lotto[0]}번째 복권에서 {win_lotto[2]} 당첨!")
        st.code(sorted(win_lotto[1]))
    else:
        st.warning("😢 당첨된 복권이 없습니다.")

st.markdown("</div>", unsafe_allow_html=True)
