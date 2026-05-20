from datetime import datetime
import pandas as pd
import numpy as np

# === CONFIGS ===
RUN_ID = datetime.now().strftime('%Y%m%d_%H%M%S')

INPUT_CSV = 'AB_NYC_2019.csv'
OUTPUT_CSV = 'AB_NYC_2019_cleaned_V1.csv'
LOG_FILE = f'data_prep_log_{RUN_ID}.txt'

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

# no reviews means no monthly review rate
df.loc[df['number_of_reviews'] == 0, 'reviews_per_month'] = 0

# remove missing names and invalid prices
df = df[df['name'].notna() & df['host_name'].notna()]
df = df[df['price'] > 0]

# log target for regression checks
df['log_price'] = np.log1p(df['price'])

# simple first-pass encoding
df['room_type_code'] = df['room_type'].map(ROOM_TYPE_MAP)
df['neighbourhood_group_code'] = df['neighbourhood_group'].map(NEIGHBOURHOOD_GROUP_MAP)

# cap very long stays
q99 = df['minimum_nights'].quantile(MIN_NIGHTS_QUANTILE)
df['minimum_nights'] = df['minimum_nights'].clip(upper=q99)

df.to_csv(OUTPUT_CSV, index=False)

log = open(LOG_FILE, 'w')
print('=== Data prep log ===', file=log)
print('', file=log)
print(f'Run ID: {RUN_ID}', file=log)
print(f'Input file: {INPUT_CSV}', file=log)
print(f'Output file: {OUTPUT_CSV}', file=log)
print(f'Final row count: {len(df)}', file=log)
print(f'Final columns: {list(df.columns)}', file=log)
print('', file=log)
print('NaN per modelling column:', file=log)
for col in MODELLING_COLS:
    print(f'  {col}: {df[col].isna().sum()}', file=log)
print('', file=log)
print(f'room_type_map: {ROOM_TYPE_MAP}', file=log)
print(f'neighbourhood_group_map: {NEIGHBOURHOOD_GROUP_MAP}', file=log)
print(f'q99 threshold for minimum_nights: {q99}', file=log)
print('', file=log)
print('Describe on modelling columns:', file=log)
print(df[MODELLING_COLS].describe(), file=log)
log.close()

print(f'Cleaned data written to {OUTPUT_CSV}')
print(f'Log written to {LOG_FILE}')
