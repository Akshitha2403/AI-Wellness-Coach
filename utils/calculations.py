# -----------------------------------
# Health Calculation Functions
# -----------------------------------


def calculate_bmi(height_cm, weight_kg):

    height_m = height_cm / 100

    bmi = weight_kg / (height_m ** 2)

    return round(bmi, 2)




def get_bmi_category(bmi):

    if bmi < 18.5:

        return "Underweight"


    elif bmi >= 18.5 and bmi < 25:

        return "Healthy"


    elif bmi >= 25 and bmi < 30:

        return "Overweight"


    else:

        return "Obese"





def calculate_bmr(
        gender,
        age,
        height_cm,
        weight_kg
):


    # Mifflin-St Jeor Equation


    if gender == "M":

        bmr = (

            (10 * weight_kg)

            +

            (6.25 * height_cm)

            -

            (5 * age)

            +

            5

        )


    else:

        bmr = (

            (10 * weight_kg)

            +

            (6.25 * height_cm)

            -

            (5 * age)

            -

            161

        )



    return round(
        bmr,
        2
    )





def calculate_daily_calories(
        bmr,
        fitness_goal
):


    if fitness_goal == "Weight Loss":

        calories = bmr - 300


    elif fitness_goal == "Weight Gain":

        calories = bmr + 500


    elif fitness_goal == "Muscle Building":

        calories = bmr + 300


    else:

        calories = bmr



    return round(
        calories,
        2
    )