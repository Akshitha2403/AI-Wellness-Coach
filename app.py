import streamlit as st
from streamlit_lottie import st_lottie
import json
import base64

from utils.database import register_user, login_user


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="WellnessAI",
    page_icon="🌿",
    layout="wide"
)


# =====================================================
# LOAD LOTTIE FILES
# =====================================================

def load_lottie(path):

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


meditation = load_lottie("assets/meditation.json")
nutrition = load_lottie("assets/nutrition.json")
running = load_lottie("assets/running.json")
schedule = load_lottie("assets/schedule.json")
workout = load_lottie("assets/workout.json")



# =====================================================
# LOAD LOGO
# =====================================================

def load_image(path):

    with open(path, "rb") as img:

        return base64.b64encode(
            img.read()
        ).decode()


logo = load_image("assets/logo.png")



# =====================================================
# SESSION
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False




# =====================================================
# CSS
# =====================================================

st.markdown(
"""

<style>


#MainMenu,header,footer{
visibility:hidden;
}


/* MAIN WHITE BACKGROUND */

.stApp{

background:white;

}



/* LOGO */


.logo{

display:flex;

justify-content:center;

animation:

float 5s infinite ease-in-out;

}



.logo img{

width:330px;

animation:

breath 4s infinite ease-in-out;

}




/* TITLE */


.title{

font-size:80px;

font-weight:900;

text-align:center;


background:

linear-gradient(
90deg,
#ff70b8,
#32d67d
);


-webkit-background-clip:text;

-webkit-text-fill-color:transparent;


animation:fade 1.5s ease;

}




.quote{

font-size:32px;

font-weight:900;

text-align:center;


background:

linear-gradient(
90deg,
#ff8cc8,
#3fd985
);


-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}



.sub{

font-size:20px;

font-weight:600;

text-align:center;

color:#777;

}




/* FEATURE PILLS */


.features{

display:flex;

justify-content:center;

gap:18px;

margin-top:25px;

}



.feature-card{

padding:15px 22px;

border-radius:35px;


background:

linear-gradient(
135deg,
#ffe4f3,
#e7fff0
);


font-size:17px;

font-weight:800;


box-shadow:

0px 10px 25px rgba(0,0,0,0.08);


transition:0.3s;

}



.feature-card:hover{

transform:translateY(-8px);

}



/* BUTTON */


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

font-size:22px;

font-weight:900;

border:none;


box-shadow:

0px 12px 35px rgba(255,130,180,0.4);


transition:0.3s;

}



div.stButton button:hover{

transform:scale(1.07);

}





/* AUTH PAGE */


.auth-box{

padding:50px;

border-radius:40px;


background:

linear-gradient(
135deg,
#ffe6f4,
#eaffef,
#fff8d8
);


box-shadow:

0px 20px 50px rgba(0,0,0,0.1);

}



.auth-title{

text-align:center;

font-size:55px;

font-weight:900;


background:

linear-gradient(
90deg,
#ff70b8,
#39d77f
);


-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}



.stTextInput input{

border-radius:25px;

height:45px;

border:2px solid #ffd8ec;

}





/* ANIMATION */


@keyframes float{

50%{

transform:translateY(-20px);

}

}



@keyframes breath{

50%{

transform:scale(1.07);

}

}



@keyframes fade{

from{

opacity:0;

transform:translateY(30px);

}


to{

opacity:1;

transform:translateY(0);

}

}

/* =====================================================
   BEAUTIFUL WELLNESSAI SIDEBAR
===================================================== */


/* SIDEBAR BACKGROUND */

section[data-testid="stSidebar"] {


background:

linear-gradient(

180deg,

#ffe6f2,

#f0fff4,

#fff8d6

);


border-radius:

0px 35px 35px 0px;


box-shadow:

8px 0px 30px rgba(0,0,0,0.08);


}




/* SIDEBAR SPACING */

section[data-testid="stSidebar"] > div {


padding-top:30px;


}





/* SIDEBAR TEXT */

section[data-testid="stSidebar"] span {


font-size:18px;


font-weight:800;


color:#555;


}






/* SELECTED PAGE */

section[data-testid="stSidebar"] [aria-current="page"] {


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






/* SELECTED PAGE TEXT */

section[data-testid="stSidebar"] [aria-current="page"] span{


color:white;


font-weight:900;


}






/* HOVER EFFECT */

section[data-testid="stSidebar"] a:hover{


background:

rgba(255,255,255,0.65);


border-radius:25px;


}






/* REMOVE EXTRA TOP SPACE */

[data-testid="stSidebarHeader"]{


height:20px;


}

</style>


""",
unsafe_allow_html=True
)





# =====================================================
# HOME
# =====================================================

def home():


    left,center,right = st.columns(
        [1,2,1]
    )


    with left:

        st_lottie(
            workout,
            height=200
        )


        st_lottie(
            meditation,
            height=180
        )



    with center:


        st.markdown(
        f"""
        <div class="logo">

        <img src="data:image/png;base64,{logo}">

        </div>
        """,
        unsafe_allow_html=True
        )



        st.markdown(
        """

        <div class="title">

        WellnessAI

        </div>


        <div class="quote">

        Balance Your Body. Elevate Your Life ✨

        </div>


        <div class="sub">

        AI powered Fitness • Nutrition • Lifestyle Coach 🌿

        </div>



        <div class="features">

        <div class="feature-card">🤖 AI Coach</div>

        <div class="feature-card">🥗 Nutrition</div>

        <div class="feature-card">🏋 Fitness</div>

        <div class="feature-card">🧘 Wellness</div>

        </div>


        """,
        unsafe_allow_html=True
        )



        st.write("")


        a,b,c = st.columns([1,1,1])


        with b:

            if st.button(
                "Get Started 🚀",
                use_container_width=True
            ):

                st.session_state.page="auth"

                st.rerun()




    with right:


        st_lottie(
            running,
            height=200
        )


        st_lottie(
            nutrition,
            height=180
        )




    b1,b2,b3 = st.columns([1,1,1])


    with b2:

        st_lottie(
            schedule,
            height=150
        )





# =====================================================
# AUTH
# =====================================================

def authentication():


    st.markdown(
    """
    <div class="auth-box">

    <div class="auth-title">

    🌿 Welcome to WellnessAI

    </div>

    """,
    unsafe_allow_html=True
    )



    login,register = st.tabs(
        [
            "🔐 Login",
            "📝 Register"
        ]
    )



    with login:


        email = st.text_input("Email")


        password = st.text_input(
            "Password",
            type="password"
        )



        if st.button(
            "Login 🚀",
            use_container_width=True
        ):


            if login_user(email,password):


                st.session_state.logged_in=True

                st.session_state.email=email


                st.switch_page(
                    "pages/1_Profile.py"
                )


            else:


                st.error(
                    "Invalid Login Details"
                )




    with register:


        name = st.text_input("Full Name")


        email = st.text_input(
            "Create Email"
        )


        password = st.text_input(
            "Create Password",
            type="password"
        )



        if st.button(
            "Create Account 💚",
            use_container_width=True
        ):


            if register_user(
                name,
                email,
                password
            ):


                st.success(
                    "Account Created Successfully 🌿"
                )


            else:


                st.warning(
                    "Account already exists"
                )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )




# =====================================================
# ROUTER
# =====================================================


if st.session_state.page=="home":

    home()


else:

    authentication()