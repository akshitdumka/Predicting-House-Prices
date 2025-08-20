# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview
This project focuses on predicting **house prices** based on numerical features using a **Linear Regression model**.  
The goal is to build a regression model that can estimate housing prices from features such as square footage, number of bedrooms, location, and other factors.  

Machine Learning techniques are used to:
- Explore and clean the dataset
- Select important features
- Train a regression model
- Evaluate performance using metrics
- Visualize predicted vs actual prices

---

## 📂 Dataset
- **File:** `housing.csv`  
- **Features (example):**
  - `LotArea` – Size of the lot
  - `OverallQual` – Overall material and finish quality
  - `YearBuilt` – Year the house was built
  - `TotalBsmtSF` – Basement area in square feet
  - `GrLivArea` – Above ground living area in square feet
  - `GarageCars` – Number of cars that fit in the garage
  - `SalePrice` – Target variable (house price)

*(Exact columns depend on the dataset provided.)*

---

## 🔎 Steps in Analysis

### 1. Data Collection
- Load dataset (`pd.read_csv()`).
- Check structure, size, and data types.

### 2. Data Cleaning & Exploration
- Handle missing values (mean/median for numerical, mode for categorical).
- Remove duplicates.
- Explore feature distributions using histograms and boxplots.
- Check correlation between features and the target variable.

### 3. Feature Selection
- Use correlation heatmap to identify relevant features.
- Drop irrelevant or highly collinear variables.

### 4. Model Training
- Split dataset into **train and test sets**.
- Train a **Linear Regression model** using Scikit-learn.

### 5. Model Evaluation
- Evaluate performance on test set using:
  - **Mean Squared Error (MSE)**
  - **Root Mean Squared Error (RMSE)**
  - **R-squared (R²)**

### 6. Visualization
- Plot **Predicted vs Actual prices**.
- Plot **Residuals** to check model performance.

---

## 📊 Visualizations
- Distribution of house prices.
- Correlation heatmap of features.
- Scatter plots (e.g., `GrLivArea` vs `SalePrice`).
- Predicted vs Actual Price plot.

---

## 🛠️ Technologies Used
- **Python 3**
- **Pandas** – Data manipulation
- **NumPy** – Numerical computations
- **Matplotlib** – Visualizations
- **Seaborn** – Statistical plots
- **Scikit-learn** – Linear Regression model

---

## 🚀 How to Run
1. Clone this repository or download the files.
2. Install required dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn

