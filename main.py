# Step 1: Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load the Dataset
df = pd.read_csv('housing.csv')  # Ensure this file is in your working directory
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Explore and Clean the Data (Revised)

# Separate numeric and non-numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns
non_numeric_cols = df.select_dtypes(exclude=['number']).columns

# Fill missing values
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
df[non_numeric_cols] = df[non_numeric_cols].fillna(method='ffill')  # or use mode if needed

# Drop duplicates
df = df.drop_duplicates()

# Optional: Encode categorical columns (if needed for modeling later)
df = pd.get_dummies(df, drop_first=True)  # one-hot encoding


# Step 4: Feature Selection using Correlation
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Matrix")
plt.show()

# Define features and target (update based on your dataset columns)
# Example for Boston housing-like dataset
features = ['RM', 'LSTAT', 'PTRATIO']  # Replace with actual column names
target = 'MEDV'  # Replace with your target column

# Step 5: Split Dataset
X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Make Predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

# Step 9: Visualize Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()
