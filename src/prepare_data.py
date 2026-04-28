import pandas as pd

# Step 1: Load data
df = pd.read_csv("data/live_data.csv")

# Step 2: Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Step 3: Select features (inputs for ML)
# These are the columns we will use to predict
X = df[["temperature", "hour", "day_of_week", "is_weekend"]]

# Step 4: Create target (what we want to predict)
# For now, we simulate energy demand using temperature
y = df["temperature"] * 2  # simple placeholder

# Step 5: Print shapes
print("Features shape:", X.shape)
print("Target shape:", y.shape)

# Step 6: Preview data
print(X.head())
print(y.head())