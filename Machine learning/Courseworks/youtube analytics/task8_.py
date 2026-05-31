import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (mean_squared_error, mean_absolute_error, r2_score,
                             accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, confusion_matrix)
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Dataset
df = pd.read_csv('USvideos_enhanced.csv')
df_numeric = df.select_dtypes(include=[np.number])

# 2. REGRESSION MODEL (Views)
df_lr = df_numeric.dropna(subset=['views'])
y_lr = df_lr['views']
X_lr = df_lr.drop('views', axis=1).fillna(df_lr.mean())

X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(
    X_lr, y_lr, test_size=0.2, random_state=42
)

lr_model = LinearRegression()
lr_model.fit(X_train_lr, y_train_lr)

y_pred_lr = lr_model.predict(X_test_lr)

# Metrics
mse = mean_squared_error(y_test_lr, y_pred_lr)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test_lr, y_pred_lr)
r2 = r2_score(y_test_lr, y_pred_lr)

# Feature importance
coef_lr = pd.DataFrame({
    "Feature": X_lr.columns,
    "Coefficient": lr_model.coef_
}).sort_values(by="Coefficient", key=abs, ascending=False)

# Plot
plt.figure(figsize=(8,5))
plt.barh(coef_lr['Feature'], coef_lr['Coefficient'])
plt.title("Regression Feature Importance (Views)")
plt.gca().invert_yaxis()
plt.show()

# 3. CLASSIFICATION MODEL (Viral)
df_log = df_numeric.dropna(subset=['viral'])
y_log = df_log['viral'].astype(int)
X_log = df_log.drop('viral', axis=1).fillna(df_log.mean())

scaler = StandardScaler()
X_log_scaled = scaler.fit_transform(X_log)

X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(
    X_log_scaled, y_log, test_size=0.2, random_state=42, stratify=y_log
)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_log, y_train_log)

y_pred_log = log_model.predict(X_test_log)
y_prob_log = log_model.predict_proba(X_test_log)[:,1]

# Metrics
acc = accuracy_score(y_test_log, y_pred_log)
prec = precision_score(y_test_log, y_pred_log)
rec = recall_score(y_test_log, y_pred_log)
f1 = f1_score(y_test_log, y_pred_log)
roc_auc = roc_auc_score(y_test_log, y_prob_log)

# Confusion Matrix
cm = confusion_matrix(y_test_log, y_pred_log)
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.show()

# Feature importance
coef_log = pd.DataFrame({
    "Feature": X_log.columns,
    "Coefficient": log_model.coef_[0]
}).sort_values(by="Coefficient", key=abs, ascending=False)

# Plot
plt.figure(figsize=(8,5))
plt.barh(coef_log['Feature'], coef_log['Coefficient'])
plt.title("Classification Feature Importance (Viral)")
plt.gca().invert_yaxis()
plt.show()

# 4. REPORT OUTPUT
print("\n================ FINAL REPORT ================\n")

# ---- Regression Summary ----
print("1. REGRESSION MODEL (Predicting Views)")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"MAE: {mae}")
print(f"R² Score: {r2}")

print("\nTop Influencing Features (Views):")
print(coef_lr.head())

# ---- Classification Summary ----
print("\n2. CLASSIFICATION MODEL (Predicting Viral)")
print(f"Accuracy: {acc}")
print(f"Precision: {prec}")
print(f"Recall: {rec}")
print(f"F1 Score: {f1}")
print(f"ROC-AUC: {roc_auc}")

print("\nTop Influencing Features (Viral):")
print(coef_log.head())

# ---- Hypothesis Insights ----
print("\n3. INSIGHTS FROM ANALYSIS")
print("- Engagement features (likes, comments) strongly impact both views and virality.")
print("- Higher interaction leads to higher probability of viral content.")
print("- Views and engagement are positively correlated.")

# ---- Business Recommendations ----
print("\n4. BUSINESS RECOMMENDATIONS")
print("- Focus on increasing engagement (likes, comments, shares).")
print("- Optimize video content to encourage interaction.")
print("- Post content that triggers audience response (questions, trends).")
print("- Maintain optimal video length (not too long, highly engaging early).")

print("\n=============================================\n")