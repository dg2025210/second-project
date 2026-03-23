import streamlit as st
import random

st.set_page_config(page_title="가위바위보 게임 ✊✌️✋", page_icon="🎮")

st.title("🎮 가위바위보 게임 ✊✌️✋")
st.write("이기면 풍선이 터집니다! 🎈")

# ✅ 정확한 이미지 (위키 기반 - 안정적)
images = {
    "가위": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Scissors_icon.png",
    "바위": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Rock_icon.png",
    "보": "https://upload.wikimedia.org/wikipedia/commons/2/25/Paper_icon.png"
}

# ✅ 이모지 fallback
emojis = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

choices = ["가위", "바위", "보"]

st.subheader("👉 선택하세요!")
user_choice = st.radio("", choices, horizontal=True)

if st.button("🔥 결과 보기!"):

    computer_choice = random.choice(choices)

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧑 당신")
        st.image(images[user_choice], width=120)
        st.markdown(f"## {emojis[user_choice]} {user_choice}")

    with col2:
        st.subheader("💻 컴퓨터")
        st.image(images[computer_choice], width=120)
        st.markdown(f"## {emojis[computer_choice]} {computer_choice}")

    st.markdown("---")

    # 결과 판정
    if user_choice == computer_choice:
        st.info("😐 비겼습니다!")
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        st.success("🎉 당신 승리!")
        st.balloons()
    else:
        st.error("😢 컴퓨터 승리!")

st.markdown("---")
st.caption("✨ 이미지 + 이모지 안정 버전")
