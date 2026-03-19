import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🎮 Keyboard Dodge Game", page_icon="🎯")

st.title("🎮 키보드 피하기 게임")
st.markdown("👉 방향키 ⬅️ ➡️ 로 움직여서 떨어지는 장애물을 피하세요!")

game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        text-align: center;
        background-color: #111;
        color: white;
        font-family: sans-serif;
    }
    canvas {
        background-color: black;
        margin-top: 10px;
        border: 2px solid white;
    }
</style>
</head>
<body>

<canvas id="game" width="300" height="400"></canvas>
<h3 id="score">⭐ 점수: 0</h3>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

let playerX = 140;
let obstacles = [];
let score = 0;
let gameOver = false;

// 키보드 입력
document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") {
        playerX -= 20;
    }
    if (e.key === "ArrowRight") {
        playerX += 20;
    }
});

// 장애물 생성
function spawnObstacle() {
    let x = Math.floor(Math.random() * 15) * 20;
    obstacles.push({x: x, y: 0});
}

// 게임 루프
function update() {
    if (gameOver) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 플레이어
    ctx.fillStyle = "cyan";
    ctx.fillRect(playerX, 360, 20, 20);

    // 장애물
    ctx.fillStyle = "red";
    for (let i = 0; i < obstacles.length; i++) {
        obstacles[i].y += 5;
        ctx.fillRect(obstacles[i].x, obstacles[i].y, 20, 20);

        // 충돌 체크
        if (
            obstacles[i].y > 340 &&
            obstacles[i].x === playerX
        ) {
            gameOver = true;
            document.getElementById("score").innerText = "💥 게임 오버! 점수: " + score;

            // 풍선 효과 (Streamlit과 통신)
            window.parent.postMessage({type: "streamlit:balloons"}, "*");
        }
    }

    // 점수 증가
    score++;
    document.getElementById("score").innerText = "⭐ 점수: " + score;

    // 랜덤 생성
    if (Math.random() < 0.05) {
        spawnObstacle();
    }

    requestAnimationFrame(update);
}

// 시작
update();
</script>

</body>
</html>
"""

components.html(game_html, height=500)
