import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# 1. Load Data

data = pd.read_csv("data/housing.csv")
print(data.columns.tolist())

# 2. Prepocess 

data ["rooms_per_household"] = data ["total_rooms"]/ data["households"]
data["bedrooms_per_room"] = data["total_bedrooms"] / data["total_rooms"]
X = data [["median_income", "housing_median_age", "rooms_per_household"]]   # Features updated
y = data ["median_house_value"]  # Target 

# 3. Split data 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. train model ( Linear Regression)

model = LinearRegression()
model.fit(X_train, y_train)

# Health check 

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Training R²: {train_score:.2f}, Test R²: {test_score:.2f}")

#5. Save Model 

pickle.dump(model, open("models/model.pkl", "wb"))
print("Model Trained and saved in (../models/) ")