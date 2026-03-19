import streamlit as st
import random

st.set_page_config(page_title="🍔 음식 이상형 월드컵", layout="wide")

# 🎯 음식 데이터 (이미지는 무료 URL 사용)
foods = [
    {"name": "🍙 주먹밥", "img": "https://www.google.com/imgres?q=%EC%A3%BC%EB%A8%B9%EB%B0%A5&imgurl=https%3A%2F%2Fstatic.japan-food.guide%2Fuploads%2Farticle%2Fcover_image%2F000%2F000%2F079%2Fd2d7e3fda4c7c8b8092baeb9a2ee995fba8a0c078bfecbcdda2f201b3fbe1820%2Fthumbnail_onigiri.jpg%3F1765173747&imgrefurl=https%3A%2F%2Fjapan-food.guide%2Fko%2Farticles%2Fonigiri&docid=81rq357Up_4hrM&tbnid=lFMhUr-onVyW9M&vet=12ahUKEwi4yej26aqTAxWVsFYBHalxKPYQnPAOegQIGRAB..i&w=375&h=250&hcb=2&ved=2ahUKEwi4yej26aqTAxWVsFYBHalxKPYQnPAOegQIGRAB"},
    {"name": "🍜 라면", "img": "https://source.unsplash.com/600x400/?ramen"},
    {"name": "🌮 타코", "img": "https://source.unsplash.com/600x400/?taco"},
    {"name": "🍗 치킨", "img": "https://source.unsplash.com/600x400/?fried-chicken"},
    {"name": "🍕 피자", "img": "https://source.unsplash.com/600x400/?pizza"},
    {"name": "🍣 초밥", "img": "https://source.unsplash.com/600x400/?sushi"},
    {"name": "🍛 카레", "img": "https://source.unsplash.com/600x400/?curry"},
    {"name": "🍔 햄버거", "img": "https://source.unsplash.com/600x400/?burger"},
    {"name": "🍝 파스타", "img": "https://source.unsplash.com/600x400/?pasta"},
    {"name": "🥗 샐러드", "img": "https://source.unsplash.com/600x400/?salad"},
    {"name": "🍰 케이크", "img": "https://source.unsplash.com/600x400/?cake"},
    {"name": "🍩 도넛", "img": "https://source.unsplash.com/600x400/?donut"},
    {"name": "🍫 초콜릿", "img": "https://source.unsplash.com/600x400/?chocolate"},
    {"name": "🍓 딸기", "img": "https://source.unsplash.com/600x400/?strawberry"},
    {"name": "🥞 팬케이크", "img": "https://source.unsplash.com/600x400/?pancake"},
    {"name": "🥟 만두", "img": "https://source.unsplash.com/600x400/?dumpling"},
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
