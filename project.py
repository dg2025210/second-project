import streamlit as st
import random

st.set_page_config(page_title="상식 퀴즈 🧠", page_icon="🧠")

st.title("🧠 랜덤 상식 퀴즈 🎯")
st.write("10문제를 풀고 당신의 지식 레벨을 확인해보세요! 😆")

# ✅ 100문제 자동 생성
quiz_data = []

base_questions = [
    ("대한민국의 수도는?", ["서울", "부산", "대구", "인천"], "서울"),
    ("물의 화학식은?", ["H2O", "CO2", "O2", "NaCl"], "H2O"),
    ("태양은 무엇인가?", ["행성", "별", "위성", "혜성"], "별"),
    ("지구는 몇 번째 행성인가?", ["1", "2", "3", "4"], "3"),
    ("피카소의 국적은?", ["프랑스", "스페인", "이탈리아", "독일"], "스페인"),
    ("세계에서 가장 큰 대륙은?", ["아시아", "유럽", "아프리카", "남극"], "아시아"),
    ("1년은 몇 개월?", ["10", "11", "12", "13"], "12"),
    ("빛의 속도는?", ["약 30만 km/s", "약 3만 km/s", "약 3000 km/s", "약 300 km/s"], "약 30만 km/s"),
    ("컴퓨터의 두뇌는?", ["RAM", "CPU", "SSD", "GPU"], "CPU"),
    ("대한민국 국기는?", ["성조기", "태극기", "일장기", "오성홍기"], "태극기")
]

# 100문제로 확장 (문장만 살짝 변형)
for i in range(10):
    for q in base_questions:
        quiz_data.append({
            "question": f"{q[0]} ({i+1})",
            "options": q[1],
            "answer": q[2],
            "explanation": f"정답은 {q[2]} 입니다 💡"
        })

# 상태 초기화
if "quiz_set" not in st.session_state:
    st.session_state.quiz_set = random.sample(quiz_data, 10)  # 🔥 중복 없이 10문제
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.finished = False

# 문제 진행
if not st.session_state.finished:
    q = st.session_state.quiz_set[st.session_state.current]

    st.subheader(f"📍 문제 {st.session_state.current + 1}/10")
    st.write(f"❓ {q['question']}")

    choice = st.radio("선택하세요 👇", q["options"], key=st.session_state.current)

    if st.button("정답 확인 ✅"):
        if choice == q["answer"]:
            st.success("정답입니다! 🎉")
            st.balloons()
            st.session_state.score += 1
        else:
            st.error(f"오답 😢 정답: {q['answer']}")

        st.info(q["explanation"])

        if st.session_state.current < 9:
            if st.button("다음 문제 ➡️"):
                st.session_state.current += 1
        else:
            st.session_state.finished = True

# 결과 화면
else:
    score = st.session_state.score

    st.title("🏁 결과 발표 🎉")
    st.subheader(f"당신의 점수: {score} / 10")

    # 🧠 지식 수준 평가
    if score == 10:
        level = "🧠 천재 수준"
    elif score >= 8:
        level = "🔥 매우 뛰어난 지식"
    elif score >= 5:
        level = "👍 평균 이상"
    elif score >= 3:
        level = "🙂 조금 더 공부 필요"
    else:
        level = "😅 기초부터 다시!"

    st.success(f"당신의 지식 레벨: {level}")

    if st.button("다시 도전 🔄"):
        st.session_state.clear()
