import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="가위바위보 게임 ✊✌️✋", page_icon="🎮")

# 제목
st.title("🎮 가위바위보 게임 ✊✌️✋")
st.write("컴퓨터와 가위바위보 한판! 이기면 🎈풍선이 터집니다!")

# 이미지 URL
images = {
    "가위": "https://cdn-icons-png.flaticon.com/512/3595/3595455.png",
    "바위": "https://cdn-icons-png.flaticon.com/512/686/686589.png",
    "보": "https://cdn-icons-png.flaticon.com/512/3595/3595458.png"
}

choices = ["가위", "바위", "보"]

# 사용자 선택
st.subheader("👉 당신의 선택은?")
user_choice = st.radio(
    "선택하세요!",
    choices,
    horizontal=True
)

# 버튼
if st.button("🔥 결과 보기!"):

    computer_choice = random.choice(choices)

    st.markdown("---")
    st.subheader("🧑 당신 vs 💻 컴퓨터")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧑 당신")
        st.image(images[user_choice], width=150)
        st.write(f"👉 {user_choice}")

    with col2:
        st.markdown("### 💻 컴퓨터")
        st.image(images[computer_choice], width=150)
        st.write(f"👉 {computer_choice}")

    st.markdown("---")

    # 결과 판정
    if user_choice == computer_choice:
        st.info("😐 비겼습니다!")
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        st.success("🎉 당신이 이겼습니다!!")
        st.balloons()
    else:
        st.error("😢 컴퓨터가 이겼습니다!")

# 하단 꾸미기
st.markdown("---")
st.caption("✨ 재미로 만든 미니 게임 | Streamlit 💙")
