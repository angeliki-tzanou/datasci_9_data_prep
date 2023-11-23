import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.dummy import DummyClassifier
from xgboost import XGBClassifier

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Drop rows with missing values
df.dropna(inplace=True)

# Define the features and the target variable
X = df.drop('AsthmaRelatedED_VisitsPer100Age0to17', axis=1)
y = df['AsthmaRelatedED_VisitsPer100Age0to17']

# Initialize the StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Dummy Classifier (Baseline)
dummy = DummyClassifier(strategy='most_frequent')
dummy.fit(X_train, y_train)
y_pred_dummy = dummy.predict(X_test)
accuracy_dummy = accuracy_score(y_test, y_pred_dummy)

# Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred_logreg = log_reg.predict(X_test)
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)

# XGBoost Classifier
xgboost = XGBClassifier()
xgboost.fit(X_train, y_train)
y_pred_xgboost = xgboost.predict(X_test)
accuracy_xgboost = accuracy_score(y_test, y_pred_xgboost)

# Print results
print(f"Baseline accuracy: {accuracy_dummy}")
print(f"Logistic Regression accuracy: {accuracy_logreg}")
print(f"XGBoost accuracy: {accuracy_xgboost}")

# Additional analysis, if needed
print("\nClassification Report (Logistic Regression):")
print(classification_report(y_test, y_pred_logreg))

# Save the model (replace 'your_model_path' with the actual path)
import joblib
joblib.dump(xgboost, 'your_model_path/xgboost_model.pkl')
