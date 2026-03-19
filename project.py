import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="🎨 그림판 앱", page_icon="🎨")

st.title("🎨 귀여운 그림판 앱")
st.write("마우스로 좌표를 클릭해서 그림을 그려보세요! ✨")

# 세션 상태 초기화
if "points" not in st.session_state:
    st.session_state.points = []

if "image" not in st.session_state:
    st.session_state.image = Image.new("RGB", (400, 400), "white")

# 🎨 설정 UI
col1, col2 = st.columns(2)

with col1:
    color = st.color_picker("🎨 색상 선택", "#000000")

with col2:
    size = st.slider("✏️ 선 굵기", 1, 20, 5)

# 클릭 좌표 입력 (대체 방식)
x = st.number_input("X 좌표", 0, 399, 0)
y = st.number_input("Y 좌표", 0, 399, 0)

# 그림 그리기
if st.button("✏️ 점 찍기"):
    draw = ImageDraw.Draw(st.session_state.image)
    draw.ellipse(
        (x-size, y-size, x+size, y+size),
        fill=color
    )
    st.session_state.points.append((x, y))

# 이미지 표시
st.image(st.session_state.image, caption="🖼️ 당신의 작품")

# 기능 버튼
col3, col4 = st.columns(2)

with col3:
    if st.button("🧹 초기화"):
        st.session_state.image = Image.new("RGB", (400, 400), "white")
        st.session_state.points = []
        st.success("캔버스를 깨끗하게 만들었어요! ✨")

with col4:
    if st.button("💾 저장"):
        st.session_state.image.save("my_drawing.png")
        st.success("저장 완료! 🎉")
        st.balloons()

# 안내
st.markdown("---")
st.info("💡 팁: 여러 점을 찍어서 그림을 완성해보세요!")
