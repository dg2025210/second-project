import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="🍔 가위바위보 게임", page_icon="✊")

st.title("🍔 가위바위보 게임 ✊✋✌️")
st.write("음식으로 즐기는 가위바위보! 😋")

# 선택지 + 음식 이미지
choices = {
    "가위 ✌️": {
        "emoji": "✌️",
        "image": "https://images.unsplash.com/photo-1604908176997-4317c13b7c3d",  # 감자튀김
        "food": "🍟 감자튀김"
    },
    "바위 ✊": {
        "emoji": "✊",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",  # 햄버거
        "food": "🍔 햄버거"
    },
    "보 ✋": {
        "emoji": "✋",
        "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c",  # 샐러드
        "food": "🥗 샐러드"
    }
}

# 유저 선택
st.subheader("👉 당신의 선택은?")
col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    if st.button("가위 ✌️"):
        user_choice = "가위 ✌️"

with col2:
    if st.button("바위 ✊"):
        user_choice = "바위 ✊"

with col3:
    if st.button("보 ✋"):
        user_choice = "보 ✋"

# 결과 처리
if user_choice:
    computer_choice = random.choice(list(choices.keys()))

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 😎 당신")
        st.image(choices[user_choice]["image"])
        st.write(choices[user_choice]["food"])

    with col2:
        st.markdown("### 🤖 컴퓨터")
        st.image(choices[computer_choice]["image"])
        st.write(choices[computer_choice]["food"])

    # 승패 판정
    result = ""

    if user_choice == computer_choice:
        result = "🤝 비겼어요!"
    elif (
        (user_choice == "가위 ✌️" and computer_choice == "보 ✋") or
        (user_choice == "바위 ✊" and computer_choice == "가위 ✌️") or
        (user_choice == "보 ✋" and computer_choice == "바위 ✊")
    ):
        result = "🎉 이겼어요!!"
        st.balloons()
    else:
        result = "😢 졌어요..."

    st.subheader(result)
