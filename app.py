import streamlit as st
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# ---------------- DARK MODE ----------------
dark_mode = st.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown("""
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🎮 Rock Paper Scissors")
st.subheader("Made by Aditya Mohanani")
st.write("Play against the computer and track your score!")

# ---------------- CHOICES ----------------
choices = {
    1: "📄 Paper",
    2: "✂️ Scissor",
    3: "🪨 Rock"
}

player_choice = st.radio(
    "Choose your move:",
    options=list(choices.keys()),
    format_func=lambda x: choices[x],
    horizontal=True
)

# ---------------- PLAY BUTTON ----------------
if st.button("▶️ Play", use_container_width=True):

    with st.spinner("Computer is thinking..."):
        time.sleep(1)

    computer_choice = random.randint(1, 3)

    st.markdown("### 🔍 Result")
    st.write(f"**You:** {choices[player_choice]}")
    st.write(f"**Computer:** {choices[computer_choice]}")

    # ---------------- GAME LOGIC ----------------
    if player_choice == computer_choice:
        st.info("🤝 It's a Tie!")

    elif (
        (player_choice == 1 and computer_choice == 3) or
        (player_choice == 2 and computer_choice == 1) or
        (player_choice == 3 and computer_choice == 2)
    ):
        st.success("🎉 YOU WON!")
        st.session_state.player_score += 1
        st.balloons()
        st.audio("https://www.soundjay.com/buttons/sounds/button-4.mp3")

    else:
        st.error("😢 YOU LOST!")
        st.session_state.computer_score += 1
        st.audio("https://www.soundjay.com/buttons/sounds/button-10.mp3")

# ---------------- SCOREBOARD ----------------
st.markdown("---")
st.markdown("## 📊 Score Board")

col1, col2 = st.columns(2)
col1.metric("👤 You", st.session_state.player_score)
col2.metric("🤖 Computer", st.session_state.computer_score)

# ---------------- RESET ----------------
if st.button("🔄 Reset Score"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.success("Score reset successfully!")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Web App | Python + Streamlit | Aditya Mohanani")
