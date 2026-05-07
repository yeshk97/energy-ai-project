# Import sqlite3 to connect to database
import sqlite3

# Import pandas to display data nicely
import pandas as pd


# Step 1: Connect to SQLite database
conn = sqlite3.connect("data/weather_data.db")


# Step 2: Run SQL query to get all data
df = pd.read_sql_query("SELECT * FROM weather_data", conn)

print("\nAll data (first 5 rows):")
print(df.head())


# Step 3: Get latest 5 records (important for time series)
latest = pd.read_sql_query(
    "SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 5",
    conn
)

print("\nLatest 5 rows:")
print(latest)


# Step 4: Example filter (hour = 18)
filtered = pd.read_sql_query(
    "SELECT * FROM weather_data WHERE hour = 18",
    conn
)

print("\nFiltered data (hour = 18):")
print(filtered.head())


# Step 5: Close DB connection
conn.close()