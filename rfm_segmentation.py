import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load RFM data
rfm = pd.read_csv("rfm.csv")

# Scale the RFM values
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

# Apply KMeans with k=4 (you can change if elbow showed another value)
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Save the segmented file
rfm.to_csv("rfm_segmented.csv", index=False)
print("✅ Customer segmentation completed and saved to rfm_segmented.csv")

# Optional: Visualize clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Recency', y='Monetary', hue='Cluster', data=rfm, palette='Set2')
plt.title('Customer Segments (Recency vs Monetary)')
plt.savefig("rfm_clusters.png")
plt.show()
