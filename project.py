import streamlit as st
import random
import time

st.set_page_config(page_title="🎮 Emoji Tetris", layout="centered")

st.title("🎮 Emoji 테트리스")
st.caption("← → ⬇️ 키 대신 버튼으로 조작하세요!")

# 보드 설정
WIDTH = 10
HEIGHT = 15
EMPTY = "⬛"

SHAPES = [
    [["🟥","🟥","🟥","🟥"]],
    [["🟩","🟩"],["🟩","🟩"]],
    [["⬜","🟦","⬜"],["🟦","🟦","🟦"]],
    [["🟨","🟨","⬜"],["⬜","🟨","🟨"]],
]

def create_board():
    return [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

def new_block():
    shape = random.choice(SHAPES)
    return {
        "shape": shape,
        "x": WIDTH // 2 - len(shape[0]) // 2,
        "y": 0
    }

def draw_board(board, block):
    temp = [row[:] for row in board]

    for i, row in enumerate(block["shape"]):
        for j, cell in enumerate(row):
            if cell != "⬜":
                x = block["x"] + j
                y = block["y"] + i
                if 0 <= y < HEIGHT and 0 <= x < WIDTH:
                    temp[y][x] = cell

    for row in temp:
        st.write("".join(row))

def collision(board, block, dx=0, dy=0):
    for i, row in enumerate(block["shape"]):
        for j, cell in enumerate(row):
            if cell == "⬜":
                continue
            x = block["x"] + j + dx
            y = block["y"] + i + dy

            if x < 0 or x >= WIDTH or y >= HEIGHT:
                return True
            if y >= 0 and board[y][x] != EMPTY:
                return True
    return False

def merge(board, block):
    for i, row in enumerate(block["shape"]):
        for j, cell in enumerate(row):
            if cell != "⬜":
                x = block["x"] + j
                y = block["y"] + i
                if 0 <= y < HEIGHT:
                    board[y][x] = cell

def clear_lines(board):
    new_board = [row for row in board if any(cell == EMPTY for cell in row)]
    lines_cleared = HEIGHT - len(new_board)

    for _ in range(lines_cleared):
        new_board.insert(0, [EMPTY]*WIDTH)

    return new_board, lines_cleared

# 세션 상태 초기화
if "board" not in st.session_state:
    st.session_state.board = create_board()
    st.session_state.block = new_block()
    st.session_state.score = 0
    st.session_state.game_over = False

board = st.session_state.board
block = st.session_state.block

# 게임 오버 체크
if collision(board, block):
    st.error("💀 게임 오버!")
    st.balloons()
    st.session_state.game_over = True

# 화면 출력
draw_board(board, block)

# 점수
st.markdown(f"### 🏆 점수: {st.session_state.score}")

# 버튼 UI
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ 왼쪽"):
        if not collision(board, block, dx=-1):
            block["x"] -= 1

with col2:
    if st.button("⬇️ 아래"):
        if not collision(board, block, dy=1):
            block["y"] += 1

with col3:
    if st.button("➡️ 오른쪽"):
        if not collision(board, block, dx=1):
            block["x"] += 1

# 자동 낙하
time.sleep(0.3)

if not collision(board, block, dy=1):
    block["y"] += 1
else:
    merge(board, block)
    board, cleared = clear_lines(board)

    if cleared > 0:
        st.success(f"🎉 {cleared}줄 제거!")
        st.balloons()
        st.session_state.score += cleared * 10

    st.session_state.block = new_block()

# 다시 실행
st.rerun()
