import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('USvideos_enhanced.csv')

# Feature Engineering
df['title_length'] = df['title'].apply(lambda x: len(str(x)))
df['publish_time']=pd.to_datetime(df['publish_time'])
df['trending_date']=pd.to_datetime(df['trending_date'], format='%y.%d.%m',errors='coerce')
df['publish_time'] = df['publish_time'].dt.tz_localize(None)
df['days_since_publish']=(df['trending_date']-df['publish_time']).dt.days

df.to_csv('USvideos_enhanced.csv', index=False)

# List of numeric features to analyze
numeric_features=['views', 'likes', 'dislikes', 'comment_count', 'title_length', 'days_since_publish']

# 1. Plot Histogram of Views
plt.figure(figsize=(10,6))
sns.histplot(df['views'], bins=50, kde=True, color='blue')
plt.title('Distribution of Youtube Views')
plt.xlabel('Views')
plt.ylabel('Frequency')
plt.show()

# 2. Plot Scatterplot of Likes vs Views
plt.figure(figsize=(10,6))
sns.scatterplot(x='views', y='likes', data=df, alpha=0.5)
plt.title('Likes vs Views')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()

# 3 Compute Correlation Matrix
corr_matrix=df[numeric_features].corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numeric Features')
plt.show()

'''When reviewing the outputs, students should focus on these three points:

The "Viral" Threshold: By using the top 25% quantile, we define "viral" based on the dataset's internal performance. This is more robust than picking an arbitrary number like 1 million views.

The Likes/Views Connection: In the scatterplot and correlation matrix, Likes will show a very high positive correlation (usually > 0.80) with Views. This suggests that engagement grows proportionally with reach.

Data Distribution: The histogram will likely show a heavy right-skew. Most videos have relatively few views, while a tiny "long tail" of videos accounts for the millions of views.

Metadata Influence: You will likely notice that title_length has a correlation near 0. This suggests that while a title is important for a human to click, its specific character count doesn't mathematically dictate the number of views.'''