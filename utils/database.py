from supabase import create_client

import streamlit as st

# -----------------------------
# Supabase Connection
# -----------------------------

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

# -----------------------------
# SAVE USER PROFILE
# -----------------------------

def save_profile(data):

    response = supabase.table(
        "profiles"
    ).insert(
        data
    ).execute()

    return response

# -----------------------------
# SAVE WELLNESS RECORD
# -----------------------------

def save_wellness_record(data):

    response = supabase.table(
        "wellness_records"
    ).insert(
        data
    ).execute()

    return response

# -----------------------------
# SAVE DAILY PROGRESS
# -----------------------------

def save_progress(data):

    response = supabase.table(
        "progress"
    ).insert(
        data
    ).execute()

    return response

# -----------------------------
# GET USER WELLNESS HISTORY
# -----------------------------

def get_user_records(email):

    response = supabase.table(
        "wellness_records"
    ).select(
        "*"
    ).eq(
        "user_email",
        email
    ).execute()

    return response.data

# -----------------------------
# REGISTER USER
# -----------------------------

def register_user(name, email, password):

    existing_user = supabase.table(
        "users"
    ).select(
        "*"
    ).eq(
        "email",
        email
    ).execute()

    if existing_user.data:
        return False

    data = {
        "name": name,
        "email": email,
        "password": password
    }

    response = supabase.table(
        "users"
    ).insert(
        data
    ).execute()

    return True

# -----------------------------
# LOGIN USER
# -----------------------------

def login_user(email, password):

    response = supabase.table(
        "users"
    ).select(
        "*"
    ).eq(
        "email",
        email
    ).eq(
        "password",
        password
    ).execute()

    if response.data:
        return True

    return False

# -----------------------------
# GET USER PROFILE
# -----------------------------

def get_profile(email):

    response = supabase.table(
        "profiles"
    ).select(
        "*"
    ).eq(
        "user_email",
        email
    ).execute()

    if response.data:
        return response.data[0]

    return None

# -----------------------------
# UPDATE USER PROFILE
# -----------------------------

def update_profile(email, data):

    response = supabase.table(
        "profiles"
    ).update(
        data
    ).eq(
        "user_email",
        email
    ).execute()

    return response

# -----------------------------
# GET LATEST WELLNESS RECORD
# -----------------------------

def get_latest_wellness_record(email):

    response = supabase.table(
        "wellness_records"
    ).select(
        "*"
    ).eq(
        "user_email",
        email
    ).order(
        "created_at",
        desc=True
    ).limit(
        1
    ).execute()

    if response.data:

        return response.data[0]

    return None

# -----------------------------
# UPDATE WELLNESS RECORD
# -----------------------------


def update_wellness_record(email, data):


    response = supabase.table(

        "wellness_records"

    ).update(

        data

    ).eq(

        "user_email",

        email

    ).execute()


    return response

# -----------------------------
# GET USER PROGRESS
# -----------------------------


def get_progress(email):


    response = supabase.table(

        "progress"

    ).select(

        "*"

    ).eq(

        "user_email",

        email

    ).order(

        "date",

        desc=True

    ).execute()



    return response.data

# -----------------------------
# GET TODAY PROGRESS
# -----------------------------


def get_today_progress(email, today_date):


    response = supabase.table(

        "progress"

    ).select(

        "*"

    ).eq(

        "user_email",

        email

    ).eq(

        "date",

        today_date

    ).execute()



    if response.data:


        return response.data[0]


    return None





# -----------------------------
# UPDATE TODAY PROGRESS
# -----------------------------


def update_today_progress(email, today_date, data):


    response = supabase.table(

        "progress"

    ).update(

        data

    ).eq(

        "user_email",

        email

    ).eq(

        "date",

        today_date

    ).execute()



    return response