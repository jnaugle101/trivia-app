import random
import re
import streamlit as st

# ⬇️ import YOUR data (dict: question -> answer)
from Trivia_Game import questions  # your original dict

st.set_page_config(page_title="Trivia Game", page_icon="❓")
st.title("❓ Trivia Game")

# --- helpers ---
def normalize(s: str) -> str:
    # lower, strip spaces, collapse multiple spaces, remove basic punctuation
    s = s.lower().strip()
    s = re.sub(r"[^\w\s]", "", s)     # remove punctuation
    s = re.sub(r"\s+", " ", s)        # collapse spaces
    return s

def is_correct(user, correct):
    """
    Allows multiple valid variants like 'green or red', 'cancer, pisces, scorpio',
    etc. Splits on common separators and checks each option.
    """
    u = normalize(user)
    c = normalize(correct)

    # split possible multiple answers
    # treat "or" and commas as separators
    parts = re.split(r"\bor\b|,", c)
    parts = [p.strip() for p in parts if p.strip()]
    if not parts:
        parts = [c]

    # exact match against any acceptable variant
    return any(u == p for p in parts)

# --- session state ---
if "started" not in st.session_state:
    st.session_state.started = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "index" not in st.session_state:
    st.session_state.index = 0
if "order" not in st.session_state:
    st.session_state.order = []

# --- start screen ---
if not st.session_state.started:
    total_available = len(questions)
    num_q = st.slider("How many questions?", 1, total_available, min(10, total_available))
    if st.button("Start"):
        st.session_state.order = random.sample(list(questions.keys()), k=num_q)
        st.session_state.score = 0
        st.session_state.index = 0
        st.session_state.started = True
        st.rerun()

# --- game flow ---
else:
    i = st.session_state.index
    total = len(st.session_state.order)

    if i < total:
        q = st.session_state.order[i]
        correct = questions[q]

        st.subheader(f"Question {i+1} of {total}")
        st.write(q)

        ans = st.text_input("Your answer:", key=f"ans_{i}")

        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("Submit", key=f"submit_{i}"):
                if not ans.strip():
                    st.warning("Please type an answer.")
                else:
                    if is_correct(ans, correct):
                        st.success(f"✅ Correct!  ({correct})")
                        st.session_state.score += 1
                    else:
                        st.error(f"❌ Incorrect. Correct answer: {correct}")
                    st.session_state.index += 1
                    st.rerun()
        with col2:
            if st.button("Quit"):
                st.session_state.started = False
                st.rerun()

        st.progress(i/total if total else 0)
    else:
        st.success(f"Game over! Your score: {st.session_state.score}/{total}")
        if st.button("Play again"):
            st.session_state.started = False
            st.rerun()
