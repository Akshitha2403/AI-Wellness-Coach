import streamlit as st
import pandas as pd
import plotly.express as px


from utils.database import get_progress


# =====================================================
# PAGE CONFIG
# =====================================================


st.set_page_config(
    page_title="Analytics | WellnessAI",
    page_icon="📊",
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


# =====================================================
# LOAD DATA
# =====================================================


records = get_progress(
    email
)


if not records:
    st.info(
        "No progress data found 🌱 Complete today's tasks first."
    )
    st.stop()


df = pd.DataFrame(
    records
)


df["date"] = pd.to_datetime(
    df["date"]
)


df = df.sort_values(
    "date"
)


# =====================================================
# CSS
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
#ffe0f3,
transparent 35%
),

radial-gradient(
circle at bottom right,
#dffff0,
transparent 35%
),

radial-gradient(
circle at center,
#fff7cc,
transparent 45%
),

linear-gradient(
135deg,
#fff8fc,
#f7fff9
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

fade 1s ease;

}

.subtitle{

text-align:center;

font-size:22px;

font-weight:500;

color:#666;

}

/* =====================================================
   ANALYTICS CARDS
===================================================== */

.card{

background:

rgba(255,255,255,0.9);

padding:30px;

border-radius:35px;

text-align:center;

box-shadow:

0px 15px 40px rgba(0,0,0,0.08);

transition:

0.3s ease;

border:

2px solid rgba(255,255,255,0.8);

}

.card:hover{

transform:

translateY(-10px)
scale(1.04);

box-shadow:

0px 20px 45px rgba(255,130,180,0.25);

}

.card h3{

font-size:23px;

color:#555;

}

.card h2{

font-size:40px;

font-weight:900;

background:

linear-gradient(

90deg,

#ff7eb3,

#48d884

);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}

/* =====================================================
   CHART CARDS
===================================================== */

[data-testid="stPlotlyChart"]{

background:white;

padding:30px;

border-radius:35px;

box-shadow:

0px 15px 40px rgba(0,0,0,0.08);

}

/* =====================================================
   HEADINGS
===================================================== */

h2,h3{

color:#42bd78;

font-weight:900;

}

/* =====================================================
   MESSAGE BOXES
===================================================== */

[data-testid="stAlert"]{

border-radius:25px;

box-shadow:

0px 12px 35px rgba(0,0,0,0.08);

font-size:18px;

}

/* =====================================================
   ANIMATION
===================================================== */

@keyframes fade{

from{

opacity:0;

transform:

translateY(-30px);

}

to{

opacity:1;

transform:

translateY(0);

}

}

</style>
""",
unsafe_allow_html=True
)


# =====================================================
# TITLE
# =====================================================


st.markdown(
"""
<div class="title">

📊 Wellness Analytics

</div>

<div class="subtitle">

Track your consistency and celebrate your growth 🌿

</div>

<br>

""",
unsafe_allow_html=True
)


# =====================================================
# CALCULATIONS
# =====================================================


average_score = round(
    df["completion_percentage"].mean(),
    2
)


active_days = len(
    df
)


total_habits = (

    df["exercise_completed"].sum()

    +

    df["water_completed"].sum()

    +

    df["diet_completed"].sum()

    +

    df["sleep_completed"].sum()

    +

    df["meditation_completed"].sum()

)



# =====================================================
# TOP CARDS
# =====================================================


c1,c2,c3 = st.columns(3)



with c1:

    st.markdown(
        f"""
        <div class="card">

        <h3>💚 Average Consistency</h3>

        <h2>{average_score}%</h2>

        </div>
        """,
        unsafe_allow_html=True
    )



with c2:

    st.markdown(
        f"""
        <div class="card">

        <h3>🔥 Active Days</h3>

        <h2>{active_days}</h2>

        </div>
        """,
        unsafe_allow_html=True
    )



with c3:

    st.markdown(
        f"""
        <div class="card">

        <h3>🌿 Habits Completed</h3>

        <h2>{total_habits}</h2>

        </div>
        """,
        unsafe_allow_html=True
    )



st.write("---")

# =====================================================
# PROGRESS LINE CHART
# =====================================================


st.subheader(
    "📈 Wellness Progress Trend"
)


line = px.line(
    df,
    x="date",
    y="completion_percentage",
    markers=True,
)


line.update_layout(
    yaxis_title="Completion %",
    xaxis_title="Date"
)


st.plotly_chart(
    line,
    use_container_width=True
)


# =====================================================
# TASK CONSISTENCY
# =====================================================


st.subheader(
    "🌿 Habit Consistency"
)


task_data = pd.DataFrame(
    {
        "Habit":[
            "Workout 🏋️",
            "Water 💧",
            "Diet 🥗",
            "Sleep 😴",
            "Meditation 🧘"
        ],
        "Completed":[
            df["exercise_completed"].sum(),
            df["water_completed"].sum(),
            df["diet_completed"].sum(),
            df["sleep_completed"].sum(),
            df["meditation_completed"].sum()
        ]
    }
)


bar = px.bar(
    task_data,
    x="Habit",
    y="Completed"
)


st.plotly_chart(
    bar,
    use_container_width=True
)




# =====================================================
# AI STYLE INSIGHT
# =====================================================


st.write("---")


if average_score >= 80:
    st.success(
        """
        🌟 Excellent consistency!

        You are maintaining a very healthy lifestyle.
        Keep following your routine 💚
        """
    )


elif average_score >= 50:
    st.info(
        """
        🌿 Good improvement!

        Your habits are growing stronger.
        Try reaching 80% consistency next 🚀
        """
    )


else:
    st.warning(
        """
        🌱 Your wellness journey has started.

        Small daily improvements create big results.
        Keep going 💚
        """
    )