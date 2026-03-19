import streamlit as st
import random
import time

st.set_page_config(page_title="🎮 Dodge Game", page_icon="🎯", layout="centered")

# ----------------------
# 초기 상태 설정
# ----------------------
if "player_x" not in st.session_state:
    st.session_state.player_x = 5
if "obstacles" not in st.session_state:
    st.session_state.obstacles = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "speed" not in st.session_state:
    st.session_state.speed = 0.3

# ----------------------
# UI
# ----------------------
st.title("🎮 피하기 게임 (Dodge Game)")
st.markdown("👉 좌우 버튼으로 캐릭터를 움직여 장애물을 피하세요!")

col1, col2, col3 = st.columns(3)

# ----------------------
# 이동 버튼
# ----------------------
with col1:
    if st.button("⬅️ 왼쪽"):
        if st.session_state.player_x > 0:
            st.session_state.player_x -= 1

with col3:
    if st.button("➡️ 오른쪽"):
        if st.session_state.player_x < 10:
            st.session_state.player_x += 1

# ----------------------
# 게임 보드 출력
# ----------------------
board = [["⬛" for _ in range(11)] for _ in range(10)]

# 플레이어 표시
board[9][st.session_state.player_x] = "🟦"

# 장애물 생성
if random.random() < 0.4:
    st.session_state.obstacles.append([0, random.randint(0, 10)])

new_obstacles = []
for y, x in st.session_state.obstacles:
    y += 1
    if y < 10:
        new_obstacles.append([y, x])
        board[y][x] = "💣"

        # 충돌 체크
        if y == 9 and x == st.session_state.player_x:
            st.session_state.game_over = True

st.session_state.obstacles = new_obstacles

# ----------------------
# 출력
# ----------------------
for row in board:
    st.write("".join(row))

st.markdown(f"### ⭐ 점수: {st.session_state.score}")

# ----------------------
# 게임 상태 처리
# ----------------------
if not st.session_state.game_over:
    st.session_state.score += 1
    time.sleep(st.session_state.speed)
    st.rerun()

else:
    st.error("💥 게임 오버!")
    st.balloons()

    st.markdown(f"## 🎉 최종 점수: {st.session_state.score}")

    if st.button("🔄 다시 시작"):
        st.session_state.player_x = 5
        st.session_state.obstacles = []
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()
