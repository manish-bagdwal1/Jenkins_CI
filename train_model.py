import numpy as np
import pandas as pd
import pickle

# Sklearn modules
from sklearn.model_selection import train_test_split, GridSearchCV, ShuffleSplit, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# -----------------------------
# 1. Load and Clean the Dataset
# -----------------------------
df = pd.read_csv('kaggle_diabetes.csv')
df.rename(columns={'DiabetesPedigreeFunction': 'DPF'}, inplace=True)

# Replace invalid zeros with NaN
replace_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[replace_cols] = df[replace_cols].replace(0, np.nan)

# Fill NaN values with appropriate statistics
df['Glucose'].fillna(df['Glucose'].mean(), inplace=True)
df['BloodPressure'].fillna(df['BloodPressure'].mean(), inplace=True)
df['SkinThickness'].fillna(df['SkinThickness'].median(), inplace=True)
df['Insulin'].fillna(df['Insulin'].median(), inplace=True)
df['BMI'].fillna(df['BMI'].median(), inplace=True)

# -----------------------------
# 2. Feature Engineering
# -----------------------------
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# -----------------------------
# 3. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# -----------------------------
# 4. Feature Scaling
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# 5. Model Selection (optional)
# -----------------------------
# You can implement model comparison using GridSearchCV here if needed

# -----------------------------
# 6. Train Final Model
# -----------------------------
classifier = RandomForestClassifier(n_estimators=20, random_state=0)
classifier.fit(X_train_scaled, y_train)

# -----------------------------
# 7. Model Evaluation
# -----------------------------
train_pred = classifier.predict(X_train_scaled)
test_pred = classifier.predict(X_test_scaled)

train_acc = accuracy_score(y_train, train_pred) * 100
test_acc = accuracy_score(y_test, test_pred) * 100

print(f"Training Accuracy: {train_acc:.2f}%")
print(f"Test Accuracy: {test_acc:.2f}%")

# -----------------------------
# 8. Save Model & Scaler
# -----------------------------
with open('rf_classifier.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("✅ Model and scaler saved as 'rf_classifier.pkl' and 'scaler.pkl'")
