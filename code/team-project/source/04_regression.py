import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# === CONFIG ===
INPUT_CSV = 'AB_NYC_2019_cleaned.csv'
LOG_FILE = 'regression.log'
METRICS_CSV = 'regression_metrics.csv'
COEF_CSV = 'regression_coefficients.csv'
FIGURES_DIR = 'figures'

FEATURES = [
    'room_type_code', 'neighbourhood_group_code',
    'latitude', 'longitude', 'minimum_nights',
    'number_of_reviews', 'reviews_per_month',
    'availability_365', 'calculated_host_listings_count'
]
TARGET = 'log_price'

# Single 80/20 train/test split. Cross-validation would be a better future check.
TEST_SIZE = 0.2
RANDOM_STATE = 1

# Exploratory polynomial model to test whether simple interactions improve R2.
# Results are used for comparison only, not for deployment.
POLY_DEGREE = 2

# VIF threshold used as a simple diagnostic only.
VIF_THRESHOLD = 5.0

DPI = 300
COLOR_PRIMARY = 'steelblue'
COLOR_SECONDARY = 'darkorange'
# === END CONFIG ===

os.makedirs(FIGURES_DIR, exist_ok=True)
df = pd.read_csv(INPUT_CSV)

X = df[FEATURES]
y = df[TARGET]

# Categorical columns use simple numeric codes for this exploratory model.
# A better version would use fuller one-hot/dummy encoding, as noted in the report limitations.

# VIF diagnostic: check whether any feature has high multicollinearity.
vif_rows = []
for col in X.columns:
    y_i = X[col]
    X_i = X.drop(columns=[col])
    reg_i = LinearRegression()
    reg_i.fit(X_i, y_i)
    r2 = reg_i.score(X_i, y_i)
    if r2 >= 1.0:
        vif_value = float('inf')
    else:
        vif_value = 1.0 / (1.0 - r2)
    vif_rows.append({'feature': col, 'VIF': vif_value})
vif_initial = pd.DataFrame(vif_rows)

# Keep all features in this student model. VIF is reported only as a diagnostic.
X_model = X

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(X_model, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

# Feature scaling. Fit on training data only and apply to test data.
# This helps the polynomial model and makes coefficients easier to compare.
scaler = StandardScaler()
X_train_scaled_arr = scaler.fit_transform(X_train)
X_test_scaled_arr = scaler.transform(X_test)
X_train_scaled = pd.DataFrame(X_train_scaled_arr, columns=X_train.columns, index=X_train.index)
X_test_scaled = pd.DataFrame(X_test_scaled_arr, columns=X_test.columns, index=X_test.index)

# Baseline model: room type only, because room type is central to the business question.
baseline_feature = 'room_type_code'

# Keep a simple correlation check for context, not for choosing the baseline.
correlations_raw = X_train.corrwith(y_train)
correlations_abs = correlations_raw.abs()
correlations = correlations_abs.sort_values(ascending=False)

# Model 1: simple linear regression on the baseline feature
lin_single = LinearRegression()
lin_single.fit(X_train_scaled[[baseline_feature]], y_train)
y_pred_single = lin_single.predict(X_test_scaled[[baseline_feature]])

# Model 2: multiple linear regression on all features (scaled)
lin_multi = LinearRegression()
lin_multi.fit(X_train_scaled, y_train)
y_pred_multi = lin_multi.predict(X_test_scaled)

# Model 3: exploratory polynomial regression, degree 2, on scaled features
poly = PolynomialFeatures(degree=POLY_DEGREE, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)
lin_poly = LinearRegression()
lin_poly.fit(X_train_poly, y_train)
y_pred_poly = lin_poly.predict(X_test_poly)

# Metrics - Model 1
r2_single = r2_score(y_test, y_pred_single)
mae_single = mean_absolute_error(y_test, y_pred_single)
mse_single = mean_squared_error(y_test, y_pred_single)
rmse_single = float(np.sqrt(mse_single))

# Metrics - Model 2
r2_multi = r2_score(y_test, y_pred_multi)
mae_multi = mean_absolute_error(y_test, y_pred_multi)
mse_multi = mean_squared_error(y_test, y_pred_multi)
rmse_multi = float(np.sqrt(mse_multi))

# Metrics - Model 3
r2_poly = r2_score(y_test, y_pred_poly)
mae_poly = mean_absolute_error(y_test, y_pred_poly)
mse_poly = mean_squared_error(y_test, y_pred_poly)
rmse_poly = float(np.sqrt(mse_poly))

# Assemble metrics table (parallel lists -> DataFrame)
metrics_data = {
    'model': [
        'Linear (room type only)',
        'Multiple linear (scaled)',
        'Polynomial degree ' + str(POLY_DEGREE) + ' (scaled)'
    ],
    'R2': [r2_single, r2_multi, r2_poly],
    'MAE': [mae_single, mae_multi, mae_poly],
    'MSE': [mse_single, mse_multi, mse_poly],
    'RMSE': [rmse_single, rmse_multi, rmse_poly]
}
metrics_df = pd.DataFrame(metrics_data)
metrics_df.to_csv(METRICS_CSV, index=False)

# Coefficients (multiple linear on scaled features) sorted by absolute magnitude
coef_df = pd.DataFrame({'feature': X_model.columns, 'coefficient': lin_multi.coef_})
coef_df['abs_coefficient'] = coef_df['coefficient'].abs()
coef_df = coef_df.sort_values('abs_coefficient', ascending=False)
coef_df = coef_df.drop(columns=['abs_coefficient'])
coef_df.to_csv(COEF_CSV, index=False)

# Figure: model performance, built from the metrics just calculated.
# This keeps the chart tied to the current regression run.
model_labels = ['Room type only', 'Multiple linear', 'Polynomial degree ' + str(POLY_DEGREE)]
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(model_labels, metrics_df['R2'], color=COLOR_PRIMARY, edgecolor='white', width=0.55)
for i, bar in enumerate(bars):
    r2_value = metrics_df.loc[i, 'R2']
    rmse_value = metrics_df.loc[i, 'RMSE']
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.012,
            f'R² = {r2_value:.2f}\nRMSE = {rmse_value:.2f}',
            ha='center', va='bottom', fontsize=10)
ax.set_ylim(0, max(0.7, float(metrics_df['R2'].max()) + 0.1))
ax.set_ylabel('R² on log_price test set')
ax.set_title('Regression model performance')
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_model_performance.png', dpi=DPI)
plt.close()

# Figure: predicted vs actual + residuals (multiple linear)
residuals = y_test - y_pred_multi
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].scatter(y_test, y_pred_multi, alpha=0.15, s=8, color=COLOR_PRIMARY)
lo = y_test.min()
hi = y_test.max()
ax[0].plot([lo, hi], [lo, hi], color='red', linewidth=1)
ax[0].set_xlabel('Actual log_price')
ax[0].set_ylabel('Predicted log_price')
ax[0].set_title('Multiple linear: predicted vs actual')
ax[1].hist(residuals, bins=60, color=COLOR_SECONDARY, edgecolor='white')
ax[1].set_xlabel('Residual')
ax[1].set_ylabel('Listings')
ax[1].set_title('Residual distribution')
plt.tight_layout()
plt.savefig(FIGURES_DIR + '/fig_regression_evidence.png', dpi=DPI)
plt.close()

# Log
log = open(LOG_FILE, 'w')
print('=== Regression run log ===', file=log)
print('', file=log)
print(f'Rows: {len(df)}', file=log)
print(f'Features: {FEATURES}', file=log)
print(f'Target: {TARGET}', file=log)
print(f'Train/test split: {1.0 - TEST_SIZE:.2f} / {TEST_SIZE:.2f}, random_state = {RANDOM_STATE}', file=log)
print('Note: single train/test split is used; cross-validation would be a better future check.', file=log)
print('Note: categorical fields use simple numeric codes in this exploratory version.', file=log)
print('Note: features are standardised (z-score) using training-set statistics only.', file=log)
print('', file=log)
print('--- VIF diagnostic ---', file=log)
print(vif_initial.round(3).to_string(index=False), file=log)
print(f'No automatic feature removal is applied; VIF threshold reference = {VIF_THRESHOLD}.', file=log)
print('', file=log)
print(f'Feature set used for multiple / polynomial: {list(X_model.columns)}', file=log)
print('', file=log)
print(f'Baseline model: {baseline_feature} only (chosen from the business question)', file=log)
print('--- Feature absolute correlation with target (training set, context only) ---', file=log)
print(correlations.round(3).to_string(), file=log)
print('', file=log)
print('--- Model metrics (test set) ---', file=log)
print(metrics_df.round(4).to_string(index=False), file=log)
print('', file=log)
print('--- Multiple linear coefficients on scaled features (sorted by |coefficient|) ---', file=log)
print(coef_df.round(4).to_string(index=False), file=log)
print(f'Intercept (multi): {lin_multi.intercept_:.4f}', file=log)
print('', file=log)
print('--- Residuals summary ---', file=log)
print(residuals.describe().round(4).to_string(), file=log)
log.close()

print('Regression run complete. Outputs: regression.log, regression_metrics.csv, regression_coefficients.csv, figures/fig_model_performance.png, figures/fig_regression_evidence.png')
