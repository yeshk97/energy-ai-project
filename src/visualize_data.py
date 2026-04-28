# Import pandas → used to read and handle CSV data (like working with Excel in code)
import pandas as pd

# Import matplotlib → used to create graphs/plots
import matplotlib.pyplot as plt


# Step 1: Load the CSV file into a DataFrame (table format)
df = pd.read_csv("data/live_data.csv")


# Step 2: Convert 'timestamp' column from string to datetime format
# This is important so we can properly plot time-based data
df["timestamp"] = pd.to_datetime(df["timestamp"])


# Step 3: Print first 5 rows to understand the data structure
print(df.head())


# Step 4: Plot temperature vs time
# X-axis → timestamp (time)
# Y-axis → temperature
plt.plot(df["timestamp"], df["temperature"])


# Step 5: Add title and labels to make graph readable
plt.title("Temperature over Time")
plt.xlabel("Time")
plt.ylabel("Temperature")


# Step 6: Rotate X-axis labels so they don’t overlap
plt.xticks(rotation=45)


# Step 7: Adjust layout to avoid cutting labels
plt.tight_layout()


# Step 8: Show the graph on screen
plt.show()