import pandas as pd
import numpy as np

df = pd.read_csv('AB_NYC_2019.csv')

# Task 2.1
df.loc[df['number_of_reviews'] == 0, 'reviews_per_month'] = 0

# Task 2.2
df = df[df['name'].notna() & df['host_name'].notna()]

# Task 2.3
df = df[df['price'] > 0]

# Task 2.4
df['log_price'] = np.log1p(df['price'])

# Task 2.5
room_type_map = {'Entire home/apt': 1, 'Private room': 2, 'Shared room': 3}
df['room_type_code'] = df['room_type'].map(room_type_map)
ng_map = {'Manhattan': 1, 'Brooklyn': 2, 'Queens': 3, 'Bronx': 4, 'Staten Island': 5}
df['neighbourhood_group_code'] = df['neighbourhood_group'].map(ng_map)

# Task 2.6
q99 = df['minimum_nights'].quantile(0.99)
df['minimum_nights'] = df['minimum_nights'].clip(upper=q99)

# Task 2.7
df.to_csv('AB_NYC_2019_cleaned.csv', index=False)

# Task 2.8
modelling_cols = ['log_price', 'room_type_code', 'neighbourhood_group_code',
                  'latitude', 'longitude', 'minimum_nights',
                  'number_of_reviews', 'reviews_per_month',
                  'availability_365', 'calculated_host_listings_count']

log = open('step2_cleaning.log', 'w')

print('=== Step 2 - Cleaning final log ===', file=log)
print('', file=log)
print(f'Final row count: {len(df)}', file=log)
print(f'Final columns: {list(df.columns)}', file=log)
print('', file=log)
print('NaN per modelling column (should all be 0):', file=log)
for col in modelling_cols:
    print(f'  {col}: {df[col].isna().sum()}', file=log)
print('', file=log)
print(f'room_type_map: {room_type_map}', file=log)
print(f'neighbourhood_group_map: {ng_map}', file=log)
print(f'q99 threshold for minimum_nights: {q99}', file=log)
print('', file=log)
print('Descriptive statistics on modelling columns:', file=log)
print(df[modelling_cols].describe(), file=log)

log.close()

print('Step 2 log written to step2_cleaning.log')
