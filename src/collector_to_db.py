# Import requests to call the weather API
import requests

# Import sqlite3 to work with SQLite database
import sqlite3

# Import datetime to create timestamp and time features
from datetime import datetime


# Weather API URL for Dallas
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=32.78&longitude=-96.8&current_weather=true"

# Database file path
DB_PATH = "data/weather_data.db"


# Step 1: Call weather API
response = requests.get(API_URL)
data = response.json()


# Step 2: Extract temperature from API response
temperature = data["current_weather"]["temperature"]


# Step 3: Create time features
now = datetime.now()
hour = now.hour
day_of_week = now.weekday()
is_weekend = 1 if day_of_week >= 5 else 0


# Step 4: Connect to SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


# Step 5: Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    temperature REAL,
    hour INTEGER,
    day_of_week INTEGER,
    is_weekend INTEGER
)
""")


# Step 6: Insert API data into table
cursor.execute("""
INSERT INTO weather_data (timestamp, temperature, hour, day_of_week, is_weekend)
VALUES (?, ?, ?, ?, ?)
""", (str(now), temperature, hour, day_of_week, is_weekend))


# Step 7: Save changes and close database
conn.commit()
conn.close()


print("API data inserted into database")