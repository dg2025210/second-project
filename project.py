# second-project
import streamlit as st
import random

st.set_page_config(page_title="일반상식 퀴즈 🧠", page_icon="🧠")

st.title("🧠 일반상식 퀴즈 게임 🎯")
st.write("문제를 풀고 당신의 상식 레벨을 확인해보세요! 😆")

# 문제 리스트
quiz_data = [
    {
        "question": "대한민국의 수도는 어디일까요?",
        "options": ["서울", "부산", "대구", "인천"],
        "answer": "서울",
        "explanation": "서울은 대한민국의 정치, 경제 중심지입니다 🇰🇷"
    },
    {
        "question": "지구에서 가장 큰 대륙은?",
        "options": ["아프리카", "유럽", "아시아", "남아메리카"],
        "answer": "아시아",
        "explanation": "아시아는 면적과 인구 모두 가장 큰 대륙입니다 🌏"
    },
    {
        "question": "물의 화학식은?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "answer": "H2O",
        "explanation": "물은 수소 2개와 산소 1개로 이루어져 있습니다 💧"
    },
    {
        "question": "태양은 무엇일까요?",
        "options": ["행성", "별", "위성", "혜성"],
        "answer": "별",
        "explanation": "태양은 스스로 빛을 내는 별입니다 ☀️"
    },
    {
        "question": "피카소는 어느 나라 화가일까요?",
        "options": ["프랑스", "이탈리아", "스페인", "독일"],
        "answer": "스페인",
        "explanation": "피카소는 스페인 출신의 유명 화가입니다 🎨"
    }
]

# 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "question" not in st.session_state:
    st.session_state.question = random.choice(quiz_data)
if "answered" not in st.session_state:
    st.session_state.answered = False

q = st.session_state.question

st.subheader(f"❓ 문제: {q['question']}")

choice = st.radio("답을 선택하세요 👇", q["options"])

if st.button("정답 확인 ✅"):
    st.session_state.answered = True

    if choice == q["answer"]:
        st.success("정답입니다! 🎉😆")
        st.balloons()
        st.session_state.score += 1
    else:
        st.error(f"오답입니다 😢 정답은 '{q['answer']}' 입니다!")

    st.info(f"💡 해설: {q['explanation']}")

# 다음 문제 버튼
if st.session_state.answered:
    if st.button("다음 문제 ➡️"):
        st.session_state.question = random.choice(quiz_data)
        st.session_state.answered = False

# 점수 표시
st.markdown("---")
st.subheader(f"🏆 현재 점수: {st.session_state.score} 점")
