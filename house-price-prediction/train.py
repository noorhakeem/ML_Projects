import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# 1. Load Data

data = pd.read_csv("data/housing.csv")
print(data.columns.tolist())

# 2. Prepocess 
X = data [["median_income", "housing_median_age"]]   # Features
y = data ["median_house_value"]  # Target 

# 3. Split data 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. train model ( Linear Regression)

model = LinearRegression()
model.fit(X_train, y_train)

#5. Save Model 

pickle.dump(model, open("model.pkl", "wb"))
print("MOdel Trained ")