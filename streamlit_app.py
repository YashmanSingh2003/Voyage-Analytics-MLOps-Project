
import streamlit as st
import pandas as pd
import joblib

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Voyage Analytics",
    page_icon="✈️",
    layout="wide"
)

# ==========================
# LOAD MODELS
# ==========================
flight_model = joblib.load("flight_price_model.pkl")
gender_model = joblib.load("gender_model.pkl")

hotel_data = joblib.load("hotel_recommender.pkl")
user_similarity_df = hotel_data["user_similarity_df"]
user_hotel_matrix = hotel_data["user_hotel_matrix"]

# ==========================
# POPULAR HOTELS
# ==========================
popular_hotels = [
    "Hotel AU",
    "Hotel K",
    "Hotel BD",
    "Hotel BP",
    "Hotel A",
    "Hotel Z",
    "Hotel AF",
    "Hotel BW",
    "Hotel CB"
]

# ==========================
# HOTEL RECOMMENDATION FUNCTION
# ==========================
def recommend_hotels(user_id, n_recommendations=3):

    if user_id not in user_similarity_df.columns:
        return ["User ID not found"]

    similar_users = (
        user_similarity_df[user_id]
        .sort_values(ascending=False)
        .iloc[1:6]
        .index
    )

    user_hotels = set(
        user_hotel_matrix.loc[user_id][
            user_hotel_matrix.loc[user_id] > 0
        ].index
    )

    recommendations = set()

    for sim_user in similar_users:

        sim_user_hotels = set(
            user_hotel_matrix.loc[sim_user][
                user_hotel_matrix.loc[sim_user] > 0
            ].index
        )

        recommendations.update(
            sim_user_hotels - user_hotels
        )

    recommendations = list(recommendations)

    if len(recommendations) < n_recommendations:

        for hotel in popular_hotels:

            if hotel not in user_hotels and hotel not in recommendations:
                recommendations.append(hotel)

            if len(recommendations) >= n_recommendations:
                break

    if len(recommendations) == 0:
        return ["User has already booked all available hotels"]

    return recommendations[:n_recommendations]


# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("✈️ Voyage Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Flight Price Prediction",
        "Gender Classification",
        "Hotel Recommendation"
    ]
)

# ==========================
# HOME
# ==========================
if page == "Home":

    st.title("✈️ Voyage Analytics")

    st.markdown("---")

    st.header("Machine Learning Travel Analytics Project")

    st.write(
    '''
    This project contains:

    ✈️ Flight Price Prediction Model

    👤 Gender Classification Model

    🏨 Hotel Recommendation System

    Built using:

    • Scikit-Learn
    • Streamlit
    • Flask
    • MLflow
    • Docker
    • Kubernetes
    • Airflow
    • Jenkins
    '''
    )

# ==========================
# FLIGHT PRICE PREDICTION
# ==========================
elif page == "Flight Price Prediction":

    st.title("✈️ Flight Price Prediction")

    cities = [
        "Recife (PE)",
        "Florianopolis (SC)",
        "Brasilia (DF)",
        "Aracaju (SE)",
        "Salvador (BH)",
        "Campo Grande (MS)",
        "Natal (RN)",
        "Sao Paulo (SP)",
        "Rio de Janeiro (RJ)"
    ]

    flight_types = [
        "firstClass",
        "economic",
        "premium"
    ]

    agencies = [
        "FlyingDrops",
        "CloudFy",
        "Rainbow"
    ]

    from_city = st.selectbox("From", cities)
    to_city = st.selectbox("To", cities)
    flight_type = st.selectbox("Flight Type", flight_types)
    agency = st.selectbox("Agency", agencies)

    time = st.number_input("Time", value=1.5)
    distance = st.number_input("Distance", value=500.0)

    year = st.number_input("Year", value=2019)
    month = st.slider("Month",1,12)
    day = st.slider("Day",1,31)
    day_of_week = st.slider("Day Of Week",0,6)
    quarter = st.slider("Quarter",1,4)

    if st.button("Predict Price"):

        input_df = pd.DataFrame({
            "from":[from_city],
            "to":[to_city],
            "flightType":[flight_type],
            "time":[time],
            "distance":[distance],
            "agency":[agency],
            "year":[year],
            "month":[month],
            "day":[day],
            "day_of_week":[day_of_week],
            "quarter":[quarter]
        })

        prediction = flight_model.predict(input_df)

        st.success(
            f"Predicted Price : ₹ {prediction[0]:,.2f}"
        )

# ==========================
# GENDER CLASSIFICATION
# ==========================
elif page == "Gender Classification":

    st.title("👤 Gender Classification")

    company = st.selectbox(
        "Company",
        [
            "4You",
            "Monsters CYA",
            "Wonka Company",
            "Acme Factory",
            "Umbrella LTDA"
        ]
    )

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    age = st.slider("Age",18,70,30)

    if st.button("Predict Gender"):

        input_df = pd.DataFrame({
            "company":[company],
            "age":[age],
            "first_name":[first_name],
            "last_name":[last_name]
        })

        prediction = gender_model.predict(input_df)[0]

        gender_map = {
            0:"Female",
            1:"Male",
            2:"None"
        }

        st.success(
            f"Predicted Gender : {gender_map[prediction]}"
        )

# ==========================
# HOTEL RECOMMENDATION
# ==========================
elif page == "Hotel Recommendation":

    st.title("🏨 Hotel Recommendation")

    user_id = st.number_input(
        "User ID",
        min_value=0,
        max_value=1309,
        value=10
    )

    if st.button("Recommend Hotels"):

        recommendations = recommend_hotels(user_id)

        st.subheader("Recommended Hotels")

        for hotel in recommendations:
            st.success(hotel)
