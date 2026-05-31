import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import(accuracy_score, precision_score, recall_score, f1_score,roc_auc_score, confusion_matrix, roc_curve)
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('USvideos_enhanced.csv')

# Preprocessing
df_numeric= df.select_dtypes(include=[np.number])

df_numeric = df_numeric.dropna(subset=['viral'])

y=df_numeric['viral']
X=df_numeric.drop('viral', axis=1)

# Handle missing values by filling with mean (for numeric features)
X=X.fillna(X.mean())

# Train test split
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train Logistic Regression Model
model=LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions and Evaluation
y_pred=model.predict(X_test)
y_prob=model.predict_proba(X_test)[:,1]

accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test, y_pred)
recall=recall_score(y_test, y_pred)
f1=f1_score(y_test, y_pred)
roc_auc=roc_auc_score(y_test, y_prob)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")        
print("Recall", recall)
print("F1 Score", f1)
print("ROC AUC Score", roc_auc)

# Confusion Matrix and ROC Curve
cm= confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d',cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

fpr, tpr, _ =roc_curve(y_test, y_prob)

plt.figure()
plt.plot(fpr,tpr)
plt.plot([0,1],[0,1])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()

# Featture Importance
coefficients=pd.DataFrame(
    {
        'Features':X.columns,
        'Coefficient': model.coef_[0]
    }
)

coefficients= coefficients.sort_values(by='Coefficient', key=abs, ascending=False)
print("\nFeature Coefficients:")
print(coefficients)