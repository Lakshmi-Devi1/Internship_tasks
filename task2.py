import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
train_file_path = r'C:\Users\lakshmi devi\Desktop\gowtham\4K Video\train.xlsx'
df_train = pd.read_excel(train_file_path)
X_train = df_train[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18']].values
y_train = df_train['target'].values  # Assuming 'Target' is the name of the target column
test_file_path = r'C:\Users\lakshmi devi\Desktop\gowtham\4K Video\test.xlsx'
df_test = pd.read_excel(test_file_path)
X_test = df_test[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18']].values
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_reg = LogisticRegression(random_state=42)
rf_clf = RandomForestClassifier(random_state=42)

log_reg.fit(X_train_scaled, y_train)
rf_clf.fit(X_train_scaled, y_train)

y_train_pred_log_reg = log_reg.predict(X_train_scaled)
y_train_pred_rf_clf = rf_clf.predict(X_train_scaled)

train_accuracy_log_reg = accuracy_score(y_train, y_train_pred_log_reg)
train_accuracy_rf_clf = accuracy_score(y_train, y_train_pred_rf_clf)

print(f"Logistic Regression Train Accuracy: {train_accuracy_log_reg:.4f}")
print(f"Random Forest Train Accuracy: {train_accuracy_rf_clf:.4f}")

test_pred_log_reg = log_reg.predict(X_test_scaled)
test_pred_rf_clf = rf_clf.predict(X_test_scaled)

df_test_predictions = pd.DataFrame({
    'Logistic Regression': test_pred_log_reg,
    'Random Forest': test_pred_rf_clf
})
output_file_path = r'C:\Users\lakshmi devi\Desktop\gowtham\4K Video\test_predictions.csv'
df_test_predictions.to_csv(output_file_path, index=False)

print(f"Predicted target values for test data saved to {output_file_path}")
