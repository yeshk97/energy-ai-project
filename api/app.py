# Import FastAPI → used to create APIs
from fastapi import FastAPI

# Import pickle → to load saved model
import pickle

# Import pandas → to structure input data
import pandas as pd


# Step 1: Create FastAPI app
app = FastAPI()


# Step 2: Load trained model once when app starts
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


# Step 3: Create API endpoint
# This will run when user visits /predict
@app.get("/predict")
def predict(temperature: float, hour: int, day_of_week: int, is_weekend: int):

    # Convert input into DataFrame (same format as training)
    input_data = pd.DataFrame([{
        "temperature": temperature,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend
    }])

    # Make prediction
    prediction = model.predict(input_data)

    # Return result as JSON
    return {"predicted_energy_demand": prediction[0]}

# Import requests and datetime
import requests
from datetime import datetime


# New endpoint for live prediction
@app.get("/predict-live")
def predict_live():

    # Step 1: Call weather API
    url = "https://api.open-meteo.com/v1/forecast?latitude=32.78&longitude=-96.8&current_weather=true"
    response = requests.get(url)
    data = response.json()

    # Step 2: Extract temperature
    temperature = data["current_weather"]["temperature"]

    # Step 3: Create time features
    now = datetime.now()
    hour = now.hour
    day_of_week = now.weekday()
    is_weekend = 1 if day_of_week >= 5 else 0

    # Step 4: Prepare input for model
    input_data = pd.DataFrame([{
        "temperature": temperature,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend
    }])

    # Step 5: Predict
    prediction = model.predict(input_data)

    # Step 6: Return result
    return {
        "temperature": temperature,
        "predicted_energy_demand": prediction[0]
    }