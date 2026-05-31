from scipy import stats
import pandas as pd

df=pd.read_csv('USvideos_enhanced.csv')  

features_to_test=['likes','dislikes','comment_count']

print("--- Hypothesis Testing (Two-Sample t-test) ---")
print("H0 (Null Hypothesis): High vs. Low engagement groups have the same mean views.")
print("H1 (Alternative): High engagement groups have significantly different mean views.\n")

results=[]

for feature in features_to_test:
    median_val=df[feature].median()
    group_high=df[df[feature]>median_val]['views']
    group_low=df[df[feature]<=median_val]['views']

    t_stat, p_val =stats.ttest_ind(group_high, group_low, equal_var=False)

    is_significant = p_val<0.5

    results.append({
        'Feature': feature,
        't-statistic': t_stat,
        'p_va;ue': p_val,
        'Significant': is_significant
    })

results_df = pd.DataFrame(results)
print(results_df)
