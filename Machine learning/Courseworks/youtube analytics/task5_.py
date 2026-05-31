import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("USvideos_enhanced.csv")

# Data Preprocessing
df_numeric= df.select_dtypes(include=[np.number])

df_numeric = df_numeric.dropna(subset=['views'])

y = df_numeric['views']
X = df_numeric.drop('views', axis=1)

X=X.fillna(X.mean())

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
model=LinearRegression()
model.fit(X_train, y_train)

# Predictions and Evaluation
y_pred=model.predict(X_test)

mse=mean_squared_error(y_test, y_pred)
rmse= np.sqrt(mse)
mae=mean_absolute_error(y_test, y_pred)
r2= r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R-squared: {r2:.4f}")

# Feature Importance Analysis
coefficients = pd.DataFrame(
    {
        'feature':X.columns,
        'Coefficient': model.coef_
    }
)

coefficients= coefficients.sort_values(by='Coefficient', key=abs, ascending=False)

print("\nFeature Coefficients:")
print(coefficients)

# Visualization of Feature Importance
plt.figure(figsize=(10,6))
plt.barh(coefficients['feature'], coefficients['Coefficient'])
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.title('Feature Coefficients from Linear Regression Model')
plt.gca().invert_yaxis()
plt.show()