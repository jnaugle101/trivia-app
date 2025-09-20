import random
import re
import streamlit as st
import difflib
import math

# ✅ Import YOUR question bank (a dict: question -> answer)
from Trivia_Game import questions  # make sure Trivia_Game.py does NOT auto-run

ALIASES = {
    "united states": {"usa", "u s a", "u.s.", "us", "u.s.a", "united states of america"},
    "new york city": {"nyc", "new york", "ny"},
    "007": {"james bond", "bond"},
    "bible": {"the bible", "holy bible"},
    "Alabama": {"AL"},
    "Alaska": {"AK"},
    "Arizona": {"AZ"},
    "Arkansas": {"AR"},
    "California": {"CA"},
    "Colorado": {"CO"},
    "Connecticut": {"CT"},
    "Delaware": {"DE"},
    "Florida": {"FL"},
    "Georgia": {"GA"},
    "Hawaii": {"HI"},
    "Idaho": {"ID"},
    "Illinois": {"IL"},
    "Indiana": {"IN"},
    "Iowa": {"IA"},
    "Kansas": {"KS"},
    "Kentucky": {"KY"},
    "Louisiana": {"LA"},
    "Maine": {"ME"},
    "Maryland": {"MD"},
    "Massachusetts": {"MA"},
    "Michigan": {"MI"},
    "Minnesota": {"MN"},
    "Mississippi": {"MS"},
    "Missouri": {"MO"},
    "Montana": {"MT"},
    "Nebraska": {"NE"},
    "Nevada": {"NV"},
    "New Hampshire": {"NH"},
    "New Jersey": {"NJ"},
    "New Mexico": {"NM"},
    "New York": {"NY"},
    "North Carolina": {"NC"},
    "North Dakota": {"ND"},
    "Ohio": {"OH"},
    "Oklahoma": {"OK"},
    "Oregon": {"OR"},
    "Pennsylvania": {"PA"},
    "Rhode Island": {"RI"},
    "South Carolina": {"SC"},
    "South Dakota": {"SD"},
    "Tennessee": {"TN"},
    "Texas": {"TX"},
    "Utah": {"UT"},
    "Vermont": {"VT"},
    "Virginia": {"VA"},
    "Washington": {"WA"},
    "West Virginia": {"WV"},
    "Wisconsin": {"WI"},
    "Wyoming": {"WY"},
    # DC (normalize() strips punctuation)
    "Washington, DC": {"DC", "Washington DC", "District of Columbia"},
    # Countries / blocs
    "United Kingdom": {"UK", "U.K.", "Great Britain", "Britain"},
    "United Arab Emirates": {"UAE"},
    "Soviet Union": {"USSR", "Union of Soviet Socialist Republics"},
    "European Union": {"EU"},
    "United Nations": {"UN"},
    "Ivory Coast": {"Cote d'Ivoire", "Côte d'Ivoire"},
    "Netherlands": {"Holland", "The Netherlands"},
    "Myanmar": {"Burma"},
    "Czechia": {"Czech Republic"},
    "Eswatini": {"Swaziland"},
    "Cape Verde": {"Cabo Verde"},
    "East Timor": {"Timor-Leste", "Timor Leste"},
    "South Korea": {"ROK", "Republic of Korea"},
    "North Korea": {"DPRK", "Democratic People's Republic of Korea"},

    # Major cities (common nicknames/abbr.)
    "Los Angeles": {"LA", "L.A."},
    "San Francisco": {"SF", "S.F.", "San Fran"},
    "Philadelphia": {"Philly"},
    "Las Vegas": {"Vegas"},
    "New Orleans": {"NOLA"},
    "Atlanta": {"ATL"},
    "Saint Louis": {"St Louis", "St. Louis"},
    "Saint Petersburg": {"St Petersburg", "St. Petersburg"},

    # People / initials
    "John F. Kennedy": {"JFK"},
    "Franklin D. Roosevelt": {"FDR"},
    "Martin Luther King Jr.": {"MLK", "Dr Martin Luther King Jr", "Dr. Martin Luther King Jr"},

    # Entertainment shorthands
    "Lord of the Rings": {"LOTR"},
    "Game of Thrones": {"GOT"},
    "Harry Potter": {"HP"},
    "Back to the Future": {"BTTF"},
    "AC/DC": {"ACDC"},
}

# ---- Page setup ----
st.set_page_config(page_title="Trivia Game", page_icon="❓")
st.title("❓ Trivia Game")

# ---- Quick reset so the start screen (rules) shows again ----
if st.button("🔄 New Game / Show Rules"):
    st.session_state.started = False
    st.session_state.index = 0
    st.session_state.order = []
    st.session_state.history = []
    st.rerun()

# Always show rules in the sidebar too (handy during the quiz)
with st.sidebar:
    st.header("📋 Rules")
    st.markdown("""
    - Numeric answers are **digits** (e.g., `1`, `2`, `1985`)
    - **Case-insensitive**, but spelling matters
    - Comma/“or” answers: **any one** counts
    - Review at the end; **Quit** anytime
    """)

# ---- Helpers ----
def normalize(s: str) -> str:
    """Lowercase, trim, replace common symbols, remove punctuation, collapse spaces."""
    s = s.lower().strip()

    # Common replacements
    s = s.replace("&", "and")          # treat "&" as "and"
    s = s.replace("’", "'")            # smart apostrophe → normal
    s = s.replace("´", "'")
    s = s.replace("`", "'")

    # Remove punctuation but keep letters/numbers/spaces
    s = re.sub(r"[^\w\s]", " ", s)

    # Collapse extra spaces
    s = re.sub(r"\s+", " ", s)
    # Strip leading "the "
    if s.startswith("the "):
        s = s[4:]

    return s

def alias_match(user_norm: str, correct_raw: str) -> bool:
    c_norm = normalize(correct_raw)
    for key, variants in ALIASES.items():
        if normalize(key) == c_norm:
            if any(user_norm == normalize(v) for v in variants):
                return True
    return False

def is_correct(user: str, correct: str) -> bool:
    """
    Accepts minor variations. If the correct answer contains 'or' or commas,
    match any of the parts (e.g., 'Green or red', 'Cancer, Pisces, Scorpio').
    """
    u = normalize(user)
    c = normalize(correct)
    if alias_match(u, correct):
        return True
    parts = re.split(r"\bor\b|,|/|;", c)
    parts = [p.strip() for p in parts if p.strip()] or [c]

    for p in parts:
        if u == p:
            return True
        if len(p) <= 3:  # super-short answers must match exactly
            continue
        ratio = difflib.SequenceMatcher(None, u, p).ratio()
        thresh = 0.88 if len(p) <= 6 else 0.8
        if ratio >= thresh:
            return True
    return False

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
    # ✅ Rules visible when the app first opens
    with st.expander("📋 Rules & Tips", expanded=True):
        st.markdown("""
        - **Numeric answers must be digits** (e.g., `1`, `2`, `1985`).
        - **Spelling counts** (answers are **case-insensitive**, but spelling matters).
        - Some answers have options (e.g., **“Green or red”** or **comma-separated** lists) — any listed option counts.
        - You’ll get a full review at the end; you can **Quit** anytime.
        """)

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

        needed = math.ceil(total * 0.70)  # 70% rule (your choice)
        if score >= needed:
            st.info("🌟 Excellent! You are Smarter than most!")
        else:
            st.warning(f"😬 Not quite Loser. You needed at least {needed}/{total} (70%).")

        st.markdown("### Review answers")
        st.write(f"✅ Correct: {right} ❌ Incorrect: {total - right}")

        # Always show each question + user answer + correct answer (no expanders)
        for idx, h in enumerate(st.session_state.history, start=1):
            icon = "✅" if h["is_correct"] else "❌"
            st.markdown(
                f"**Q{idx} {icon}**  \n"
                f"{h['q']}  \n"
                f"**Your answer:** {h['user']}  \n"
                f"**Correct answer:** {h['correct']}"
            )

        if st.button("Play again"):
            st.session_state.started = False
            st.session_state.index = 0
            st.session_state.order = []
            st.session_state.history = []
            st.rerun()
