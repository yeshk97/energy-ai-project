# Import pandas for data handling
import pandas as pd

# Import sqlite3 to read data from SQLite database
import sqlite3

# Import LinearRegression model
from sklearn.linear_model import LinearRegression

# Import pickle to save trained model
import pickle


# Step 1: Connect to SQLite database
conn = sqlite3.connect("data/weather_data.db")


# Step 2: Read data from DB table
df = pd.read_sql_query("SELECT * FROM weather_data", conn)


# Step 3: Close DB connection
conn.close()


# Step 4: Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])


# Step 5: Sort data by timestamp
df = df.sort_values("timestamp")


# Step 6: Select input features
X = df[["temperature", "hour", "day_of_week", "is_weekend"]]


# Step 7: Create temporary target
# Later we replace this with real energy demand
y = df["temperature"] * 2


# Step 8: Create model
model = LinearRegression()


# Step 9: Train model
model.fit(X, y)


# Step 10: Save trained model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)


print("Model trained using DB data and saved successfully.")