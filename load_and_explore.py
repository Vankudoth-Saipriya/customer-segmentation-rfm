import pandas as pd

# Load the Excel file and specific sheet
df = pd.read_csv(r"C:\Users\saipr\OneDrive\Pictures\Desktop\Customer_Segmentation_Project\online_retail_II.csv")

# Show basic info
print("🔹 First 5 rows:")
print(df.head())

print("\n🔹 Info:")
print(df.info())

print("\n🔹 Null values per column:")
print(df.isnull().sum())

# Remove null Customer IDs
df = df[df['Customer ID'].notnull()]

# Remove negative Quantity or Price
df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['Price']

#  Rename for consistency
df.rename(columns={'Customer ID': 'CustomerID', 'Price': 'UnitPrice'}, inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Save cleaned CSV
df.to_csv("online_retail_cleaned.csv", index=False)
print("✅ Cleaned data saved as online_retail_cleaned.csv")






















































