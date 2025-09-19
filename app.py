import random
import re
import streamlit as st

# ✅ Import YOUR question bank (a dict: question -> answer)
from Trivia_Game import questions  # make sure Trivia_Game.py does NOT auto-run

# ---- Page setup ----
st.set_page_config(page_title="Trivia Game", page_icon="❓")
st.title("❓ Trivia Game")

# ---- Helpers ----
def normalize(s: str) -> str:
    """Lowercase, trim, remove punctuation, collapse spaces."""
    s = s.lower().strip()
    s = re.sub(r"[^\w\s]", "", s)   # remove punctuation
    s = re.sub(r"\s+", " ", s)     # collapse multiple spaces
    return s

def is_correct(user: str, correct: str) -> bool:
    """
    Accepts minor variations. If the correct answer contains 'or' or commas,
    match any of the parts (e.g., 'Green or red', 'Cancer, Pisces, Scorpio').
    """
    u = normalize(user)
    c = normalize(correct)
    parts = re.split(r"\bor\b|,", c)
    parts = [p.strip() for p in parts if p.strip()] or [c]
    return any(u == p for p in parts)

# ---- Session state ----
if "started" not in st.session_state:
    st.session_state.started = False
if "index" not in st.session_state:
    st.session_state.index = 0
if "order" not in st.session_state:
    st.session_state.order = []     # list of questions in play-order
if "history" not in st.session_state:
    st.session_state.history = []   # list of dicts: {q, user, correct, is_correct}

# ---- Start screen ----
if not st.session_state.started:
    total_available = len(questions)
    num_default = min(10, total_available)
    num_q = st.slider("How many questions?", 1, total_available, num_default)
    if st.button("Start"):
        st.session_state.order = random.sample(list(questions.keys()), k=num_q)
        st.session_state.history = []
        st.session_state.index = 0
        st.session_state.started = True
        st.rerun()

# ---- Game flow ----
else:
    i = st.session_state.index
    total = len(st.session_state.order)

    if i < total:
        q = st.session_state.order[i]
        correct = questions[q]

        st.subheader(f"Question {i + 1} of {total}")
        st.write(q)

        ans = st.text_input("Your answer:", key=f"ans_{i}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Submit", key=f"submit_{i}"):
                if not ans.strip():
                    st.warning("Please type an answer.")
                else:
                    ok = is_correct(ans, correct)
                    # Record but DO NOT reveal correctness now (review at end)
                    st.session_state.history.append({
                        "q": q,
                        "user": ans,
                        "correct": correct,
                        "is_correct": ok
                    })
                    st.session_state.index += 1
                    st.rerun()
        with col2:
            if st.button("Quit"):
                st.session_state.started = False
                st.rerun()

        st.progress(i / total if total else 0)

    else:
        # ---- End screen with score, percentage, and full review ----
        right = sum(1 for h in st.session_state.history if h["is_correct"])
        score = right
        percentage = (score / total) * 100 if total else 0.0

        st.success(f"Game over! Your score: {score}/{total} ({percentage:.2f}%)")

        if percentage > 80:
            st.info("🌟 Excellent!")
        else:
            st.warning("😬 Loser")

        st.markdown("### Review answers")
        st.write(f"✅ Correct: {right} ❌ Incorrect: {total - right}")

        for idx, h in enumerate(st.session_state.history, start=1):
            with st.expander(f"Q{idx}: {'✅' if h['is_correct'] else '❌'}"):
                st.write(h["q"])
                st.write(f"**Your answer:** {h['user']}")
                st.write(f"**Correct answer:** {h['correct']}")

        if st.button("Play again"):
            st.session_state.started = False
            st.session_state.index = 0
            st.session_state.order = []
            st.session_state.history = []
            st.rerun()
