# -------------------------------------
# Wellness Score Calculation
# -------------------------------------


def calculate_wellness_score(

        bmi,

        stress_level,

        workout_completion,

        diet_completion,

        sleep_completion

):


    total_score = 0


    # ------------------
    # BMI SCORE (25)
    # ------------------

    if 18.5 <= bmi <= 24.9:

        total_score += 25


    elif 25 <= bmi <= 29.9:

        total_score += 18


    else:

        total_score += 10



    # ------------------
    # STRESS SCORE (20)
    # ------------------

    if stress_level == "Low":

        total_score += 20


    elif stress_level == "Moderate":

        total_score += 15


    elif stress_level == "High":

        total_score += 10


    else:

        total_score += 5




    # ------------------
    # WORKOUT SCORE (25)
    # ------------------

    workout_score = (

        workout_completion / 100

    ) * 25


    total_score += workout_score





    # ------------------
    # DIET SCORE (15)
    # ------------------

    diet_score = (

        diet_completion / 100

    ) * 15


    total_score += diet_score





    # ------------------
    # SLEEP SCORE (15)
    # ------------------

    sleep_score = (

        sleep_completion / 100

    ) * 15


    total_score += sleep_score




    return round(
        total_score,
        2
    )





def wellness_category(score):


    if score >= 85:

        return "Excellent Lifestyle 🌟"


    elif score >= 70:

        return "Good Lifestyle 💪"


    elif score >= 50:

        return "Needs Improvement 🌱"


    else:

        return "Needs More Attention ⚠️"