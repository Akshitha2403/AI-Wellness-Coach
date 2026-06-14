import streamlit as st


from datetime import date


from utils.database import (
    save_progress,
    get_today_progress,
    update_today_progress
)


# =====================================================
# PAGE CONFIG
# =====================================================


st.set_page_config(
    page_title="Progress | WellnessAI",
    page_icon="🌿",
    layout="wide"
)


# =====================================================
# LOGIN CHECK
# =====================================================


if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning(
        "Please login first 🌿"
    )
    st.stop()


email = st.session_state.email


today = str(
    date.today()
)


# =====================================================
# CSS DESIGN
# =====================================================


st.markdown(
"""
<style>

/* =====================================================
   MAIN BACKGROUND
===================================================== */

.stApp{

background:

radial-gradient(
circle at top left,
#ffdff2,
transparent 35%
),

radial-gradient(
circle at bottom right,
#dffff0,
transparent 35%
),

radial-gradient(
circle at center,
#fff5c9,
transparent 45%
),

linear-gradient(
135deg,
#fff7fb,
#f6fff8
);

}

/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {

background:

linear-gradient(

180deg,

#ffe5f4,

#eaffef,

#fff8d8

);

border-radius:

0px 35px 35px 0px;

box-shadow:

8px 0px 30px rgba(0,0,0,0.08);

}

section[data-testid="stSidebar"] span{

font-size:18px;
font-weight:800;
color:#555;

}

section[data-testid="stSidebar"] [aria-current="page"]{

background:

linear-gradient(

90deg,

#ff91c8,

#8ff5a2

);

border-radius:25px;

box-shadow:

0px 8px 25px rgba(255,120,180,0.35);

}

section[data-testid="stSidebar"] [aria-current="page"] span{

color:white;

}

/* =====================================================
   TITLE
===================================================== */

.title{

font-size:60px;
font-weight:900;
text-align:center;

background:

linear-gradient(
90deg,
#ff70b8,
#3bd87f
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;

animation:

drop 1s ease;

}

.subtitle{

font-size:22px;
font-weight:500;
text-align:center;
color:#666;

}

/* =====================================================
   WELLNESS TASK CARDS
===================================================== */

.card{

height:160px;

background:

rgba(255,255,255,0.85);

border-radius:35px;

display:flex;

flex-direction:column;

justify-content:center;

align-items:center;

font-size:22px;

font-weight:900;

color:#555;

box-shadow:

0px 15px 35px rgba(0,0,0,0.08);

transition:

0.3s ease;

border:

2px solid rgba(255,255,255,0.8);

}

.card:hover{

transform:

translateY(-10px)
scale(1.05);

box-shadow:

0px 20px 45px rgba(255,130,180,0.25);

}

.icon{

font-size:65px;

margin-bottom:15px;

animation:

floatIcon 3s infinite ease-in-out;

}

/* =====================================================
   CHECKBOX
===================================================== */

.stCheckbox{

display:flex;

justify-content:center;

font-weight:800;

}

/* =====================================================
   PERCENTAGE DISPLAY
===================================================== */

.percent{

font-size:85px;

font-weight:900;

text-align:center;

background:

linear-gradient(

90deg,

#ff7eb3,

#45d483

);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

animation:

pulse 3s infinite;

}

/* =====================================================
   BUTTON
===================================================== */

div.stButton button{

height:60px;

border-radius:40px;

background:

linear-gradient(

90deg,

#ff8ec7,

#8ff5a2

);

color:white;

font-size:20px;

font-weight:900;

border:none;

box-shadow:

0px 12px 30px rgba(255,120,170,0.4);

transition:0.3s;

}

div.stButton button:hover{

transform:

scale(1.06);

}

/* =====================================================
   ALERT BOXES
===================================================== */

[data-testid="stAlert"]{

border-radius:25px;

font-size:18px;

box-shadow:

0px 10px 30px rgba(0,0,0,0.08);

}

/* =====================================================
   ANIMATIONS
===================================================== */

@keyframes floatIcon{

0%{

transform:translateY(0);

}

50%{

transform:translateY(-10px);

}

100%{

transform:translateY(0);

}

}

@keyframes pulse{

50%{

transform:scale(1.08);

}

}

@keyframes drop{

from{

opacity:0;
transform:translateY(-30px);

}

to{

opacity:1;
transform:translateY(0);

}

}

</style>
""",
unsafe_allow_html=True
)


# =====================================================
# HEADER
# =====================================================


st.markdown(
"""
<div class="title">

🌿 Daily Wellness Progress

</div>

<div class="subtitle">

Small steps everyday create a healthier you 💚

</div>

<br>

""",
unsafe_allow_html=True
)


# =====================================================
# CHECKLIST
# =====================================================


st.subheader(
    "Today's Wellness Checklist ✨"
)


c1,c2,c3,c4,c5 = st.columns(5)


with c1:
    st.markdown(
    """
    <div class="card">
    <div class="icon">🏋️‍♀️</div>
    Workout
    </div>
    """,
    unsafe_allow_html=True
    )

    exercise = st.checkbox(
        "Completed",
        key="exercise"
    )


with c2:
    st.markdown(
    """
    <div class="card">
    <div class="icon">💧</div>
    Hydration
    </div>
    """,
    unsafe_allow_html=True
    )

    water = st.checkbox(
        "Completed",
        key="water"
    )


with c3:
    st.markdown(
    """
    <div class="card">
    <div class="icon">🥗</div>
    Healthy Diet
    </div>
    """,
    unsafe_allow_html=True
    )

    diet = st.checkbox(
        "Completed",
        key="diet"
    )


with c4:
    st.markdown(
    """
    <div class="card">
    <div class="icon">😴</div>
    Sleep Goal
    </div>
    """,
    unsafe_allow_html=True
    )

    sleep = st.checkbox(
        "Completed",
        key="sleep"
    )


with c5:
    st.markdown(
    """
    <div class="card">
    <div class="icon">🧘‍♀️</div>
    Meditation
    </div>
    """,
    unsafe_allow_html=True
    )

    meditation = st.checkbox(
        "Completed",
        key="meditation"
    )


# =====================================================
# CALCULATE SCORE
# =====================================================


completed = sum(
    [
        exercise,
        water,
        diet,
        sleep,
        meditation
    ]
)


percentage = round(
    (completed/5)*100,
    2
)


st.markdown(
f"""
<div style="text-align:center">
<div class="percent">
{percentage}%
</div>
Daily Goal Completed 🌱
</div>
""",
unsafe_allow_html=True
)


# =====================================================
# SAVE / UPDATE TODAY
# =====================================================


a,b,c = st.columns(

    [1,1,1]

)


with b:
    if st.button(
        "Save Today's Progress 💚",
        use_container_width=True
    ):
        data = {
            "user_email":email,
            "exercise_completed":exercise,
            "water_completed":water,
            "diet_completed":diet,
            "sleep_completed":sleep,
            "meditation_completed":meditation,
            "completion_percentage":percentage,
            "date":today
        }

        existing = get_today_progress(
            email,
            today
        )

        if existing:
            update_today_progress(
                email,
                today,
                data
            )
        else:
            save_progress(
                data
            )

        # =====================================================
        # MOTIVATION
        # =====================================================

        if percentage == 100:
            st.success(
            """
            🎉 PERFECT WELLNESS DAY ACHIEVED 💚

            Amazing work! You completed every goal today 🌿

            Keep maintaining this healthy lifestyle ✨
            """
            )

            st.balloons()

        elif percentage == 80:
            st.info(
            """
            ⭐ Almost There Champion!

            Just one more habit left 🚀
            """
            )

        elif percentage == 60:
            st.info(
            """
            🌿 Great Progress!

            You are building consistency 💚
            """
            )

        elif percentage == 40:
            st.warning(
            """
            🌤️ Good Start!

            Complete a few more habits today 💪
            """
            )

        elif percentage == 20:
            st.warning(
            """
            🌧️ Small Step Started!

            Push yourself a little more 🌱
            """
            )

        else:
            st.error(
            """
            🌱 Your wellness journey is waiting!

            Start with one small habit 💚
            """
            )