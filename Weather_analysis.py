# ==========================
# Step 1 : Import the necessary libraries
# ==========================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# For better visualization aesthetics
plt.style.use("seaborn-v0_8")

# ==========================
# Step 2 : Load the dataset
# ==========================

file_path = r"\Users\SANSKAR\OneDrive\Desktop\CP\Python Projects\Weather_data.csv"  
df = pd.read_csv(file_path)

# ==========================
# Step 3 : Display the original dataset
# ==========================

# Convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

print("Original Dataset:")
print(df.head())
print(df.info())
print(df.describe())

# ==========================
# Step 4 : Handle missing values
# ==========================

df.fillna({
      "Precipitation": 0,  
      "WindSpeed": df["WindSpeed"].mean(),  
      "Humidity": df["Humidity"].mean()  
      
}, inplace=True) 

# ==========================
# Step 5 : Add missing data (if necessary)
# ==========================

df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

# ==========================
# Step 6 : Data Analysis
# ==========================

# 1. Average temperature and humidity
avg_temp = df['Temperature'].mean()
avg_humidity = df['Humidity'].mean()
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Average Humidity: {avg_humidity:.2f} %")

# 2. Frequency of different weather conditions
condition_counts = df['Condition'].value_counts()
print("\nWeather Condition Counts:")
print(condition_counts)

#=========================
# Step 7 : Data Visualization
#==========================

# 1. Temperature Trends

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Temperature"], marker='o')
plt.title("Temperature Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2.Humidity Trends

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Humidity"], marker='o')
plt.title("Humidity Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3.Condition Frequency

plt.figure(figsize=(7, 5))
sns.countplot(x="Condition", data=df) # type: ignore
plt.title("Weather Condition Frequency")
plt.xlabel("Condition")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4.Temperature vs Humidity

plt.figure(figsize=(10, 5))
plt.scatter(df["Temperature"], df["Humidity"])
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()

# 5.Coreelation Heatmap

plt.figure(figsize=(7, 5))
sns.heatmap(df[["Temperature", "Humidity","Precipitation","WindSpeed"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()





