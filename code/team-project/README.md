# Team Project: Project Report (Unit 6) - Track 1 source bundle

Track 1: classical machine learning regression and clustering on the AB_NYC_2019 Airbnb dataset (Dgomonov, 2019). This folder is the live bundle of source scripts, run outputs and figures that supports the [Team Project deep page on the e-portfolio site](https://protode908.github.io/eportfolio-uoe/projects/team-project/). It reflects the v1.6 development snapshot; later snapshots will replace files in place.

## Layout

- `source/` - the five-step Python pipeline (currently v1.6 of steps 01 and 02; 03-05 + figure3 land here as they are finalised).
- `data/` - cleaned and clustered Airbnb CSVs produced by the pipeline.
- `logs/` - run logs for each pipeline stage.
- `tables/` - numerical result tables (regression metrics, regression coefficients, cluster profiles and cluster cross-tabs).
- `figures/` - PNG figures emitted by the pipeline.

## Files in this v1.6 drop

### `source/`

- `01_data_prep_v1.6.py` - cleaning, mapping and q99 price cap.
- `02_data_exploration_v1.6.py` - profiling, percentile reporting, shares, correlations.

### `data/`

- `AB_NYC_2019_cleaned.csv` - cleaned data, 48,847 rows.
- `AB_NYC_2019_clustered.csv` - same data with the current cluster column added.

### `logs/`

- `clustering.log` - features used, K sweep across 2..6, current K=3 profiles, cross-tabs.
- `regression.log` - VIF, correlations, metrics across linear / multi-linear / polynomial, coefficients.
- (future: `cleaning.log`, `exploration.log`)

### `tables/`

- `regression_metrics.csv` - R², MAE, MSE, RMSE.
- `regression_coefficients.csv` - scaled coefficients.
- `cluster_profiles.csv` - current K=3 profiles.
- `cluster_crosstab_room_type.csv` - cluster by room type.
- `cluster_crosstab_neighbourhood_group.csv` - cluster by neighbourhood group.

### `figures/`

- `fig_cluster_scatter_v1.6.png` - current K=3 segment scatter.
- `fig_price_heatmap_v1.6.png` - median price by neighbourhood group and room type.
- (future: price distribution, neighbourhood share, room-type share, correlation heatmap, minimum_nights, demand signals, regression evidence, k-means diagnostics, silhouette by segment, model performance, CRISP-DM flow diagram source)
