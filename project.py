import streamlit as st
import random
import time

# ── 페이지 설정 ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="✊ 가위바위보",
    page_icon="✊",
    layout="centered",
)

# ── 전역 CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700;800&display=swap');

/* 배경 그라디언트 애니메이션 */
@keyframes bgShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* 풍선 떠오르기 */
@keyframes balloonRise {
    0%   { transform: translateY(100vh) scale(0.5) rotate(-10deg); opacity: 0; }
    20%  { opacity: 1; }
    80%  { opacity: 0.8; }
    100% { transform: translateY(-20vh) scale(1.2) rotate(10deg); opacity: 0; }
}

/* 흔들기 */
@keyframes shake {
    0%,100% { transform: translateX(0); }
    20%      { transform: translateX(-8px) rotate(-3deg); }
    40%      { transform: translateX(8px)  rotate(3deg); }
    60%      { transform: translateX(-6px) rotate(-2deg); }
    80%      { transform: translateX(6px)  rotate(2deg); }
}

/* 팡 터지기 */
@keyframes pop {
    0%   { transform: scale(1); }
    40%  { transform: scale(1.35); }
    60%  { transform: scale(0.92); }
    80%  { transform: scale(1.12); }
    100% { transform: scale(1); }
}

/* 별 반짝임 */
@keyframes twinkle {
    0%,100% { opacity: 1;   transform: scale(1); }
    50%      { opacity: 0.3; transform: scale(0.7); }
}

/* 승리 빛남 */
@keyframes winGlow {
    0%,100% { box-shadow: 0 0 24px 4px #ffe06688; }
    50%      { box-shadow: 0 0 48px 16px #ff9f0a99; }
}

/* 카드 등장 */
@keyframes cardIn {
    from { opacity: 0; transform: translateY(30px) scale(0.9); }
    to   { opacity: 1; transform: translateY(0)    scale(1);   }
}

/* 스코어 펄스 */
@keyframes scorePulse {
    0%,100% { transform: scale(1); }
    50%      { transform: scale(1.18); }
}

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460, #533483);
    background-size: 400% 400%;
    animation: bgShift 12s ease infinite;
    font-family: 'Nanum Gothic', sans-serif;
    color: #f0f0f0;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { display: none; }
.block-container { padding-top: 2rem !important; max-width: 760px; }

/* 타이틀 */
.main-title {
    font-family: 'Jua', sans-serif;
    font-size: 3.2rem;
    text-align: center;
    background: linear-gradient(90deg, #ffe066, #ff9f0a, #ff6b6b, #ff9f0a, #ffe066);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: bgShift 4s linear infinite;
    margin-bottom: 0.2rem;
    letter-spacing: 2px;
    text-shadow: none;
}

.sub-title {
    text-align: center;
    color: #aab4d4;
    font-size: 1rem;
    margin-bottom: 1.5rem;
    letter-spacing: 1px;
}

/* 점수판 */
.scoreboard {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-bottom: 1.6rem;
}

.score-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 16px;
    padding: 0.7rem 1.5rem;
    text-align: center;
    min-width: 100px;
    backdrop-filter: blur(6px);
}

.score-label {
    font-size: 0.75rem;
    color: #aab4d4;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.score-num {
    font-family: 'Jua', sans-serif;
    font-size: 2rem;
    line-height: 1.2;
}

.score-win  { color: #ffe066; }
.score-draw { color: #a0c4ff; }
.score-lose { color: #ff6b6b; }

/* 손 선택 버튼 */
.choice-row {
    display: flex;
    justify-content: center;
    gap: 1.2rem;
    flex-wrap: wrap;
    margin-bottom: 1.4rem;
}

.choice-btn {
    background: rgba(255,255,255,0.08);
    border: 2px solid rgba(255,255,255,0.18);
    border-radius: 20px;
    padding: 1rem 1.4rem;
    cursor: pointer;
    transition: transform 0.18s, border-color 0.18s, background 0.18s;
    text-align: center;
    min-width: 130px;
    animation: cardIn 0.5s ease;
}

.choice-btn:hover {
    transform: translateY(-6px) scale(1.07);
    border-color: #ffe066;
    background: rgba(255,224,102,0.13);
}

.choice-btn .hand-img {
    font-size: 4rem;
    display: block;
    margin-bottom: 0.3rem;
    filter: drop-shadow(0 4px 12px rgba(255,224,102,0.3));
}

.choice-btn .hand-label {
    font-family: 'Jua', sans-serif;
    font-size: 1.1rem;
    color: #e8e8e8;
}

/* 대결 결과 박스 */
.result-box {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 24px;
    padding: 1.6rem;
    text-align: center;
    margin-bottom: 1.2rem;
    animation: cardIn 0.4s ease;
    backdrop-filter: blur(8px);
}

.vs-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1.4rem;
    margin-bottom: 1rem;
}

.vs-hand {
    font-size: 5rem;
    animation: pop 0.5s ease;
    filter: drop-shadow(0 6px 18px rgba(255,255,255,0.2));
}

.vs-label {
    font-family: 'Jua', sans-serif;
    font-size: 1.6rem;
    color: #aab4d4;
}

.result-text {
    font-family: 'Jua', sans-serif;
    font-size: 2.4rem;
    margin-top: 0.3rem;
    letter-spacing: 2px;
}

.result-win  { color: #ffe066; animation: shake 0.5s ease, winGlow 1.6s infinite; }
.result-draw { color: #a0c4ff; }
.result-lose { color: #ff6b6b; animation: shake 0.5s ease; }

/* 풍선 컨테이너 */
.balloons-wrap {
    position: fixed;
    bottom: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 9999;
    overflow: hidden;
}

.balloon {
    position: absolute;
    font-size: 2.8rem;
    animation: balloonRise linear forwards;
    bottom: -60px;
}

/* 별 반짝임 장식 */
.stars-row {
    text-align: center;
    font-size: 1.1rem;
    margin-bottom: 0.8rem;
    animation: twinkle 1.8s ease-in-out infinite;
    color: #ffe066;
    letter-spacing: 4px;
}

/* 리셋 버튼 */
.stButton > button {
    background: linear-gradient(135deg, #ff6b6b, #ff9f0a) !important;
    color: #1a1a2e !important;
    font-family: 'Jua', sans-serif !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.5rem 1.8rem !important;
    transition: transform 0.15s, box-shadow 0.15s !important;
    box-shadow: 0 4px 16px rgba(255,159,10,0.35) !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 0 8px 24px rgba(255,159,10,0.5) !important;
}

.footer-txt {
    text-align: center;
    color: #555e7a;
    font-size: 0.78rem;
    margin-top: 1rem;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ── 세션 상태 초기화 ──────────────────────────────────────────────────────────
for key, default in [("wins", 0), ("draws", 0), ("losses", 0),
                     ("total", 0), ("result", None),
                     ("player_choice", None), ("computer_choice", None),
                     ("show_balloons", False)]:
    if key not in st.session_state:
        st.session_state[key] = default

# ── 데이터 ───────────────────────────────────────────────────────────────────
CHOICES = {
    "가위": {"emoji": "✂️", "img": "✂️", "beats": "보"},
    "바위": {"emoji": "✊", "img": "✊", "beats": "가위"},
    "보":   {"emoji": "🖐️", "img": "🖐️", "beats": "가위바위보"},   # placeholder
}

BEATS = {"가위": "보", "바위": "가위", "보": "바위"}   # 이기는 상대

def judge(player: str, computer: str) -> str:
    if player == computer:
        return "draw"
    if BEATS[player] == computer:
        return "win"
    return "lose"

def play(choice: str):
    computer = random.choice(list(CHOICES.keys()))
    outcome  = judge(choice, computer)

    st.session_state.player_choice   = choice
    st.session_state.computer_choice = computer
    st.session_state.total          += 1
    st.session_state.result          = outcome
    st.session_state.show_balloons   = (outcome == "win")

    if outcome == "win":
        st.session_state.wins   += 1
    elif outcome == "draw":
        st.session_state.draws  += 1
    else:
        st.session_state.losses += 1

def reset():
    for key in ("wins", "draws", "losses", "total"):
        st.session_state[key] = 0
    st.session_state.result          = None
    st.session_state.player_choice   = None
    st.session_state.computer_choice = None
    st.session_state.show_balloons   = False

# ── UI 렌더링 ─────────────────────────────────────────────────────────────────

# 타이틀
st.markdown('<div class="main-title">✊ 가위바위보 ✂️🖐️</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">컴퓨터와 한 판 승부! 이길 수 있겠어요? 😏</div>', unsafe_allow_html=True)

# 점수판
w = st.session_state.wins
d = st.session_state.draws
l = st.session_state.losses
t = st.session_state.total

st.markdown(f"""
<div class="scoreboard">
    <div class="score-card">
        <div class="score-label">🏆 승리</div>
        <div class="score-num score-win">{w}</div>
    </div>
    <div class="score-card">
        <div class="score-label">🤝 무승부</div>
        <div class="score-num score-draw">{d}</div>
    </div>
    <div class="score-card">
        <div class="score-label">💀 패배</div>
        <div class="score-num score-lose">{l}</div>
    </div>
    <div class="score-card">
        <div class="score-label">🎮 총판수</div>
        <div class="score-num" style="color:#c8d8f4">{t}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 손 선택 버튼 (Streamlit columns 사용)
st.markdown("### 🎯 손을 선택하세요!")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div style='text-align:center; font-size:4.5rem; margin-bottom:-0.5rem;
                filter:drop-shadow(0 6px 16px rgba(255,224,102,0.4));'>✂️</div>
    """, unsafe_allow_html=True)
    if st.button("✂️ 가위", use_container_width=True, key="btn_scissor"):
        play("가위")

with col2:
    st.markdown("""
    <div style='text-align:center; font-size:4.5rem; margin-bottom:-0.5rem;
                filter:drop-shadow(0 6px 16px rgba(255,159,10,0.4));'>✊</div>
    """, unsafe_allow_html=True)
    if st.button("✊ 바위", use_container_width=True, key="btn_rock"):
        play("바위")

with col3:
    st.markdown("""
    <div style='text-align:center; font-size:4.5rem; margin-bottom:-0.5rem;
                filter:drop-shadow(0 6px 16px rgba(100,220,255,0.4));'>🖐️</div>
    """, unsafe_allow_html=True)
    if st.button("🖐️ 보", use_container_width=True, key="btn_paper"):
        play("보")

# ── 결과 표시 ─────────────────────────────────────────────────────────────────
if st.session_state.result:
    pc = st.session_state.player_choice
    cc = st.session_state.computer_choice
    outcome = st.session_state.result

    RESULT_MAP = {
        "win":  ("🎉 내가 이겼다!", "result-win",  "🏆"),
        "draw": ("🤝 비겼어요!",    "result-draw", "😐"),
        "lose": ("😢 졌어요...",    "result-lose", "💀"),
    }
    rtxt, rcls, rico = RESULT_MAP[outcome]

    pe = CHOICES[pc]["emoji"]
    ce = CHOICES[cc]["emoji"]

    st.markdown(f"""
    <div class="result-box">
        <div style="color:#aab4d4; font-size:0.85rem; letter-spacing:2px; margin-bottom:0.8rem;">
            ⚔️ &nbsp; 대 결 결 과 &nbsp; ⚔️
        </div>
        <div class="vs-row">
            <div>
                <div class="vs-hand">{pe}</div>
                <div style="color:#ffe066; font-family:'Jua',sans-serif; font-size:0.95rem;">나 · {pc}</div>
            </div>
            <div class="vs-label">VS</div>
            <div>
                <div class="vs-hand" style="transform:scaleX(-1);">{ce}</div>
                <div style="color:#ff9f9f; font-family:'Jua',sans-serif; font-size:0.95rem;">컴퓨터 · {cc}</div>
            </div>
        </div>
        <div class="result-text {rcls}">{rico} {rtxt}</div>
    </div>
    """, unsafe_allow_html=True)

    # 승리 시 풍선 애니메이션
    if st.session_state.show_balloons:
        balloons_html = '<div class="balloons-wrap">'
        balloon_emojis = ["🎈","🎉","🎊","✨","🌟","💫","🏆","🎀","🥳","🎁"]
        for i in range(22):
            left   = random.randint(2, 96)
            delay  = round(random.uniform(0, 2.5), 2)
            dur    = round(random.uniform(3.2, 5.8), 2)
            size   = round(random.uniform(2.0, 3.8), 1)
            emoji  = random.choice(balloon_emojis)
            balloons_html += (
                f'<div class="balloon" style="left:{left}%;'
                f'animation-duration:{dur}s;animation-delay:{delay}s;'
                f'font-size:{size}rem;">{emoji}</div>'
            )
        balloons_html += "</div>"
        st.markdown(balloons_html, unsafe_allow_html=True)

        st.markdown("""
        <div class="stars-row">
            ★ ☆ ★ &nbsp; 축하합니다! 🥳 &nbsp; ★ ☆ ★
        </div>
        """, unsafe_allow_html=True)

    # 패배 시 위로 메시지
    elif outcome == "lose":
        st.markdown("""
        <div style="text-align:center; color:#aab4d4; font-size:0.95rem; margin-bottom:0.5rem;">
            😅 다시 도전해보세요! 화이팅! 💪
        </div>
        """, unsafe_allow_html=True)

# ── 구분선 + 리셋 ──────────────────────────────────────────────────────────────
st.markdown("---")

col_l, col_m, col_r = st.columns([1.5, 1, 1.5])
with col_m:
    if st.button("🔄 초기화", use_container_width=True, key="btn_reset"):
        reset()
        st.rerun()

# 승률 표시
if t > 0:
    win_rate = round(w / t * 100, 1)
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("📊 승률", f"{win_rate}%")
    with col_b:
        streak_label = "연속 승리 중! 🔥" if st.session_state.result == "win" else "더 잘 할 수 있어요! 💪"
        st.info(streak_label)

st.markdown('<div class="footer-txt">made with ❤️ &nbsp;·&nbsp; Streamlit Cloud</div>', unsafe_allow_html=True)
