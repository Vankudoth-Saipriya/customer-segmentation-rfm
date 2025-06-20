import pandas as pd

# Step 1: Load cleaned data
df = pd.read_csv("online_retail_cleaned.csv")

# Step 2: Convert InvoiceDate to datetime (in case it's read as object)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Step 3: Set snapshot date (day after the last transaction)
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Step 4: Group by CustomerID and calculate RFM
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,   # Recency
    'Invoice': 'nunique',                                      # Frequency
    'TotalPrice': 'sum'                                        # Monetary
}).reset_index()

# Step 5: Rename columns
rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'Invoice': 'Frequency',
    'TotalPrice': 'Monetary'
}, inplace=True)

# Step 6: Save to CSV
rfm.to_csv("rfm.csv", index=False)

# Step 7: Display the first few rows
print("✅ RFM Metrics:")
print(rfm.head())
