from fastapi import FastAPI
import pickle
import pandas as pd
import requests
import sqlite3
from datetime import datetime

# Create FastAPI app
app = FastAPI()

# Load trained model once when API starts
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


# Endpoint 1: Manual prediction
@app.get("/predict")
def predict(temperature: float, hour: int, day_of_week: int, is_weekend: int):

    input_data = pd.DataFrame([{
        "temperature": temperature,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend
    }])

    prediction = model.predict(input_data)

    return {"predicted_energy_demand": prediction[0]}


# Endpoint 2: Live prediction from weather API
@app.get("/predict-live")
def predict_live():

    url = "https://api.open-meteo.com/v1/forecast?latitude=32.78&longitude=-96.8&current_weather=true"

    response = requests.get(url)
    data = response.json()

    temperature = data["current_weather"]["temperature"]

    now = datetime.now()
    hour = now.hour
    day_of_week = now.weekday()
    is_weekend = 1 if day_of_week >= 5 else 0

    input_data = pd.DataFrame([{
        "temperature": temperature,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend
    }])

    prediction = model.predict(input_data)

    return {
        "temperature": temperature,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend,
        "predicted_energy_demand": prediction[0]
    }


# Endpoint 3: Prediction from latest DB row
@app.get("/predict-from-db")
def predict_from_db():

    conn = sqlite3.connect("data/weather_data.db")

    query = """
    SELECT temperature, hour, day_of_week, is_weekend
    FROM weather_data
    ORDER BY timestamp DESC
    LIMIT 1
    """

    input_data = pd.read_sql_query(query, conn)

    conn.close()

    prediction = model.predict(input_data)

    return {
        "input": input_data.to_dict(orient="records")[0],
        "predicted_energy_demand": prediction[0]
    }