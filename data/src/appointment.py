import pandas as pd
import os

# STEP 1: Load the CSV file
input_path = os.path.join("data", "raw", "appointments.csv")
try:
    df = pd.read_csv(input_path)
    print("✅ Loaded CSV successfully from:", os.path.abspath(input_path))
except FileNotFoundError:
    print("❌ File not found:", os.path.abspath(input_path))
    exit()

# Save a copy of the original (for README preview)
df_before = df.copy()

# STEP 2: Replace '######' with missing values (NaN)
df.replace("######", pd.NA, inplace=True)

# STEP 3: Clean 'reasons' column
if 'reasons' in df.columns:
    df['reasons'] = df['reasons'].astype(str)
    df = df[~df['reasons'].str.lower().str.contains("no show", na=False)]
else:
    print("⚠️ Warning: 'reasons' column not found.")

# STEP 4: Print for debugging
print("\n=== BEFORE CLEANING ===")
print(df_before.head())

print("\n=== AFTER CLEANING ===")
print(df.head())

print("\n🧹 Number of rows after cleaning:", len(df))

# STEP 5: Save the cleaned CSV
output_csv_path = os.path.join("..", "LEARNERS-REPO", "data", "processed", "appointments_cleaned.csv")
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

try:
    df.to_csv(output_csv_path, index=False)
    print("✅ Cleaned CSV saved at:", os.path.abspath(output_csv_path))
except Exception as e:
    print("❌ Error saving CSV:", e)
    exit()

# # STEP 6: Save both before and after previews to README_output.md
output_md_path = os.path.join("..", "LEARNERS-REPO", "README_output.md")
try:
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write("# Cleaned Appointment Data Report\n\n")

        f.write("## 📋 Preview Before Cleaning:\n\n")
        f.write(df_before.head(10).to_markdown(index=False))
        f.write("\n\n---\n\n")

        f.write("## 🧹 Preview After Cleaning:\n\n")
        f.write(df.head(10).to_markdown(index=False))

    print("✅ README_output.md written at:", os.path.abspath(output_md_path))
except Exception as e:
    print("❌ Error saving README markdown file:", e)

