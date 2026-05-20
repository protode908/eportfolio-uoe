import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# === CONFIG ===
INPUT_CSV = 'AB_NYC_2019_cleaned.csv'
LOG_FILE = 'clustering.log'
PROFILES_CSV = 'cluster_profiles.csv'
CROSSTAB_RT_CSV = 'cluster_crosstab_room_type.csv'
CROSSTAB_NG_CSV = 'cluster_crosstab_neighbourhood_group.csv'
CLUSTERED_CSV = 'AB_NYC_2019_clustered.csv'
FIGURES_DIR = 'figures'

# Numeric cluster features. room_type is added as dummy fields because the business question
# is about practical listing segments. These clusters should be read as listing groups,
# not hidden customer segments.
NUMERIC_CLUSTER_FEATURES = [
    'log_price',
    'minimum_nights', 'reviews_per_month',
    'availability_365'
]
ROOM_TYPE_COLUMN = 'room_type'

K_RANGE = list(range(2, 7))
K_VALUES_TO_HIGHLIGHT = [3, 5]
K_CHOSEN = 3

RANDOM_STATE = 1
N_INIT = 10
# Calculate silhouette on a sample so the script runs in reasonable time.
SILHOUETTE_SAMPLE_SIZE = 10000
SCATTER_X = 'log_price'
SCATTER_Y = 'availability_365'
# Sample 50% of points for the scatter so dense areas are readable (deterministic via random_state).
SCATTER_SAMPLE_FRACTION = 0.5

DPI = 300
COLOR_PRIMARY = 'steelblue'
SCATTER_ALPHA = 0.15
SCATTER_SIZE = 8
# === END CONFIG ===

os.makedirs(FIGURES_DIR, exist_ok=True)
df = pd.read_csv(INPUT_CSV)

# Build feature matrix: numeric features + one-hot fields for room_type.
X_numeric = df[NUMERIC_CLUSTER_FEATURES]
X_room_dummies = pd.get_dummies(df[ROOM_TYPE_COLUMN], prefix='room_type', drop_first=False)
X = pd.concat([X_numeric, X_room_dummies], axis=1)

# Standardise features because K-Means uses distances and the columns have different scales.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow + silhouette sweep
inertias = []
silhouettes = []
for k in K_RANGE:
    km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=N_INIT)
    labels_k = km.fit_predict(X_scaled)
    inertias.append(km.inertia_)
    sil = silhouette_score(X_scaled, labels_k, sample_size=SILHOUETTE_SAMPLE_SIZE, random_state=RANDOM_STATE)
    silhouettes.append(sil)

# Elbow + silhouette diagnostics figure (two panels, kept for the e-Portfolio supporting evidence)
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(K_RANGE, inertias, marker='o', color=COLOR_PRIMARY)
for k in K_VALUES_TO_HIGHLIGHT:
    if k in K_RANGE:
        ax[0].axvline(k, color='gray', linestyle='--', alpha=0.5, linewidth=1)
ax[0].set_xlabel('K')
ax[0].set_ylabel('Inertia (SSE)')
ax[0].set_title('K-Means elbow plot')
ax[0].grid(alpha=0.3)
ax[1].plot(K_RANGE, silhouettes, marker='o', color=COLOR_PRIMARY)
for k in K_VALUES_TO_HIGHLIGHT:
    if k in K_RANGE:
        ax[1].axvline(k, color='gray', linestyle='--', alpha=0.5, linewidth=1)
ax[1].set_xlabel('K')
ax[1].set_ylabel('Silhouette score')
ax[1].set_title('Silhouette score by K')
ax[1].grid(alpha=0.3)
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_kmeans_diagnostics.png', dpi=DPI)
plt.close()

# Final fit at chosen K
km_final = KMeans(n_clusters=K_CHOSEN, random_state=RANDOM_STATE, n_init=N_INIT)
clusters = km_final.fit_predict(X_scaled)
df['cluster'] = clusters

# Name each cluster using its most common room_type.
cluster_to_label = {}
for c in sorted(df['cluster'].unique()):
    dominant_room = df.loc[df['cluster'] == c, 'room_type'].mode().iloc[0]
    if dominant_room == 'Entire home/apt':
        cluster_to_label[c] = 'Entire-home segment'
    elif dominant_room == 'Private room':
        cluster_to_label[c] = 'Private-room segment'
    else:
        cluster_to_label[c] = 'Shared-room segment'

# Cluster profiles on the numeric features only (dummies are not interpretable as means)
profiles = df.groupby('cluster')[NUMERIC_CLUSTER_FEATURES].mean().round(3)
profiles['count'] = df.groupby('cluster').size()
profiles['share'] = (profiles['count'] / len(df)).round(3)
profiles.to_csv(PROFILES_CSV)

# Cross-tabs (counts)
crosstab_rt = pd.crosstab(df['cluster'], df['room_type'])
crosstab_ng = pd.crosstab(df['cluster'], df['neighbourhood_group'])
crosstab_rt.to_csv(CROSSTAB_RT_CSV)
crosstab_ng.to_csv(CROSSTAB_NG_CSV)

# Cross-tabs (row percentages) computed step by step
rt_row_sums = crosstab_rt.sum(axis=1)
crosstab_rt_pct = crosstab_rt.div(rt_row_sums, axis=0)
crosstab_rt_pct = crosstab_rt_pct.round(3)
ng_row_sums = crosstab_ng.sum(axis=1)
crosstab_ng_pct = crosstab_ng.div(ng_row_sums, axis=0)
crosstab_ng_pct = crosstab_ng_pct.round(3)

# Save clustered CSV for downstream use
df.to_csv(CLUSTERED_CSV, index=False)

# 2D scatter with named segments and centroid X markers.
df_plot = df.sample(frac=SCATTER_SAMPLE_FRACTION, random_state=RANDOM_STATE)

fig, ax = plt.subplots(figsize=(10, 6))
unique_clusters = sorted(df_plot['cluster'].unique())
for c in unique_clusters:
    mask = df_plot['cluster'] == c
    ax.scatter(df_plot.loc[mask, SCATTER_X], df_plot.loc[mask, SCATTER_Y],
               alpha=SCATTER_ALPHA, s=SCATTER_SIZE, label=cluster_to_label[c])

# Centroid markers (computed on the full cluster, not the sampled view)
for c in unique_clusters:
    cluster_full = df[df['cluster'] == c]
    cx = cluster_full[SCATTER_X].mean()
    cy = cluster_full[SCATTER_Y].mean()
    ax.scatter(cx, cy, marker='X', s=400, c='black',
               edgecolor='white', linewidth=2, zorder=5)

ax.set_xlabel('log price per night (higher = more expensive)')
ax.set_ylabel('availability (days per year)')
ax.set_title('NYC listing segments at K = ' + str(K_CHOSEN) + ': by price and availability')
ax.legend(markerscale=2.5, loc='upper left', framealpha=0.9)
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_cluster_scatter.png', dpi=DPI)
plt.close()

# Log
log = open(LOG_FILE, 'w')
print('=== Clustering run log ===', file=log)
print('', file=log)
print(f'Rows: {len(df)}', file=log)
print(f'Numeric cluster features: {NUMERIC_CLUSTER_FEATURES}', file=log)
print(f'Categorical encoded as dummy fields: {ROOM_TYPE_COLUMN}', file=log)
print('Note: room_type is included because this analysis is about practical listing segments.', file=log)
print(f'Dummy columns added: {list(X_room_dummies.columns)}', file=log)
print(f'Scaler: StandardScaler (z-score) applied to full feature matrix', file=log)
print(f'K range tested: {K_RANGE}', file=log)
print(f'K values highlighted on chart: {K_VALUES_TO_HIGHLIGHT}', file=log)
print(f'K chosen for final fit: {K_CHOSEN}', file=log)
print(f'random_state = {RANDOM_STATE}, n_init = {N_INIT}, silhouette sample size = {SILHOUETTE_SAMPLE_SIZE}', file=log)
print('', file=log)
print('--- Diagnostics by K (inertia + silhouette) ---', file=log)
for i in range(len(K_RANGE)):
    k = K_RANGE[i]
    inertia = inertias[i]
    sil = silhouettes[i]
    print(f'  K = {k}: inertia = {inertia:.2f}, silhouette = {sil:.4f}', file=log)
print('', file=log)
print('--- Cluster ID to segment label mapping ---', file=log)
for c in sorted(cluster_to_label.keys()):
    print(f'  Cluster {c}: {cluster_to_label[c]}', file=log)
print('', file=log)
print('--- Cluster profiles (numeric feature means + count + share) ---', file=log)
print(profiles.to_string(), file=log)
print('', file=log)
print('--- Cluster x room_type (counts) ---', file=log)
print(crosstab_rt.to_string(), file=log)
print('', file=log)
print('--- Cluster x room_type (row %) ---', file=log)
print(crosstab_rt_pct.to_string(), file=log)
print('', file=log)
print('--- Cluster x neighbourhood_group (counts) ---', file=log)
print(crosstab_ng.to_string(), file=log)
print('', file=log)
print('--- Cluster x neighbourhood_group (row %) ---', file=log)
print(crosstab_ng_pct.to_string(), file=log)
log.close()

print('Clustering run complete. Outputs: clustering.log, cluster_profiles.csv, cluster_crosstab_room_type.csv, cluster_crosstab_neighbourhood_group.csv, AB_NYC_2019_clustered.csv, figures/fig_kmeans_diagnostics.png, figures/fig_cluster_scatter.png')
