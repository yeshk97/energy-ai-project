# Import pandas → to read and handle CSV data
import pandas as pd

# Import LinearRegression model from sklearn
# This is a simple ML algorithm used for prediction
from sklearn.linear_model import LinearRegression


# Step 1: Load the collected data from CSV file
df = pd.read_csv("data/live_data.csv")


# Step 2: Select input features (X)
# These are the variables used to make predictions
X = df[["temperature", "hour", "day_of_week", "is_weekend"]]


# Step 3: Define target variable (y)
# This is what we want to predict
# For now, we are simulating energy demand using temperature
y = df["temperature"] * 2   # placeholder logic


# Step 4: Create the ML model
model = LinearRegression()


# Step 5: Train the model using X (inputs) and y (output)
# Model learns relationship between inputs and output
model.fit(X, y)


# Step 6: Take latest row of data for testing
latest_data = X.tail(1)


# Step 7: Make prediction using trained model
prediction = model.predict(latest_data)


# Step 8: Print input data used for prediction
print("Latest input data:")
print(latest_data)


# Step 9: Print predicted result
print("Predicted energy demand:")
print(prediction[0])

import pickle

# Save trained model to file
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)