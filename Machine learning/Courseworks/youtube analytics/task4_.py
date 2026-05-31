import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

df=pd.read_csv('USvideos_enhanced.csv')

df['title_length'] = df['title'].apply(lambda x: len(str(x)))
df['publish_time'] = pd.to_datetime(df['publish_time']).dt.tz_localize(None)
df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m', errors='coerce')
df['days_since_publish'] = (df['trending_date'] - df['publish_time']).dt.days

df = df.dropna(subset=['views', 'viral', 'likes', 'dislikes', 'comment_count'])

# 1. Define feature groups
numeric_features=['likes', 'dislikes','comment_count', 'title_length', 'days_since_publish']
categorical_features=['channel_title', 'category_id']

y_reg=df['views']
y_clf=df['viral']

# 3. Create the preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        # sparse_output=False ensures we get a dense matrix back for easier handling
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
    ]
)

# 4. Fit and Transform the features (X)
X = df[numeric_features + categorical_features]
X_processed = preprocessor.fit_transform(X)

# 5. Split the data into training and testing sets

# Regression Split (Predicting 'views')
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_processed, y_reg, test_size=0.2, random_state=42
)

# Classification Split (Predicting 'viral')
# Added stratify=y_clf to maintain the 75/25 ratio in both sets
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_processed, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)

# Final Outputs
print(f"Processed Feature Matrix Shape: {X_processed.shape}")
print(f"Training Set Size: {X_train_reg.shape[0]} samples")
print(f"Testing Set Size: {X_test_reg.shape[0]} samples")