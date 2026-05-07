import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import requests


st.title("Energy AI Forecasting Dashboard")

st.write(
    "This dashboard shows stored weather data and predicts energy demand using FastAPI."
)


# -----------------------------
# Load data from SQLite DB
# -----------------------------
conn = sqlite3.connect("data/weather_data.db")
df = pd.read_sql_query("SELECT * FROM weather_data", conn)
conn.close()

df["timestamp"] = pd.to_datetime(df["timestamp"])


# -----------------------------
# Show data table
# -----------------------------
st.subheader("Stored Weather Data")
st.dataframe(df)


# -----------------------------
# Show temperature chart
# -----------------------------
st.subheader("Temperature Trend")

fig, ax = plt.subplots()
ax.plot(df["timestamp"], df["temperature"])
ax.set_xlabel("Time")
ax.set_ylabel("Temperature")
ax.set_title("Temperature Over Time")
plt.xticks(rotation=45)
st.pyplot(fig)


# -----------------------------
# Prediction Modes
# -----------------------------
st.subheader("Prediction")

mode = st.selectbox(
    "Select Prediction Mode",
    ["Live Prediction", "DB Latest Prediction", "Manual Prediction"]
)


# -----------------------------
# Mode 1: Live Prediction
# Calls /predict-live
# -----------------------------
if mode == "Live Prediction":
    if st.button("Get Live Prediction"):
        response = requests.get("http://127.0.0.1:8000/predict-live")
        data = response.json()

        st.success(f"Temperature: {data['temperature']}")
        st.success(f"Predicted Energy Demand: {data['predicted_energy_demand']}")


# -----------------------------
# Mode 2: DB Latest Prediction
# Calls /predict-from-db
# -----------------------------
elif mode == "DB Latest Prediction":
    if st.button("Predict From Latest DB Row"):
        response = requests.get("http://127.0.0.1:8000/predict-from-db")
        data = response.json()

        st.write("Input Used:")
        st.json(data["input"])

        st.success(f"Predicted Energy Demand: {data['predicted_energy_demand']}")


# -----------------------------
# Mode 3: Manual Prediction
# Calls /predict
# -----------------------------
else:
    temperature = st.number_input("Temperature", value=30.0)
    hour = st.number_input("Hour", min_value=0, max_value=23, value=12)
    day_of_week = st.number_input("Day of Week", min_value=0, max_value=6, value=0)
    is_weekend = st.selectbox("Is Weekend?", [0, 1])

    if st.button("Predict Manually"):
        url = (
            "http://127.0.0.1:8000/predict"
            f"?temperature={temperature}"
            f"&hour={hour}"
            f"&day_of_week={day_of_week}"
            f"&is_weekend={is_weekend}"
        )

        response = requests.get(url)
        data = response.json()

        st.success(f"Predicted Energy Demand: {data['predicted_energy_demand']}")