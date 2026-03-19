import streamlit as st
import random

st.set_page_config(page_title="🍔 음식 이상형 월드컵", layout="wide")

# 🎯 음식 데이터 (이미지는 무료 URL 사용)
foods = [
    {"name": "🍕 피자", "img": "https://images.unsplash.com/photo-1601924638867-3ec1c7c3b24f"},
    {"name": "🍔 햄버거", "img": "https://images.unsplash.com/photo-1550547660-d9450f859349"},
    {"name": "🍜 라면", "img": "https://images.unsplash.com/photo-1604908176997-4318f1c28f2d"},
    {"name": "🍣 초밥", "img": "https://images.unsplash.com/photo-1562158070-622a5d7c3a29"},
    {"name": "🍗 치킨", "img": "https://images.unsplash.com/photo-1606755962773-d324e9a13086"},
    {"name": "🌮 타코", "img": "https://images.unsplash.com/photo-1601924582975-7e6f4f2c9b87"},
    {"name": "🍝 파스타", "img": "https://images.unsplash.com/photo-1589302168068-964664d93dc0"},
    {"name": "🥗 샐러드", "img": "https://images.unsplash.com/photo-1551248429-40975aa4de74"},
    {"name": "🍰 케이크", "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"},
    {"name": "🍩 도넛", "img": "https://images.unsplash.com/photo-1542826438-bd32f43d626f"},
    {"name": "🍫 초콜릿", "img": "https://images.unsplash.com/photo-1511381939415-e44015466834"},
    {"name": "🍓 딸기", "img": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6"},
    {"name": "🥞 팬케이크", "img": "https://images.unsplash.com/photo-1587735243615-c03f25aaff15"},
    {"name": "🍙 주먹밥", "img": "https://images.unsplash.com/photo-1604908176997-4318f1c28f2d"},
    {"name": "🍛 카레", "img": "https://images.unsplash.com/photo-1604909052743-2f3c7c3e5e7f"},
    {"name": "🥟 만두", "img": "https://images.unsplash.com/photo-1608032077018-c9aad9565d29"},
]

# 🎮 초기 상태 설정
if "round" not in st.session_state:
    st.session_state.round = 16
    st.session_state.current = random.sample(foods, 16)
    st.session_state.next_round = []
    st.session_state.index = 0
    st.session_state.winner = None

# 🏆 타이틀
st.title("🍔 음식 이상형 월드컵 😋")
st.markdown(f"## 🔥 {st.session_state.round}강")

# 🏁 우승 화면
if st.session_state.winner:
    st.balloons()
    st.success(f"🏆 당신의 최애 음식은?! 👉 {st.session_state.winner['name']} 🎉")
    st.image(st.session_state.winner["img"], use_column_width=True)

    if st.button("🔄 다시하기"):
        st.session_state.clear()
    st.stop()

# ⚔️ 현재 대결
idx = st.session_state.index
foods_list = st.session_state.current

food1 = foods_list[idx]
food2 = foods_list[idx + 1]

col1, col2 = st.columns(2)

with col1:
    st.image(food1["img"], use_column_width=True)
    if st.button(food1["name"], key=f"left_{idx}"):
        st.session_state.next_round.append(food1)
        st.session_state.index += 2

with col2:
    st.image(food2["img"], use_column_width=True)
    if st.button(food2["name"], key=f"right_{idx}"):
        st.session_state.next_round.append(food2)
        st.session_state.index += 2

# 👉 라운드 종료 처리
if st.session_state.index >= len(st.session_state.current):
    if len(st.session_state.next_round) == 1:
        st.session_state.winner = st.session_state.next_round[0]
    else:
        st.session_state.current = st.session_state.next_round
        st.session_state.next_round = []
        st.session_state.index = 0
        st.session_state.round //= 2
        st.rerun()
