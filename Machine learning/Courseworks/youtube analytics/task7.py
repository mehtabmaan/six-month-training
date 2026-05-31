import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

df=pd.read_csv('USvideos_enhanced.csv')

df_numeric= df.select_dtypes(include=[np.number])

# Linear Regression
df_lr=df_numeric.dropna(subset=['views'])
y_lr=df_lr['views']
X_lr=df_lr.drop('views', axis=1).fillna(df_lr.mean())

# Logistic Regression
df_log=df_numeric.dropna(subset=['viral'])
y_log= df_log['viral'].astype(int)
X_log = df_log.drop('viral', axis=1).fillna(df_log.mean())

# Scaling Techniques
scalers={
    'StandarScaler': StandardScaler(),
    'MinMaxScaler':MinMaxScaler()
}

results={}

for name, scaler in scalers.items():

    X_lr_scaled=scaler.fit_transform(X_lr)
    X_log_scaled=scaler.fit_transform(X_log)

    lr_model=LinearRegression()
    log_model=LogisticRegression(max_iter=1000)

    lr_scores=cross_val_score(lr_model, X_lr_scaled, y_lr, cv=5, scoring='r2')
    log_scores=cross_val_score(log_model, X_log_scaled, y_log, cv=5, scoring='accuracy')

    results[name]={
        'Linear Regression Mean R2': lr_scores.mean(),
        'Linear Regression Variance': lr_scores.var(),
        'Logistic Regression Mean Accuracy': log_scores.mean(),
        'Logistic Regression Variance': log_scores.var()
    }

for scaler_name, res in results.items():
    print(f"\nScaler: {scaler_name}")
    for k,v in res.items():
        print(f'{k}: {v:.4f}')

#  Train Logistic Model for Feature Importance
scaler=StandardScaler()
X_log_scaled= scaler.fit_transform(X_log)

model=LogisticRegression(max_iter=1000)
model.fit(X_log_scaled, y_log)

coefficients=pd.DataFrame(
    {
        'Feature': X_log.columns,
        'Coefficients': model.coef_[0]
    }
).sort_values(by='Coefficients', key=abs, ascending=False)

print("\nLogistic Regression Coefficients:")
print(coefficients)

#  Plot Feature Importance
plt.figure(figsize=(10,6))
plt.barh(coefficients['Feature'], coefficients['Coefficients'])
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.title('Feature Coefficients from Logistic Regression Model')
plt.gca().invert_yaxis()
plt.show()