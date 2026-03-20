import pandas as pd

print("----- TASK 1 : DATA IMMERSION & WRANGLING -----")

# Load data
df = pd.read_csv("raw_sales_data.csv")

print("\n1. RAW DATA INFO")
print(df.info())

print("\n2. MISSING VALUES")
print(df.isnull().sum())

print("\n3. DUPLICATES")
print("Duplicate Rows:", df.duplicated().sum())

# Cleaning
df = df.drop_duplicates()
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df['Profit'] = df['Profit'].fillna(0)
df['Category'] = df['Category'].str.lower()

df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month

# Outlier treatment
Q1 = df['Profit'].quantile(0.25)
Q3 = df['Profit'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Profit'] >= Q1-1.5*IQR) &
        (df['Profit'] <= Q3+1.5*IQR)]

# Save cleaned file
df.to_csv("cleaned_sales_data.csv", index=False)

print("\n4. AFTER CLEANING SHAPE:", df.shape)

print("\n5. CLEANED DATA SAMPLE")
print(df.head())

print("\nTASK-1 COMPLETED SUCCESSFULLY")
