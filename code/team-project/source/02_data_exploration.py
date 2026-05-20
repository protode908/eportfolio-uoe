import pandas as pd

# === CONFIG ===
INPUT_CSV = 'AB_NYC_2019_cleaned.csv'
LOG_FILE = 'exploration.log'

PRICE_PERCENTILES = [0.25, 0.5, 0.75, 0.9, 0.95, 0.99]
TOP_N_NEIGHBOURHOODS = 10
TOP_N_HOSTS = 10

MODELLING_COLS = [
    'log_price', 'room_type_code', 'neighbourhood_group_code',
    'latitude', 'longitude', 'minimum_nights',
    'number_of_reviews', 'reviews_per_month',
    'availability_365', 'calculated_host_listings_count'
]
# === END CONFIG ===

df = pd.read_csv(INPUT_CSV)

log = open(LOG_FILE, 'w')

# Shape
print('=== EDA exploration log ===', file=log)
print('', file=log)
print(f'Rows: {len(df)}', file=log)
print(f'Columns: {df.columns.tolist()}', file=log)
print('', file=log)

# Numeric overview
print('--- describe (numeric) ---', file=log)
print(df.describe().to_string(), file=log)
print('', file=log)

# Price
print('--- price percentiles ---', file=log)
print(df['price'].describe(percentiles=PRICE_PERCENTILES).to_string(), file=log)
print('', file=log)
print('--- log_price ---', file=log)
print(df['log_price'].describe().to_string(), file=log)
print('', file=log)

# Categoricals: room_type
print('--- room_type counts ---', file=log)
print(df['room_type'].value_counts().to_string(), file=log)
print('', file=log)
print('--- room_type shares ---', file=log)
print(df['room_type'].value_counts(normalize=True).round(3).to_string(), file=log)
print('', file=log)

# Categoricals: neighbourhood_group
print('--- neighbourhood_group counts ---', file=log)
print(df['neighbourhood_group'].value_counts().to_string(), file=log)
print('', file=log)
print('--- neighbourhood_group shares ---', file=log)
print(df['neighbourhood_group'].value_counts(normalize=True).round(3).to_string(), file=log)
print('', file=log)

# Sub-neighbourhoods
print(f'Unique sub-neighbourhoods: {df["neighbourhood"].nunique()}', file=log)
print('', file=log)
print(f'--- top {TOP_N_NEIGHBOURHOODS} sub-neighbourhoods by listings ---', file=log)
print(df['neighbourhood'].value_counts().head(TOP_N_NEIGHBOURHOODS).to_string(), file=log)
print('', file=log)

# Cross-tabs
print('--- median price by neighbourhood_group x room_type ---', file=log)
print(df.pivot_table(index='neighbourhood_group', columns='room_type',
                     values='price', aggfunc='median').round(0).to_string(), file=log)
print('', file=log)
print('--- mean log_price by neighbourhood_group x room_type ---', file=log)
print(df.pivot_table(index='neighbourhood_group', columns='room_type',
                     values='log_price', aggfunc='mean').round(3).to_string(), file=log)
print('', file=log)

# Demand signals
print('--- availability_365 ---', file=log)
print(df['availability_365'].describe().to_string(), file=log)
print(f'Share with availability_365 == 0: {(df["availability_365"]==0).mean():.3f}', file=log)
print('', file=log)
print('--- reviews_per_month ---', file=log)
print(df['reviews_per_month'].describe().to_string(), file=log)
print(f'Share with reviews_per_month == 0: {(df["reviews_per_month"]==0).mean():.3f}', file=log)
print('', file=log)

# Correlations
print('--- correlation matrix on modelling features ---', file=log)
print(df[MODELLING_COLS].corr().round(3).to_string(), file=log)
print('', file=log)

# Hosts
print('--- calculated_host_listings_count ---', file=log)
print(df['calculated_host_listings_count'].describe().to_string(), file=log)
print('', file=log)
print(f'--- top {TOP_N_HOSTS} host_id by listing count ---', file=log)
print(df.groupby('host_id').size().sort_values(ascending=False).head(TOP_N_HOSTS).to_string(), file=log)

log.close()
print('Written: exploration.log')
