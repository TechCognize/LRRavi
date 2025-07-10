import pandas as pd
import os

# STEP 1: Load the CSV file
try:
    df = pd.read_csv(r'data/raw/appointments.csv')
    print("✅ Loaded CSV successfully.")
except FileNotFoundError:
    print("❌ File not found: data/raw/appointments.csv")
    exit()

# Show first 5 rows BEFORE cleaning
print("=== BEFORE CLEANING ===")
print(df.head())

# STEP 2: Replace '######' with missing values (NaN)
df.replace("######", pd.NA, inplace=True)

# STEP 3: Clean 'reasons' column
if 'reasons' in df.columns:
    # Ensure it's string type
    df['reasons'] = df['reasons'].astype(str)
    
    # Filter out 'no show' rows
    df = df[~df['reasons'].str.lower().str.contains("no show", na=False)]
else:
    print("⚠️ Warning: 'reasons' column not found.")

# Show first 5 rows AFTER cleaning
print("\n=== AFTER CLEANING ===")
print(df.head())

# Print number of rows after cleaning
print("\n🧹 Number of rows after cleaning:", len(df))

# STEP 4: Save the cleaned CSV
output_path = os.path.join("..", "LEARNERS-REPO", "data", "processed", "appointments_cleaned.csv")
output_dir = os.path.dirname(output_path)
os.makedirs(output_dir, exist_ok=True)  # Make sure directory exists

# Print absolute path for verification
abs_output_path = os.path.abspath(output_path)
print("\n📂 Saving cleaned CSV to:", abs_output_path)

try:
    df.to_csv(output_path, index=False)
    print("✅ Cleaned file saved successfully.")
except Exception as e:
    print("❌ Error saving cleaned file:", e)
    exit()

# STEP 5: Save Markdown Preview to README_output.md
output_md_path = os.path.join("..", "LEARNERS-REPO","README_output.md")
try:
    with open(output_md_path, "w") as f:
        f.write("# Cleaned Appointment Data (Preview)\n\n")
        f.write("Below is a preview of the cleaned data:\n\n")
        f.write(df.head(10).to_markdown(index=False))
    print("✅ Markdown preview saved to:", os.path.abspath(output_md_path))
except Exception as e:
    print("❌ Error saving markdown preview:", e)
