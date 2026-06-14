import streamlit as st


from utils.database import (
    save_profile,
    get_profile,
    update_profile
)


# =====================================================
# PAGE CONFIG
# =====================================================


st.set_page_config(
    page_title="Profile | WellnessAI",
    page_icon="🌿",
    layout="wide"
)


# =====================================================
# LOGIN CHECK
# =====================================================


if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first 🌿")
    st.stop()


email = st.session_state.email


# =====================================================
# LOAD PROFILE
# =====================================================


profile = get_profile(email)


# =====================================================
# CALCULATIONS
# =====================================================


def calculate_bmi(weight, height):
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)


def calculate_bmr(gender, weight, height, age):
    if gender == "Male":
        return round(
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            + 5,
            2
        )
    else:
        return round(
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            - 161,
            2
        )


def calculate_calories(bmr, goal):
    if goal == "Weight Loss":
        return round(bmr - 300, 2)
    elif goal == "Weight Gain":
        return round(bmr + 400, 2)
    elif goal == "Muscle Building":
        return round(bmr + 300, 2)
    return bmr


# =====================================================
# CSS
# =====================================================


st.markdown(
    """
    <style>
    /* =====================================================
       APP BACKGROUND
    ====================================================== */

    .stApp{

    background:

    radial-gradient(
    circle at top left,
    #ffdff0,
    transparent 35%
    ),

    radial-gradient(
    circle at bottom right,
    #dcffe6,
    transparent 35%
    ),

    linear-gradient(
    135deg,
    #fff7fb,
    #f8fff4,
    #fffbe8
    );

    }

    /* =====================================================
       SIDEBAR
    ====================================================== */

    section[data-testid="stSidebar"] {

    background:

    linear-gradient(

    180deg,

    #ffe4f3,

    #eaffef,

    #fff7d6

    );

    border-radius:

    0px 35px 35px 0px;

    box-shadow:

    8px 0px 35px rgba(0,0,0,0.08);

    }

    section[data-testid="stSidebar"] span{

    font-size:18px;
    font-weight:800;
    color:#555;

    }

    section[data-testid="stSidebar"] [aria-current="page"] {

    background:

    linear-gradient(

    90deg,

    #ff9acb,

    #8ff5a2

    );

    border-radius:25px;

    box-shadow:

    0px 10px 25px rgba(255,120,180,0.35);

    }

    section[data-testid="stSidebar"] [aria-current="page"] span{

    color:white;

    }

    /* =====================================================
       TITLE
    ====================================================== */

    .title{

    font-size:58px;
    font-weight:900;
    text-align:center;

    background:

    linear-gradient(
    90deg,
    #ff74b8,
    #45d483
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    animation:

    fadeDown 1.2s ease;

    }

    .subtitle{

    text-align:center;
    font-size:22px;
    font-weight:500;
    color:#666;

    }

    /* =====================================================
       FORM GLASS EFFECT
    ====================================================== */

    [data-testid="stForm"]{

    background:

    rgba(255,255,255,0.75);

    padding:35px;

    border-radius:35px;

    box-shadow:

    0px 20px 50px rgba(0,0,0,0.08);

    backdrop-filter:

    blur(15px);

    }

    /* SECTION HEADINGS */

    h3{

    color:#32b873;

    font-weight:900;

    }

    /* INPUT BOXES */

    .stTextInput input,
    .stNumberInput input{

    border-radius:20px;

    background:#ffffff;

    border:2px solid #ffe1ef;

    }

    .stSelectbox div[data-baseweb="select"]{

    border-radius:20px;

    }

    /* MULTISELECT */

    .stMultiSelect div{

    border-radius:20px;

    }

    /* =====================================================
       BUTTON
    ====================================================== */

    div.stButton button,
    button[kind="primaryFormSubmit"]{

    height:55px;

    border-radius:35px;

    background:

    linear-gradient(
    90deg,
    #ff8fc7,
    #8ff5a2
    );

    color:white;

    font-size:20px;

    font-weight:900;

    border:none;

    box-shadow:

    0px 12px 30px rgba(255,120,170,0.35);

    transition:0.3s;

    }

    div.stButton button:hover,
    button[kind="primaryFormSubmit"]:hover{

    transform:

    scale(1.04);

    }

    /* =====================================================
       METRICS BMI BMR CALORIES
    ====================================================== */

    [data-testid="stMetric"]{

    background:white;

    padding:25px;

    border-radius:25px;

    box-shadow:

    0px 10px 30px rgba(0,0,0,0.08);

    text-align:center;

    }

    @keyframes fadeDown{

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
# TITLE
# =====================================================


st.markdown(
    """
    <div class="title">
    🌿 Create Your Wellness Profile
    </div>

    <div class="subtitle">
    Tell WellnessAI about yourself for personalized recommendations
    </div>

    <br>
    """,
    unsafe_allow_html=True
)


# =====================================================
# HELPERS
# =====================================================


def value(column, default=None):
    if profile:
        return profile.get(column, default)
    return default


def dropdown_index(options, column):
    if profile:
        data = profile.get(column)
        if data in options:
            return options.index(data)
    return 0


# =====================================================
# FORM
# =====================================================


with st.form("profile_form"):

    st.subheader("👤 Personal Information")
    c1, c2 = st.columns(2)

    with c1:

        name = st.text_input(
            "Name",
            value=value("name","")
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            value=int(value("age")) if value("age") else None,
            placeholder="Enter your age"
        )

        gender_options = [
            "Select Gender",
            "Male",
            "Female"
        ]

        gender = st.selectbox(
            "Gender",
            gender_options,
            index=dropdown_index(
                gender_options,
                "gender"
            )
        )

    with c2:

        height = st.number_input(
            "Height (cm)",
            min_value=1.0,
            value=float(value("height")) if value("height") else None,
            placeholder="Enter height"
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=1.0,
            value=float(value("weight")) if value("weight") else None,
            placeholder="Enter weight"
        )

        body_fat = st.number_input(
            "Body Fat %",
            min_value=1.0,
            value=float(value("body_fat")) if value("body_fat") else None,
            placeholder="Enter body fat percentage"
        )

        bp1,bp2 = st.columns(2)

        with bp1:

            systolic = st.number_input(
                "Systolic BP",
                min_value=1,
                value=int(value("systolic")) if value("systolic") else None,
                placeholder="Enter systolic BP"
            )

        with bp2:

            diastolic = st.number_input(
                "Diastolic BP",
                min_value=1,
                value=int(value("diastolic")) if value("diastolic") else None,
                placeholder="Enter diastolic BP"
            )

    st.subheader("🌎 Lifestyle Details")
    c3,c4 = st.columns(2)

    with c3:

        profession_options = [
            "Select Profession",
            "Student",
            "Employee",
            "Business Owner",
            "Homemaker",
            "Retired"
        ]

        profession = st.selectbox(
            "Profession",
            profession_options,
            index=dropdown_index(
                profession_options,
                "profession"
            )
        )

        stress_options = [
            "Select Stress Level",
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]

        stress = st.selectbox(
            "Stress Level",
            stress_options,
            index=dropdown_index(
                stress_options,
                "stress_level"
            )
        )

        available_time = st.number_input(
            "Available Time Per Day (minutes)",
            min_value=1,
            value=int(value("available_time")) if value("available_time") else None,
            placeholder="Enter available time"
        )

    with c4:

        goal_options = [
            "Select Fitness Goal",
            "Weight Loss",
            "Weight Gain",
            "Muscle Building",
            "Maintain Fitness",
            "Improve Stamina"
        ]

        goal = st.selectbox(
            "Fitness Goal",
            goal_options,
            index=dropdown_index(
                goal_options,
                "fitness_goal"
            )
        )

        food_options = [
            "Select Food Preference",
            "Vegetarian",
            "Non-Vegetarian",
            "Vegan"
        ]

        food = st.selectbox(
            "Food Preference",
            food_options,
            index=dropdown_index(
                food_options,
                "food_preference"
            )
        )

        saved_health = []
        if profile and profile.get("health_conditions"):
            saved_health = profile["health_conditions"].split(",")

        health = st.multiselect(
            "Health Conditions",
            [
                "Diabetes",
                "Thyroid",
                "High Blood Pressure",
                "Obesity",
                "Joint Pain",
                "None"
            ],
            default=saved_health
        )

    submit = st.form_submit_button(
        "Save Profile 🌿"
    )


# =====================================================
# SAVE
# =====================================================


if submit:

    if (
        not name
        or age is None
        or height is None
        or weight is None
        or body_fat is None
        or systolic is None
        or diastolic is None
        or available_time is None
        or gender.startswith("Select")
        or profession.startswith("Select")
        or stress.startswith("Select")
        or goal.startswith("Select")
        or food.startswith("Select")
    ):

        st.error(
            "Please complete all profile details 🌿"
        )

    else:

        bmi = calculate_bmi(weight,height)

        bmr = calculate_bmr(
            gender,
            weight,
            height,
            age
        )

        calories = calculate_calories(
            bmr,
            goal
        )

        data = {

            "user_email": email,

            "name": name,

            "age": age,

            "gender": gender,

            "height": height,

            "weight": weight,

            "body_fat": body_fat,

            "systolic": systolic,

            "diastolic": diastolic,

            "profession": profession,

            "stress_level": stress,

            "available_time": available_time,

            "fitness_goal": goal,

            "food_preference": food,

            "health_conditions": ",".join(health),

            "bmi": bmi,

            "bmr": bmr,

            "calories": calories

        }

        if profile:

            update_profile(
                email,
                data
            )

            st.success(
                "Profile Updated Successfully 💚"
            )

        else:

            save_profile(data)

            st.success(
                "Profile Created Successfully 🌿"
            )

        st.session_state.profile = data

        st.write("---")

        c1,c2,c3 = st.columns(3)

        c1.metric(
            "BMI",
            bmi
        )

        c2.metric(
            "BMR",
            bmr
        )

        c3.metric(
            "Calories",
            calories
        )