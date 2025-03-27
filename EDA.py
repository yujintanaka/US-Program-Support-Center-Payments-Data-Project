import pandas as pd
df = pd.read_csv('data/all_data.csv')


print(len(df['RECIPIENT'].unique()))
# 3300 unique recipients

# Filtering rows where 'Occupation' column contains 'Engineer'
filtered_df = df[df['AWARD DESCRIPTION'].str.contains('bolivia', case=False, na=False)]

print(filtered_df['AWARD DESCRIPTION'].info())



