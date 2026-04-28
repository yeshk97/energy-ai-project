# -----------------------------
# Real-Time Weather Data Collector
# Project: Energy AI Forecasting
# Purpose:
# 1. Call a free weather API
# 2. Extract temperature
# 3. Create time-based ML features
# 4. Store the data in a CSV file
# 5. Repeat continuously like an IoT data stream
# -----------------------------

# Import time module → used to add delay (sleep) for continuous data collection
import time

# Import csv module → used to write data into CSV file (like Excel)
import csv

# Import os module → used to check if file already exists
import os

# Import requests → used to call API and get data from URL
import requests

# Import datetime → used to get current date and time from system
from datetime import datetime


# Open-Meteo API URL for Dallas, Texas
# latitude and longitude represent the location
# current_weather=true means we want current real-time weather data
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=32.78&longitude=-96.8&current_weather=true"


# This is where our collected data will be stored
# CSV is like a simple Excel-style table
FILE_PATH = "data/live_data.csv"


# This loop keeps running continuously
# It simulates real-time IoT-style data collection
while True:

    # -----------------------------
    # Step 1: Call the weather API
    # -----------------------------
    response = requests.get(API_URL)

    # Convert API response from JSON format into Python dictionary
    data = response.json()


    # -----------------------------
    # Step 2: Extract useful data
    # -----------------------------
    # From the API response, go inside "current_weather"
    # and extract only the temperature value
    temperature = data["current_weather"]["temperature"]


    # -----------------------------
    # Step 3: Create time-based features
    # -----------------------------
    # Current system time
    now = datetime.now()

    # Extract hour from current time
    # Example: 6:30 PM → hour = 18
    hour = now.hour

    # Extract day of week
    # Monday = 0, Tuesday = 1, ..., Sunday = 6
    day_of_week = now.weekday()

    # Create weekend flag
    # Saturday = 5, Sunday = 6
    # If weekend → 1, else → 0
    is_weekend = 1 if day_of_week >= 5 else 0


    # -----------------------------
    # Step 4: Check if CSV exists
    # -----------------------------
    # If file does not exist, we need to add column names first
    file_exists = os.path.isfile(FILE_PATH)


    # -----------------------------
    # Step 5: Store data into CSV
    # -----------------------------
    # mode="a" means append mode
    # append means: add new row without deleting old rows
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)

        # If this is a new file, write column names first
        if not file_exists:
            writer.writerow([
                "timestamp",
                "temperature",
                "hour",
                "day_of_week",
                "is_weekend"
            ])

        # Write one row of real-time data
        writer.writerow([
            now,
            temperature,
            hour,
            day_of_week,
            is_weekend
        ])


    # -----------------------------
    # Step 6: Print confirmation
    # -----------------------------
    print("One row saved:", now, temperature)


    # -----------------------------
    # Step 7: Wait before next API call
    # -----------------------------
    # For testing, we collect data every 10 seconds
    # Later, in real projects, this can be 1 min, 5 min, or hourly
    time.sleep(60)