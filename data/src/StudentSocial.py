import pandas as pd
import numpy as np
import os

# ✅ Step 1: Load raw CSV
file_path = r"C:\Users\ravi\final\Learners-Repo\data\raw\Students Social Media Addiction.csv"
df = pd.read_csv(file_path)

# ✅ Step 2: Clean and transform
df['Conflicts_Over_Social_Media'] = df['Conflicts_Over_Social_Media'].replace(0, np.nan)
df_cleaned = df.dropna(subset=['Conflicts_Over_Social_Media', 'Sleep_Hours_Per_Night'])
df_cleaned = df_cleaned[(df_cleaned['Age'] >= 15) & (df_cleaned['Age'] <= 30)]
df_cleaned = df_cleaned[df_cleaned['Avg_Daily_Usage_Hours'] <= 24]
df_cleaned['Addiction_Level'] = pd.cut(
    df_cleaned['Addicted_Score'],
    bins=[-1, 3, 6, 10],
    labels=['Low', 'Moderate', 'High']
)

# ✅ Step 3: Save cleaned CSV
processed_path = r"C:\Users\ravi\final\Learners-Repo\data\processed\cleaned_social_media.csv"
os.makedirs(os.path.dirname(processed_path), exist_ok=True)
df_cleaned.to_csv(processed_path, index=False)

print("✅ Cleaned data saved to:", processed_path)

# ✅ Step 4: Generate README.md (AFTER df and df_cleaned are defined)
readme_path = r"C:\Users\ravi\final\Learners-Repo\README.md"

before_rows = df.shape[0]
after_rows = df_cleaned.shape[0]
before_sample = df.head().to_markdown(index=False)
after_sample = df_cleaned.head().to_markdown(index=False)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write("# 📊 Students Social Media Addiction - Data Cleaning Report\n\n")
    f.write(f"**Total Rows Before Cleaning:** {before_rows}\n\n")
    f.write("### 🔍 Sample Data Before Cleaning:\n")
    f.write(f"{before_sample}\n\n")
    f.write(f"**Total Rows After Cleaning:** {after_rows}\n\n")
    f.write("### ✅ Sample Data After Cleaning:\n")
    f.write(f"{after_sample}\n\n")
    f.write("### 🔧 Transformations Applied:\n")
    f.write("- Replaced `0` in `Conflicts_Over_Social_Media` with null (NaN)\n")
    f.write("- Dropped rows with missing values in key columns\n")
    f.write("- Filtered rows with age between 15 and 30\n")
    f.write("- Removed entries with usage > 24 hours/day\n")
    f.write("- Added new column `Addiction_Level` based on `Addicted_Score`\n")

print("✅ README.md generated at:", readme_path)
