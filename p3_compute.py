import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
import joblib
from lime.lime_tabular import LimeTabularExplainer
import pickle

# Loading clean dataset #1:
df1_clean = pd.read_csv('datasets/processed/LeadBloodLevels_2017_byMSA.csv')

# Using as a target variable the percent of individuals, under 18 years of age, with an elevated blood lead level (defined as  > 4.5 μg/dL).
X1 = df1_clean.drop('pctunder18ebll', axis=1)
y1 = df1_clean['pctunder18ebll']

# Initialize the StandardScaler
scaler = StandardScaler()
X_scale1 = scaler.fit_transform(X1)

# Split the data into training and testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(X_scaled, y1, test_size=0.2, random_state=42)

# Instantiate and train a dummy regressor
dummy_regressor = DummyRegressor(strategy='mean')
dummy_regressor.fit(X_train1, y_train1)

# Make predictions on the test set
y_pred_dummy = dummy_regressor.predict(X_test1)

# Evaluate using a regression metric like Mean Squared Error
mse_dummy1 = mean_squared_error(y_test1, y_pred_dummy)
print(f'Mean Squared Error (Dummy): {mse_dummy}')

# Instantiate and train an XGBoost regressor
xgboost = XGBRegressor()
xgboost.fit(X_train1, y_train1)

# Make predictions on the test set
y_pred_xgboost = xgboost.predict(X_test1)

# Evaluate using a regression metric like Mean Squared Error
mse_xgboost = mean_squared_error(y_test1, y_pred_xgboost)
print(f'Mean Squared Error (XGBoost): {mse_xgboost}')

# Save the XGBoost model
joblib.dump(xgboost, 'datasets/processed/df1_clean_computed.pkl')

###############################
# Loading clean dataset #2:
df2_clean= pd.read_csv('datasets/processed/Peds_ED_visits.csv')
df2_clean.columns

# Wanted to use as a target variable the Asthma related Peds ED visits from ages 0-17 years old per 100 visits data:
X = df2_clean.drop('asthmarelateded_visitsper100age0to17', axis=1)
y = df2_clean['asthmarelateded_visitsper100age0to17']

# Initialize the StandardScaler
scaler = StandardScaler()
X_scaled2 = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_scaled2, y, test_size=0.2, random_state=42)

# Assuming y_train and y_test are continuous (regression task)
# Instantiate and train a dummy regressor
dummy_regressor = DummyRegressor(strategy='mean')
dummy_regressor.fit(X_train2, y_train2)

# Make predictions on the test set
y_pred_dummy = dummy_regressor.predict(X_test2)

# Evaluate using a regression metric like Mean Squared Error
mse_dummy2 = mean_squared_error(y_test2, y_pred_dummy)
print(f'Mean Squared Error (Dummy): {mse_dummy2}')

# Instantiate and train an XGBoost regressor
xgboost = XGBRegressor()
xgboost.fit(X_train2, y_train2)

# Make predictions on the test set
y_pred_xgboost = xgboost.predict(X_test2)

# Evaluate using a regression metric like Mean Squared Error
mse_xgboost = mean_squared_error(y_test2, y_pred_xgboost)
print(f'Mean Squared Error (XGBoost): {mse_xgboost}')

# Save the XGBoost model
joblib.dump(xgboost, 'datasets/processed/df2_computed.pkl')