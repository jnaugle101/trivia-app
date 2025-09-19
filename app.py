import streamlit as st

st.set_page_config(page_title="Trivia Game", page_icon="❓")

st.title("❓ Trivia Game")

# Simple demo question bank (edit/expand later)
QUESTIONS = [
    {
        "q": "Which language runs in a web browser?",
        "choices": ["Python", "Java", "C++", "JavaScript"],
        "answer": "JavaScript",
    },
    {
        "q": "What is the capital of Georgia (USA)?",
        "choices": ["Savannah", "Macon", "Atlanta", "Augusta"],
        "answer": "Atlanta",
    },
    {
        "q": "2 + 2 * 2 = ?",
        "choices": ["6", "8", "4", "2"],
        "answer": "6",
    },
]

if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0

def show_question(i):
    q = QUESTIONS[i]
    st.subheader(f"Question {i+1} of {len(QUESTIONS)}")
    choice = st.radio(q["q"], q["choices"], index=None)
    if st.button("Submit", key=f"submit_{i}"):
        if choice is None:
            st.warning("Please select an answer.")
        else:
            correct = (choice == q["answer"])
            if correct:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect. Correct answer: {q['answer']}")
            st.session_state.index += 1
            st.experimental_rerun()

# Game flow
if st.session_state.index < len(QUESTIONS):
    show_question(st.session_state.index)
else:
    st.success(f"Game over! Your score: {st.session_state.score}/{len(QUESTIONS)}")
    if st.button("Play again"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.experimental_rerun()
