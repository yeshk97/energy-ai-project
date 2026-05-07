# Import pandas for data handling
import pandas as pd

# Import sqlite3 to connect to SQLite database
import sqlite3


# Step 1: Connect to SQLite database
conn = sqlite3.connect("data/weather_data.db")


# Step 2: Read data from database table into pandas DataFrame
# This replaces read_csv
df = pd.read_sql_query("SELECT * FROM weather_data", conn)


# Step 3: Close the database connection
conn.close()


# Step 4: Convert timestamp column (text → datetime format)
# This helps in sorting, filtering, time-based analysis
df["timestamp"] = pd.to_datetime(df["timestamp"])


# Step 5: Sort data based on time (important for time series)
df = df.sort_values("timestamp")


# Step 6: Select features (inputs for ML model)
# These columns will be used to predict output
X = df[["temperature", "hour", "day_of_week", "is_weekend"]]


# Step 7: Create target variable (output)
# For now, we simulate energy demand using temperature
# (Later we will replace this with real logic)
y = df["temperature"] * 2


# Step 8: Print shapes (to verify data size)
print("Features shape:", X.shape)
print("Target shape:", y.shape)


# Step 9: Preview features
print("\nFeatures preview:")
print(X.head())


# Step 10: Preview target
print("\nTarget preview:")
print(y.head())