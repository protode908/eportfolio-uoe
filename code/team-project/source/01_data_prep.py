import pandas as pd
import numpy as np

# === CONFIG ===
INPUT_CSV = 'AB_NYC_2019.csv'
OUTPUT_CSV = 'AB_NYC_2019_cleaned.csv'
LOG_FILE = 'data_prep_cleaning.log'

ROOM_TYPE_MAP = {'Entire home/apt': 1, 'Private room': 2, 'Shared room': 3}
NEIGHBOURHOOD_GROUP_MAP = {'Manhattan': 1, 'Brooklyn': 2, 'Queens': 3, 'Bronx': 4, 'Staten Island': 5}

MIN_NIGHTS_QUANTILE = 0.99

MODELLING_COLS = [
    'log_price', 'room_type_code', 'neighbourhood_group_code',
    'latitude', 'longitude', 'minimum_nights',
    'number_of_reviews', 'reviews_per_month',
    'availability_365', 'calculated_host_listings_count'
]
# === END CONFIG ===

df = pd.read_csv(INPUT_CSV)

# Cleaning step 1
# Fill reviews_per_month with 0 where there are no reviews.
# Leave last_review as NaN because it is a date field and is not used by the modelling scripts.
df.loc[df['number_of_reviews'] == 0, 'reviews_per_month'] = 0

# Cleaning step 2
df = df[df['name'].notna() & df['host_name'].notna()]

# Cleaning step 3
df = df[df['price'] > 0]

# Cleaning step 4
df['log_price'] = np.log1p(df['price'])

# Cleaning step 5
df['room_type_code'] = df['room_type'].map(ROOM_TYPE_MAP)
df['neighbourhood_group_code'] = df['neighbourhood_group'].map(NEIGHBOURHOOD_GROUP_MAP)

# Cleaning step 6
q99 = df['minimum_nights'].quantile(MIN_NIGHTS_QUANTILE)
df['minimum_nights'] = df['minimum_nights'].clip(upper=q99)

# Save cleaned dataset
df.to_csv(OUTPUT_CSV, index=False)

# Write cleaning log
log = open(LOG_FILE, 'w')
print('=== Data preparation cleaning log ===', file=log)
print('', file=log)
print(f'Final row count: {len(df)}', file=log)
print(f'Final columns: {list(df.columns)}', file=log)
print('', file=log)
print('NaN per modelling column (should all be 0):', file=log)
for col in MODELLING_COLS:
    print(f'  {col}: {df[col].isna().sum()}', file=log)
print('', file=log)
print(f'room_type_map: {ROOM_TYPE_MAP}', file=log)
print(f'neighbourhood_group_map: {NEIGHBOURHOOD_GROUP_MAP}', file=log)
print(f'q99 threshold for minimum_nights: {q99}', file=log)
print('', file=log)
print('Descriptive statistics on modelling columns:', file=log)
print(df[MODELLING_COLS].describe(), file=log)
log.close()

print('Data preparation log written to data_prep_cleaning.log')
