import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error

# Loading clean dataset
df2_clean= pd.read_csv('datasets/processed/Peds_ED_visits.csv')
df2_clean.columns

# Wanted to use as a target variable the Asthma related Peds ED visits from ages 0-17 years old per 100 visits data:
X = df2_clean.drop('asthmarelateded_visitsper100age0to17', axis=1)
y = df2_clean['asthmarelateded_visitsper100age0to17']

# Initialize the StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Assuming y_train and y_test are continuous (regression task)
# Instantiate and train a dummy regressor
dummy_regressor = DummyRegressor(strategy='mean')
dummy_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred_dummy = dummy_regressor.predict(X_test)

# Evaluate using a regression metric like Mean Squared Error
mse_dummy = mean_squared_error(y_test, y_pred_dummy)
print(f'Mean Squared Error (Dummy): {mse_dummy}')

# Save the model (replace 'your_model_path' with the actual path)
import joblib
joblib.dump(xgboost, 'your_model_path/xgboost_model.pkl')









############################################
# Pick the observation in the validation set for which explanation is required
observation_1 = 20
# Get the explanation for Logistic Regression and show the prediction
exp = explainer.explain_instance(X_val[observation_1], xgboost.predict_proba, num_features=9)
exp.save_to_file('WK9/code/model_dev/models/observation_1.html')

## save the model
pickle.dump(xgboost, open('WK9/code/model_dev/models/xgboost_100k.sav', 'wb'))