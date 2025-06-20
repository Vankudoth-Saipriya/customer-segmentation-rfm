import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load RFM metrics
rfm = pd.read_csv("rfm.csv")

# Scale RFM
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

# Apply KMeans with 4 clusters
model = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = model.fit_predict(rfm_scaled)

# Save updated RFM with clusters
rfm.to_csv("rfm.csv", index=False)

print("✅ Clusters added and saved to rfm.csv")
