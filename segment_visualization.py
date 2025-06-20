import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load final RFM data
rfm = pd.read_csv("rfm_final.csv")

# Plot segment distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=rfm, x='Segment', palette='Set2')
plt.title('Customer Segment Counts')
plt.xlabel('Segment')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.savefig("segment_counts.png")
plt.show()
