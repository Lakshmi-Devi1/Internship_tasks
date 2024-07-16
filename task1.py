import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
train_file_path = r'C:\Users\lakshmi devi\Desktop\gowtham\4K Video\train.xlsx'
df_train = pd.read_excel(train_file_path)
X_train = df_train[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18']].values
test_file_path = r'C:\Users\lakshmi devi\Desktop\gowtham\4K Video\test.xlsx'
df_test = pd.read_excel(test_file_path)
X_test = df_test[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18']].values
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_train_scaled)
test_cluster_labels = kmeans.predict(X_test_scaled)
print("Predicted clusters for test data:")
for i, label in enumerate(test_cluster_labels):
    print(f"Data point {i+1}: Cluster {label}")


