import pandas as pd

# Load clustered data
rfm = pd.read_csv("rfm.csv")

# Map cluster number to readable labels (adjust if needed)
label_map = {
    0: "Inactive",
    1: "Regular",
    2: "Loyal",
    3: "Premium"
}
rfm["Segment"] = rfm["Cluster"].map(label_map)

# Save the final labeled dataset
rfm.to_csv("rfm_final.csv", index=False)

# Optional: Summary output
summary = rfm.groupby("Segment").agg({
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": ["mean", "count"]
}).round(2)

print("✅ Cluster labeling completed. Final summary:\n")
print(summary)
