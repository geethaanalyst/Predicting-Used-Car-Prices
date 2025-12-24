import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Load the dataset
df = pd.read_csv('usedCars.csv')

# Convert 'ManufactureDate' to datetime
df['ManufactureDate'] = pd.to_datetime(df['ManufactureDate'], errors='coerce')

# Data preprocessing: Convert 'Price' from 'X Lakhs' to float
def price_to_float(price_str):
    if isinstance(price_str, str):
        return float(price_str.replace(' Lakhs', '').replace(',', ''))
    return price_str

df['Price'] = df['Price'].apply(price_to_float)
df.loc[df['Price'] == 95000, 'Price'] = 0.95

# Fill missing values in categorical columns
categorical_cols = [
    'Company', 'Model', 'Variant', 'FuelType', 'Colour',
    'BodyStyle', 'TransmissionType', 'Owner', 'DealerState', 'City', 'CngKit'
]
df[categorical_cols] = df[categorical_cols].fillna('Unknown')

# Categorical features
categorical_cols = ['Company', 'FuelType', 'BodyStyle', 'TransmissionType', 'Owner', 'Model']

# Feature engineering
# Calculate car age as of 2025
current_year = datetime.now().year
df['CarAge'] = current_year - df['ModelYear']

# One-hot encoding for categorical features
df_encoded = pd.get_dummies(df[categorical_cols])
numeric_cols = ['Kilometer', 'ModelYear', 'Warranty', 'QualityScore', 'CarAge']

# Select features and target
X = pd.concat([df_encoded, df[numeric_cols]], axis=1)
y = df['Price']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

#save the model
with open('used_car_price_model.pkl', 'wb') as f:
    pickle.dump((lr, X.columns.tolist()), f)
print("Model saved successfully as used_car_price_model.pkl")