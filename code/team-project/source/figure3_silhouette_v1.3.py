import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples
from sklearn.preprocessing import StandardScaler

# === CONFIG ===
# This script is only for Figure 3: silhouette quality by listing segment.
# It is self-contained: it uses the cleaned file if available, otherwise it applies
# the same simple cleaning steps to the original AB_NYC_2019.csv file.
CLEAN_INPUT_CSV = 'AB_NYC_2019_cleaned.csv'
RAW_INPUT_CSV = 'AB_NYC_2019.csv'

FIGURES_DIR = 'figures'
OUTPUT_FIGURE = 'fig3_silhouette_by_segment.png'
OUTPUT_SCORES_CSV = 'figure3_silhouette_scores.csv'
LOG_FILE = 'figure3_silhouette.log'

ROOM_TYPE_MAP = {'Entire home/apt': 1, 'Private room': 2, 'Shared room': 3}
NEIGHBOURHOOD_GROUP_MAP = {'Manhattan': 1, 'Brooklyn': 2, 'Queens': 3, 'Bronx': 4, 'Staten Island': 5}
MIN_NIGHTS_QUANTILE = 0.99

NUMERIC_CLUSTER_FEATURES = [
    'log_price',
    'minimum_nights',
    'reviews_per_month',
    'availability_365'
]
ROOM_TYPE_COLUMN = 'room_type'

K_CHOSEN = 3
RANDOM_STATE = 1
N_INIT = 10

# Full dataset calculation. This can take time because silhouette compares listings to one another.
USE_FULL_DATASET = True

DPI = 300
SEGMENT_ORDER = ['Entire-home segment', 'Private-room segment', 'Shared-room segment']
SEGMENT_COLOURS = ['#9ecae1', '#f4a6a6', '#fdd27c']
# === END CONFIG ===

os.makedirs(FIGURES_DIR, exist_ok=True)

# Load the cleaned file if it exists. If not, clean the raw file so this script can run on its own.
if os.path.exists(CLEAN_INPUT_CSV):
    df = pd.read_csv(CLEAN_INPUT_CSV)
    data_source = CLEAN_INPUT_CSV
else:
    if not os.path.exists(RAW_INPUT_CSV):
        raise FileNotFoundError(
            'Could not find AB_NYC_2019_cleaned.csv or AB_NYC_2019.csv in this folder.'
        )

    df = pd.read_csv(RAW_INPUT_CSV)
    data_source = RAW_INPUT_CSV + ' cleaned inside this script'

    # Same practical cleaning logic used in the main data preparation script.
    df.loc[df['number_of_reviews'] == 0, 'reviews_per_month'] = 0
    df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
    df = df[df['name'].notna() & df['host_name'].notna()]
    df = df[df['price'] > 0]
    df['log_price'] = np.log1p(df['price'])
    df['room_type_code'] = df['room_type'].map(ROOM_TYPE_MAP)
    df['neighbourhood_group_code'] = df['neighbourhood_group'].map(NEIGHBOURHOOD_GROUP_MAP)
    q99 = df['minimum_nights'].quantile(MIN_NIGHTS_QUANTILE)
    df['minimum_nights'] = df['minimum_nights'].clip(upper=q99)

# Check the columns needed for this plot.
needed_cols = NUMERIC_CLUSTER_FEATURES + [ROOM_TYPE_COLUMN]
missing_cols = [col for col in needed_cols if col not in df.columns]
if missing_cols:
    raise ValueError('Missing required columns for Figure 3: ' + str(missing_cols))

# Keep only rows that have the fields needed for clustering.
df = df.dropna(subset=needed_cols).copy()

# Build the same style of clustering feature matrix used in the main clustering script.
X_numeric = df[NUMERIC_CLUSTER_FEATURES]
X_room_dummies = pd.get_dummies(df[ROOM_TYPE_COLUMN], prefix='room_type', drop_first=False)
X = pd.concat([X_numeric, X_room_dummies], axis=1)

# Standardise before K-Means because the fields are on different scales.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit the selected K = 3 solution.
km = KMeans(n_clusters=K_CHOSEN, random_state=RANDOM_STATE, n_init=N_INIT)
cluster_labels = km.fit_predict(X_scaled)
df['cluster'] = cluster_labels

# Name each cluster using its most common room type.
cluster_to_segment = {}
for cluster_id in sorted(df['cluster'].unique()):
    dominant_room = df.loc[df['cluster'] == cluster_id, ROOM_TYPE_COLUMN].mode().iloc[0]
    if dominant_room == 'Entire home/apt':
        cluster_to_segment[cluster_id] = 'Entire-home segment'
    elif dominant_room == 'Private room':
        cluster_to_segment[cluster_id] = 'Private-room segment'
    else:
        cluster_to_segment[cluster_id] = 'Shared-room segment'

df['segment_name'] = df['cluster'].map(cluster_to_segment)

# Calculate one silhouette score per listing for the selected K = 3 solution.
# Higher values mean the listing fits its assigned segment more clearly.
sil_values = silhouette_samples(X_scaled, cluster_labels)

silhouette_df = pd.DataFrame({
    'cluster': df['cluster'].values,
    'segment_name': df['segment_name'].values,
    'silhouette_score': sil_values
})
silhouette_df.to_csv(OUTPUT_SCORES_CSV, index=False)

# Prepare data for plotting in a fixed segment order.
plot_data = []
plot_labels = []
plot_colours = []
for i, segment in enumerate(SEGMENT_ORDER):
    values = silhouette_df.loc[silhouette_df['segment_name'] == segment, 'silhouette_score']
    if len(values) > 0:
        plot_data.append(values.values)
        plot_labels.append(segment)
        plot_colours.append(SEGMENT_COLOURS[i])

fig, ax = plt.subplots(figsize=(9.5, 5.6))
box = ax.boxplot(
    plot_data,
    labels=plot_labels,
    patch_artist=True,
    showfliers=True,
    medianprops={'color': 'black', 'linewidth': 1.5},
    whiskerprops={'color': 'black'},
    capprops={'color': 'black'},
    flierprops={
        'marker': 'o',
        'markerfacecolor': 'white',
        'markeredgecolor': 'black',
        'markersize': 4,
        'linestyle': 'none'
    }
)

for patch, colour in zip(box['boxes'], plot_colours):
    patch.set_facecolor(colour)
    patch.set_alpha(0.75)
    patch.set_edgecolor('black')

# Add red dashed mean lines inside each box.
for pos, values in enumerate(plot_data, start=1):
    mean_value = float(np.mean(values))
    ax.plot([pos - 0.25, pos + 0.25], [mean_value, mean_value],
            color='red', linestyle='--', linewidth=1.5)

ax.axhline(0, color='gray', linestyle='--', linewidth=1)
ax.set_title('Silhouette quality by listing segment (K = 3)')
ax.set_ylabel('Silhouette score')
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()

figure_path = os.path.join(FIGURES_DIR, OUTPUT_FIGURE)
plt.savefig(figure_path, dpi=DPI)
plt.close()

# Simple log for checking results.
summary = silhouette_df.groupby('segment_name')['silhouette_score'].agg(['count', 'mean', 'median', 'min', 'max']).round(4)

log = open(LOG_FILE, 'w')
print('=== Figure 3 silhouette plot log ===', file=log)
print('', file=log)
print(f'Data source: {data_source}', file=log)
print(f'Rows used: {len(df)}', file=log)
print(f'Cluster features: {NUMERIC_CLUSTER_FEATURES} + room_type dummy fields', file=log)
print(f'Dummy columns: {list(X_room_dummies.columns)}', file=log)
print(f'K chosen: {K_CHOSEN}', file=log)
print(f'random_state = {RANDOM_STATE}, n_init = {N_INIT}', file=log)
print(f'Full dataset silhouette calculation: {USE_FULL_DATASET}', file=log)
print('', file=log)
print('Cluster ID to segment label:', file=log)
for cluster_id in sorted(cluster_to_segment.keys()):
    print(f'  Cluster {cluster_id}: {cluster_to_segment[cluster_id]}', file=log)
print('', file=log)
print('Silhouette summary by segment:', file=log)
print(summary.to_string(), file=log)
print('', file=log)
print(f'Figure saved to: {figure_path}', file=log)
print(f'Scores saved to: {OUTPUT_SCORES_CSV}', file=log)
log.close()

print('Figure 3 silhouette plot complete.')
print('Figure saved to: ' + figure_path)
print('Scores saved to: ' + OUTPUT_SCORES_CSV)
print('Log written to: ' + LOG_FILE)
