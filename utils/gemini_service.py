from google import genai
import streamlit as st


# -----------------------------
# Gemini Client
# -----------------------------


client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


# -----------------------------
# GENERATE WELLNESS PLAN
# -----------------------------


def generate_wellness_plan(
        name,
        age,
        gender,
        bmi,
        calories,
        profession,
        stress_level,
        fitness_goal,
        food_preference,
        health_conditions,
        workout_intensity
):

    prompt = f"""

You are an AI Personalized Wellness and Lifestyle Coach.

Create a customized wellness plan using the following user details:

USER DETAILS:

Name: {name}

Age: {age}

Gender: {gender}

BMI: {bmi}

Daily Calories Required: {calories}

Profession: {profession}

Stress Level: {stress_level}

Fitness Goal: {fitness_goal}

Food Preference: {food_preference}

Health Conditions: {health_conditions}

ML Predicted Workout Intensity: {workout_intensity}

Generate the following sections:

1. 🥗 PERSONALIZED DIET PLAN

Provide:

- Breakfast
- Lunch
- Evening Snack
- Dinner

2. 🏋 WEEKLY WORKOUT PLAN

Create:

Monday to Sunday workout routine.

Consider the predicted workout intensity.

3. 📅 DAILY WELLNESS TIMETABLE

Example:

6 AM - Wake Up

7 AM - Workout

10 PM - Sleep

4. 🌿 HEALTH & LIFESTYLE SUGGESTIONS

5. 💚 MOTIVATIONAL MESSAGE

Make it practical, beginner friendly and personalized.

"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""

⚠️ Gemini Error:

{e}

"""