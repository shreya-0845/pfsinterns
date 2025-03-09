import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the cleaned dataset
cleaned_dataset_path = "Life Expectancy Data Cleaned.csv"
df = pd.read_csv(cleaned_dataset_path)

# Define features and target variable
X = df.drop(columns=['Life expectancy ', 'Country', 'Year', 'Status'])
y = df['Life expectancy ']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
lr_rmse = mean_squared_error(y_test, y_pred_lr, squared=False)
lr_r2 = r2_score(y_test, y_pred_lr)

print(f"Linear Regression - RMSE: {lr_rmse:.2f}, R2: {lr_r2:.2f}")

# Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
rf_rmse = mean_squared_error(y_test, y_pred_rf, squared=False)
rf_r2 = r2_score(y_test, y_pred_rf)

print(f"Random Forest Regressor - RMSE: {rf_rmse:.2f}, R2: {rf_r2:.2f}")
