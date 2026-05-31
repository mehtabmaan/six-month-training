import pandas as pd 
import numpy as np

df=pd.read_csv('USvideos.csv')

print("----Dataset Head----")
print(df.head())

print("----Dataset Info----")
print(df.info())

print("----Dataset Description----")
print(df.describe())

# 3. Identify Regression Target
regression_target = 'views'

df=df.dropna(subset=[regression_target])

# 4.Identify Classification Target (viral)
top_25_threshold=df[regression_target].quantile(0.75)
print(f"Top 25% threshold for views: {top_25_threshold:.2f}")

# 5. Create viral column
df['viral']= (df[regression_target]> top_25_threshold).astype(int)

df.to_csv('USvideos_enhanced.csv', index=False)

print("----Dataset with Viral Column----")
print(df.head())