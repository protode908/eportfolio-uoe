from datetime import datetime
import sys
import pandas as pd

# === CONFIGURATION ===
RUN_ID = datetime.now().strftime('%Y%m%d_%H%M%S')

INPUT_CSV = 'AB_NYC_2019_cleaned_V1.csv'
LOG_FILE = f'exploration_log_{RUN_ID}.txt'

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
original_stdout = sys.stdout
sys.stdout = log

print('=== EDA exploration log ===')
print()
print(f'Run ID: {RUN_ID}')
print(f'Input file: {INPUT_CSV}')
print(f'Rows: {len(df)}')
print(f'Columns: {df.columns.tolist()}')
print()

# Basic numeric summaries
print('--- describe ---')
print(df.describe().to_string())
print()

# Price checks
print('--- price percentiles ---')
print(df['price'].describe(percentiles=PRICE_PERCENTILES).to_string())
print()
print('--- log_price ---')
print(df['log_price'].describe().to_string())
print()

# Room type
print('--- room_type counts ---')
print(df['room_type'].value_counts().to_string())
print()
print('--- room_type shares ---')
print(df['room_type'].value_counts(normalize=True).round(3).to_string())
print()

# Neighbourhood group
print('--- neighbourhood_group counts ---')
print(df['neighbourhood_group'].value_counts().to_string())
print()
print('--- neighbourhood_group shares ---')
print(df['neighbourhood_group'].value_counts(normalize=True).round(3).to_string())
print()

# Sub-neighbourhoods
print(f'Unique sub-neighbourhoods: {df["neighbourhood"].nunique()}')
print()
print(f'--- top {TOP_N_NEIGHBOURHOODS} sub-neighbourhoods by listings ---')
print(df['neighbourhood'].value_counts().head(TOP_N_NEIGHBOURHOODS).to_string())
print()

# Cross-tabs
print('--- median price by neighbourhood_group x room_type ---')
print(df.pivot_table(index='neighbourhood_group', columns='room_type',
                     values='price', aggfunc='median').round(0).to_string())
print()
print('--- mean log_price by neighbourhood_group x room_type ---')
print(df.pivot_table(index='neighbourhood_group', columns='room_type',
                     values='log_price', aggfunc='mean').round(3).to_string())
print()

# Demand signals
print('--- availability_365 ---')
print(df['availability_365'].describe().to_string())
print(f'Share with availability_365 == 0: {(df["availability_365"] == 0).mean():.3f}')
print()
print('--- reviews_per_month ---')
print(df['reviews_per_month'].describe().to_string())
print(f'Share with reviews_per_month == 0: {(df["reviews_per_month"] == 0).mean():.3f}')
print()

# Correlations
print('--- correlation matrix on modelling features ---')
print(df[MODELLING_COLS].corr().round(3).to_string())
print()

# Hosts
print('--- calculated_host_listings_count ---')
print(df['calculated_host_listings_count'].describe().to_string())
print()
print(f'--- top {TOP_N_HOSTS} host_id by listing count ---')
print(df.groupby('host_id').size().sort_values(ascending=False).head(TOP_N_HOSTS).to_string())

sys.stdout = original_stdout
log.close()
print(f'Written: {LOG_FILE}')
