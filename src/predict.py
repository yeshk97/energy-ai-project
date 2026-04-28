# Import pickle → used to load saved ML model from file
import pickle

# Import pandas → used to read CSV data
import pandas as pd


# Step 1: Load the trained model from file
# "rb" means read in binary mode
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


# Step 2: Load the latest collected data
df = pd.read_csv("data/live_data.csv")


# Step 3: Select features (same features used during training)
X = df[["temperature", "hour", "day_of_week", "is_weekend"]]


# Step 4: Take the most recent row of data
# This simulates real-time prediction
latest_data = X.tail(1)


# Step 5: Use model to predict output
prediction = model.predict(latest_data)


# Step 6: Print the prediction result
print("Predicted energy demand:", prediction[0])