import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === CONFIG ===
INPUT_CSV = 'AB_NYC_2019_cleaned.csv'
FIGURES_DIR = 'figures'

DPI = 300
HIST_BINS_PRICE = 80
HIST_BINS_GENERAL = 50
PRICE_VIEW_QUANTILE = 0.99
REVIEWS_VIEW_QUANTILE = 0.99

COLOR_PRIMARY = 'steelblue'
COLOR_SECONDARY = 'darkorange'
CMAP_SEQUENTIAL = 'YlOrRd'
CMAP_DIVERGING = 'RdBu_r'

MODELLING_COLS = [
    'log_price', 'room_type_code', 'neighbourhood_group_code',
    'latitude', 'longitude', 'minimum_nights',
    'number_of_reviews', 'reviews_per_month',
    'availability_365', 'calculated_host_listings_count'
]
# === END CONFIG ===

os.makedirs(FIGURES_DIR, exist_ok=True)
df = pd.read_csv(INPUT_CSV)

# Figure: price distribution (raw + log)
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].hist(df['price'], bins=HIST_BINS_PRICE,
           range=(0, df['price'].quantile(PRICE_VIEW_QUANTILE)),
           color=COLOR_PRIMARY, edgecolor='white')
ax[0].set_title('Price (USD, view capped at q99)')
ax[0].set_xlabel('Price')
ax[0].set_ylabel('Listings')
ax[1].hist(df['log_price'], bins=HIST_BINS_PRICE,
           color=COLOR_SECONDARY, edgecolor='white')
ax[1].set_title('log1p(price)')
ax[1].set_xlabel('log1p(price)')
ax[1].set_ylabel('Listings')
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_price_distribution.png', dpi=DPI)
plt.close()

# Figure: listings per neighbourhood group
fig, ax = plt.subplots(figsize=(8, 4))
c = df['neighbourhood_group'].value_counts()
ax.bar(c.index, c.values, color=COLOR_PRIMARY, edgecolor='white')
ax.set_title('Listings per neighbourhood group')
ax.set_ylabel('Listings')
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_neighbourhood_share.png', dpi=DPI)
plt.close()

# Figure: listings per room type
fig, ax = plt.subplots(figsize=(8, 4))
c = df['room_type'].value_counts()
ax.bar(c.index, c.values, color=COLOR_SECONDARY, edgecolor='white')
ax.set_title('Listings per room type')
ax.set_ylabel('Listings')
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_room_type_share.png', dpi=DPI)
plt.close()

# Figure: median price heatmap (neighbourhood group x room type)
ct = df.pivot_table(index='neighbourhood_group', columns='room_type',
                    values='price', aggfunc='median')
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(ct, annot=True, fmt='.0f', cmap=CMAP_SEQUENTIAL, ax=ax)
ax.set_title('Median price (USD) by neighbourhood group x room type')
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_price_heatmap.png', dpi=DPI)
plt.close()

# Figure: correlation heatmap on modelling features
fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(df[MODELLING_COLS].corr(), annot=True, fmt='.2f',
            cmap=CMAP_DIVERGING, center=0, vmin=-1, vmax=1, ax=ax)
ax.set_title('Correlation matrix (modelling features)')
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_correlation_heatmap.png', dpi=DPI)
plt.close()

# Figure: minimum_nights post-cap
fig, ax = plt.subplots(figsize=(9, 4))
ax.hist(df['minimum_nights'], bins=HIST_BINS_GENERAL,
        color=COLOR_PRIMARY, edgecolor='white')
ax.set_title('Minimum nights (post-cap at q99)')
ax.set_xlabel('Minimum nights')
ax.set_ylabel('Listings')
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_minimum_nights.png', dpi=DPI)
plt.close()

# Figure: demand signals (availability + reviews_per_month)
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].hist(df['availability_365'], bins=HIST_BINS_GENERAL,
           color=COLOR_PRIMARY, edgecolor='white')
ax[0].set_title('Availability (days / year)')
ax[0].set_xlabel('Days available')
ax[0].set_ylabel('Listings')
ax[1].hist(df['reviews_per_month'], bins=HIST_BINS_GENERAL,
           range=(0, df['reviews_per_month'].quantile(REVIEWS_VIEW_QUANTILE)),
           color=COLOR_SECONDARY, edgecolor='white')
ax[1].set_title('Reviews per month (view capped at q99)')
ax[1].set_xlabel('Reviews per month')
ax[1].set_ylabel('Listings')
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_demand_signals.png', dpi=DPI)
plt.close()

print('Figures written to figures/')
