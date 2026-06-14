import pickle
import pandas as pd
import os


# Get project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# Model paths

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "wellness_model.pkl"
)


ENCODER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "encoders.pkl"
)


FEATURE_PATH = os.path.join(
    BASE_DIR,
    "models",
    "feature_names.pkl"
)



# Load ML files

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


with open(ENCODER_PATH, "rb") as file:
    encoders = pickle.load(file)
print(encoders["gender"].classes_)


with open(FEATURE_PATH, "rb") as file:
    feature_names = pickle.load(file)




def predict_workout_intensity(user_data):


    # Convert dictionary to dataframe

    input_df = pd.DataFrame(
        [user_data]
    )


    # Encode categorical columns

    for column in encoders:

        if column != "Workout_Intensity":

            if column in input_df.columns:

                input_df[column] = encoders[column].transform(
                    input_df[column]
                )


    # Arrange columns in training order

    input_df = input_df[
        feature_names
    ]


    # Prediction

    prediction = model.predict(
        input_df
    )[0]



    # Convert number back to text

    intensity = encoders[
        "Workout_Intensity"
    ].inverse_transform(
        [prediction]
    )[0]



    return intensity

