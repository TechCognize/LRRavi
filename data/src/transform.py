import pandas as pd
import os
import sys

# Redirect stdout to readme file
sys.stdout = open('README.md', 'w', encoding='utf-8')

# Step 1: Load the data
df = pd.read_csv(r'data/raw/your_file.csv')
print("# 🚀 Data Cleaning Report\n")

print("## ✅ Before Cleaning")
print("**Total rows:**", len(df), "\n")

print("### Sample rows:")
print(df.head(), "\n")

print("### Missing values:")
print(df.isnull().sum(), "\n")

print("### Any duplicates?")
print(df.duplicated().any(), "\n")

# Step 2: Apply cleaning transformations
df = df.drop_duplicates()  # Remove duplicate rows
df.columns = df.columns.str.lower()  # Convert column names to lowercase
df = df[df[df.columns[0]] != ""]  # Remove rows where first column is empty
df = df.reset_index(drop=True)  # Reset index
df = df.dropna()  # Remove missing values again

# Step 3: Validations
print("## ✅ After Cleaning")
print("**Total rows:**", len(df), "\n")

print("### First 5 rows:")
print(df.head(), "\n")

print("### Missing values remaining:")
print(df.isnull().sum(), "\n")

print("### Any duplicates?")
print(df.duplicated().any(), "\n")

print("### Data types:")
print(df.dtypes, "\n")

print(f"### Unique values in '{df.columns[0]}':", df[df.columns[0]].nunique(), "\n")

print("### Summary Statistics:")
print(df.describe(include='all'), "\n")

# Step 4: Save cleaned data
os.makedirs(r'data/processed', exist_ok=True)
df.to_csv(r'data/processed/cleaned_file.csv', index=False)

print("✅ Cleaned data saved to `data/processed/cleaned_file.csv`")

# Close redirection
sys.stdout.close()
