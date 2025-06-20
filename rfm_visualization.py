import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Script started")

# Load RFM data
rfm = pd.read_csv("rfm.csv")

# Set Seaborn style
sns.set(style="whitegrid")

# Plot histograms of Recency, Frequency, and Monetary
plt.figure(figsize=(18, 5))

# Recency
plt.subplot(1, 3, 1)
sns.histplot(rfm['Recency'], bins=30, kde=True, color='skyblue')
plt.title('Recency Distribution')

# Frequency
plt.subplot(1, 3, 2)
sns.histplot(rfm['Frequency'], bins=30, kde=True, color='lightgreen')
plt.title('Frequency Distribution')

# Monetary
plt.subplot(1, 3, 3)
sns.histplot(rfm['Monetary'], bins=30, kde=True, color='salmon')
plt.title('Monetary Distribution')

plt.tight_layout()

# Save the plot
plt.savefig("rfm_distributions.png")

# Show the plot
plt.show()
