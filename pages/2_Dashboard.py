import streamlit as st
import plotly.express as px
import pandas as pd


from utils.database import (
    get_profile,
    save_wellness_record,
    get_latest_wellness_record,
    update_wellness_record
)


from utils.prediction import predict_workout_intensity


from utils.gemini_service import generate_wellness_plan


# =====================================================
# PAGE CONFIG
# =====================================================


st.set_page_config(
    page_title="Dashboard | WellnessAI",
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


# =====================================================
# LOAD PROFILE
# =====================================================


profile = get_profile(
    email
)


if profile is None:
    st.warning(
        "Please create your profile first 🌿"
    )
    st.stop()


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
#ffdff1,
transparent 35%
),

radial-gradient(
circle at bottom right,
#dffff0,
transparent 35%
),

radial-gradient(
circle at center,
#fff6cf,
transparent 40%
),

linear-gradient(
135deg,
#fff8fc,
#f8fff7
);

}

/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {

background:

linear-gradient(

180deg,

#ffe4f3,

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

#91f5a8

);

border-radius:25px;

box-shadow:

0px 8px 25px rgba(255,120,180,0.3);

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
#ff74b8,
#3edb82
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;

animation:

slide 1s ease;

}

.subtitle{

text-align:center;
font-size:22px;
font-weight:500;
color:#666;

}

/* =====================================================
   HEALTH CARDS
===================================================== */

.card{

background:

rgba(255,255,255,0.85);

padding:30px;

border-radius:30px;

text-align:center;

box-shadow:

0px 15px 35px rgba(0,0,0,0.08);

transition:0.3s;

border:

2px solid rgba(255,255,255,0.7);

}

.card:hover{

transform:

translateY(-8px)
scale(1.03);

box-shadow:

0px 20px 45px rgba(255,130,180,0.25);

}

.card h3{

font-size:25px;
color:#555;

}

.card h2{

font-size:35px;

background:

linear-gradient(

90deg,

#ff78b5,

#48d884

);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;

font-weight:900;

}

/* =====================================================
   AI PLAN BOX
===================================================== */

.ai-box{

background:

rgba(255,255,255,0.85);

padding:40px;

border-radius:35px;

font-size:18px;

line-height:1.8;

box-shadow:

0px 15px 40px rgba(0,0,0,0.08);

border-left:

10px solid #ff9acb;

white-space:pre-wrap;

}

/* =====================================================
   CHART CONTAINER
===================================================== */

[data-testid="stPlotlyChart"]{

background:white;

padding:25px;

border-radius:35px;

box-shadow:

0px 15px 40px rgba(0,0,0,0.08);

}

/* =====================================================
   BUTTON
===================================================== */

div.stButton button{

height:55px;

border-radius:35px;

background:

linear-gradient(

90deg,

#ff8ec7,

#8ff5a2

);

color:white;

font-size:18px;

font-weight:900;

border:none;

box-shadow:

0px 12px 30px rgba(255,120,180,0.35);

transition:0.3s;

}

div.stButton button:hover{

transform:

scale(1.05);

}

/* =====================================================
   HEADINGS
===================================================== */

h2,h3{

color:#44b875;
font-weight:900;

}

@keyframes slide{

from{

opacity:0;
transform:translateY(-30px);

}

to{

opacity:1;
transform:translateY(0);

}

}

/* =====================================================
   MOBILE RESPONSIVE FIX
===================================================== */

@media only screen and (max-width: 768px){

.stApp{

background:

linear-gradient(
135deg,
#fff7fb,
#f2fff7,
#fffbea
) !important;

}

/* all text visible */

h1,h2,h3,h4,h5,h6,
p,label,span,div{

color:#333333 !important;

}

/* title fix */

.title{

font-size:35px !important;

color:#333333 !important;

-webkit-text-fill-color:#333333 !important;

}

/* subtitle */

.subtitle{

font-size:16px !important;

color:#555 !important;

}

/* cards */

.card{

width:100% !important;

padding:20px !important;

margin-bottom:20px !important;

background:white !important;

}

/* AI box */

.ai-box{

background:white !important;

color:#333333 !important;

font-size:16px !important;

padding:20px !important;

border-radius:25px !important;

}

/* inputs */

input,
textarea{

color:#222 !important;

background:white !important;

}

/* dropdown */

div[data-baseweb="select"]{

background:white !important;

color:#222 !important;

}

/* buttons */

.stButton button{

width:100% !important;

font-size:16px !important;

}

/* plotly charts */

[data-testid="stPlotlyChart"]{

overflow-x:auto !important;

padding:10px !important;

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

🌿 WellnessAI Dashboard

</div>

<div class="subtitle">

Your personalized AI health companion 💚

</div>

<br>

""",
unsafe_allow_html=True
)


# =====================================================
# ML INPUT
# =====================================================


gender_value = (
    "M"
    if profile["gender"] == "Male"
    else "F"
)


# =====================================================
# FIX HEALTH CONDITIONS FORMAT
# =====================================================


health_data = profile["health_conditions"]


if isinstance(
    health_data,
    list
):

    health_value = health_data


elif isinstance(
    health_data,
    str
):

    health_value = health_data.split(",")


else:

    health_value = "None"


ml_input = {
    "age": profile["age"],
    "gender": gender_value,
    "height_cm": profile["height"],
    "weight_kg": profile["weight"],
    "BMI": profile["bmi"],
    "body fat_%": profile["body_fat"],
    "diastolic": profile["diastolic"],
    "systolic": profile["systolic"],
    "Health_Condition": health_value,
    "Profession": profile["profession"],
    "Stress_Level": profile["stress_level"],
    "Fitness_Goal": profile["fitness_goal"],
    "Available_Time": profile["available_time"]
}


# =====================================================
# GET OLD RECORD
# =====================================================


old_record = get_latest_wellness_record(
    email
)


# =====================================================
# GENERATE / LOAD AI PLAN
# =====================================================


regenerate = st.button(
    "🔄 Regenerate AI Wellness Plan"
)


if old_record and not regenerate:
    workout_intensity = old_record["workout_intensity"]
    ai_plan = old_record["ai_plan"]


else:
    with st.spinner(
        "Creating your personalized AI plan 🌿"
    ):
        workout_intensity = predict_workout_intensity(
            ml_input
        )

        ai_plan = generate_wellness_plan(
            profile["name"],
            profile["age"],
            profile["gender"],
            profile["bmi"],
            profile["calories"],
            profile["profession"],
            profile["stress_level"],
            profile["fitness_goal"],
            profile["food_preference"],
            profile["health_conditions"],
            workout_intensity
        )

        record = {
            "user_email":email,
            "bmi":profile["bmi"],
            "bmr":profile["bmr"],
            "daily_calories":profile["calories"],
            "workout_intensity":workout_intensity,
            "ai_plan":ai_plan
        }

        if old_record:
            update_wellness_record(
                email,
                record
            )
        else:
            save_wellness_record(
                record
            )


# =====================================================
# HEALTH CARDS
# =====================================================


c1,c2,c3,c4 = st.columns(4)


with c1:
    st.markdown(
        f"""
        <div class="card">
        <h3>💗 BMI</h3>
        <h2>{profile['bmi']}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


with c2:
    st.markdown(
        f"""
        <div class="card">
        <h3>🔥 BMR</h3>
        <h2>{profile['bmr']}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


with c3:
    st.markdown(
        f"""
        <div class="card">
        <h3>🥗 Calories</h3>
        <h2>{profile['calories']}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


with c4:
    st.markdown(
        f"""
        <div class="card">
        <h3>🏋️ Level</h3>
        <h2>{workout_intensity}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("---")


# =====================================================
# PERSONALIZED NUTRITION CHART
# =====================================================


st.subheader(
    "🥗 Personalized Nutrition Distribution"
)


goal = profile["fitness_goal"]


if goal == "Weight Loss":

    protein = 40
    carbs = 35
    fats = 25


elif goal == "Muscle Building":

    protein = 35
    carbs = 45
    fats = 20


elif goal == "Weight Gain":

    protein = 30
    carbs = 50
    fats = 20


else:

    protein = 30
    carbs = 40
    fats = 30


nutrition = pd.DataFrame(
    {
        "Type":[
            "Protein 🥩",
            "Carbohydrates 🍚",
            "Healthy Fats 🥑"
        ],

        "Value":[
            protein,
            carbs,
            fats
        ]
    }
)


fig = px.pie(
    nutrition,
    values="Value",
    names="Type",
    hole=0.55,

    color_discrete_sequence=[
        "#ff9acb",
        "#8ff5a2",
        "#ffe680"
    ]
)


fig.update_layout(
    showlegend=True,
    height=500
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# =====================================================
# AI PLAN
# =====================================================


st.subheader(
    "🤖 Your AI Generated Wellness Plan"
)


st.markdown(
    f"""
    <div class="ai-box">
    {ai_plan}
    </div>
    """,
    unsafe_allow_html=True
)