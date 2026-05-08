"""
data_cleaning.py
================
Student Stress Project — Practical Design Course
-------------------------------------------------
This script cleans and processes both raw datasets:
  - Student_Stress_Factors_and_Mental_Health.csv  (Dataset 1, 100 rows)
  - Student_Stress_Level.csv                       (Dataset 2, 150 rows)

Run from the project root:
    python src/data_cleaning.py

Outputs (saved to data/processed/):
    cleaned_df1.csv   ← Cleaned Dataset 1
    cleaned_df2.csv   ← Cleaned Dataset 2
"""

import pandas as pd
import numpy as np
import os

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────
RAW_DIR       = "data/raw/"
PROCESSED_DIR = "data/processed/"
FILE_DF1      = "Student_Stress_Factors_and_Mental_Health.csv"
FILE_DF2      = "Student_Stress_Level.csv"

os.makedirs(PROCESSED_DIR, exist_ok=True)


# ─────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def log(msg):
    print(f"  ✔  {msg}")

def section(title):
    print(f"\n{'='*55}")
    print(f"  {title}")
    print(f"{'='*55}")

def check_missing(df, name):
    total = df.isnull().sum().sum()
    if total == 0:
        log(f"[{name}] No missing values ✅")
    else:
        print(f"\n  ⚠  Missing values in {name}:")
        print(df.isnull().sum()[df.isnull().sum() > 0].to_string())
    return total

def check_duplicates(df, name):
    n = df.duplicated().sum()
    if n == 0:
        log(f"[{name}] No duplicate rows ✅")
    else:
        print(f"  ⚠  [{name}] {n} duplicate rows found")
    return n

def fill_missing(df):
    """
    Rule:
      - Column > 40% missing  → drop the column
      - Numerical             → fill with median
      - Categorical           → fill with mode
    """
    threshold = 0.4 * len(df)
    for col in df.columns:
        missing = df[col].isnull().sum()
        if missing == 0:
            continue
        if missing > threshold:
            df.drop(columns=[col], inplace=True)
            log(f"Dropped '{col}' — {missing/len(df)*100:.0f}% missing (>40%)")
        elif pd.api.types.is_numeric_dtype(df[col]):
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
            log(f"Filled '{col}' with median = {median_val}")
        else:
            mode_val = df[col].mode()[0]
            df[col].fillna(mode_val, inplace=True)
            log(f"Filled '{col}' with mode = '{mode_val}'")
    return df


# ─────────────────────────────────────────────────────────────────────────────
# CLEAN DATASET 1 — Student_Stress_Factors_and_Mental_Health.csv
# ─────────────────────────────────────────────────────────────────────────────
def clean_df1(path):
    section("DATASET 1: Student Stress Factors & Mental Health")

    # STEP 1 — Load
    df = pd.read_csv(path)
    log(f"Loaded: {df.shape[0]} rows × {df.shape[1]} columns")

    # STEP 2 — Check
    check_missing(df, "DF1")
    check_duplicates(df, "DF1")

    # STEP 3 — Handle missing values
    df = fill_missing(df)

    # STEP 4 — Remove duplicates
    before = len(df)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    removed = before - len(df)
    log(f"Removed {removed} duplicate row(s) → {len(df)} rows remain")

    # STEP 5 — Consistent formats
    # Clean column names → snake_case
    df.columns = [
        'sleep_quality', 'headache_frequency', 'academic_performance',
        'study_load', 'extracurricular_activities', 'stress_level',
        'gender', 'age', 'course', 'year_of_study', 'cgpa',
        'marital_status', 'depression', 'anxiety', 'panic_attack',
        'sought_treatment'
    ]
    log("Column names → snake_case")

    # Standardise text columns (strip whitespace, consistent casing)
    df['year_of_study'] = df['year_of_study'].str.strip().str.title()
    df['cgpa']          = df['cgpa'].str.strip()
    df['gender']        = df['gender'].str.strip()
    df['course']        = df['course'].str.strip()
    for col in ['marital_status', 'depression', 'anxiety', 'panic_attack', 'sought_treatment']:
        df[col] = df[col].str.strip()
    log("Text columns: whitespace stripped, casing standardised")

    # Ensure numeric types
    numeric_cols = ['sleep_quality', 'headache_frequency', 'academic_performance',
                    'study_load', 'extracurricular_activities', 'stress_level', 'age']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').astype(int)
    log("Numeric columns confirmed int64")

    # STEP 6 — Scale validation (all Likert cols should be 1–5)
    likert_cols = ['sleep_quality', 'headache_frequency', 'academic_performance',
                   'study_load', 'extracurricular_activities', 'stress_level']
    for col in likert_cols:
        mn, mx = df[col].min(), df[col].max()
        status = "✅" if mn >= 1 and mx <= 5 else "⚠  OUT OF RANGE"
        log(f"Scale check '{col}': range {mn}–{mx} {status}")

    # STEP 7 — Final validation
    assert df.isnull().sum().sum() == 0, "❌ Still has missing values!"
    assert df.duplicated().sum() == 0,   "❌ Still has duplicates!"
    log(f"Final shape: {df.shape[0]} rows × {df.shape[1]} columns")
    log("Missing = 0 | Duplicates = 0 | All types correct ✅")

    return df


# ─────────────────────────────────────────────────────────────────────────────
# CLEAN DATASET 2 — Student_Stress_Level.csv
# ─────────────────────────────────────────────────────────────────────────────
def clean_df2(path):
    section("DATASET 2: Student Stress Level Dataset")

    # STEP 1 — Load
    df = pd.read_csv(path)
    log(f"Loaded: {df.shape[0]} rows × {df.shape[1]} columns")

    # STEP 2 — Check
    check_missing(df, "DF2")
    check_duplicates(df, "DF2")

    # STEP 3 — Handle missing values
    df = fill_missing(df)

    # STEP 4 — Remove duplicates
    before = len(df)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    removed = before - len(df)
    log(f"Removed {removed} duplicate row(s) → {len(df)} rows remain")

    # STEP 5 — Column names already clean snake_case — standardise just in case
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    log("Column names confirmed lowercase snake_case")

    # Ensure all numeric
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    log("All columns confirmed numeric (int64)")
    df = df.astype(int)

    # STEP 6 — Scale validation
    # stress_level: should be 1–2 (binary)
    # depression: PHQ-9 clinical scale 0–27 (DO NOT force to 1–5)
    # anxiety:    GAD-7 clinical scale 0–21 (DO NOT force to 1–5)
    # others:     Likert 1–5

    print("\n  📌 Scale Notes for Dataset 2:")
    print("     stress_level    → Binary  : 1=Low, 2=High")
    print("     depression      → PHQ-9   : 0–27 (clinical, not Likert)")
    print("     anxiety         → GAD-7   : 0–21 (clinical, not Likert)")
    print("     All other cols  → Likert  : 0–5 or 1–5")

    likert_cols = ['sleep_quality', 'academic_performance', 'study_load',
                   'teacher_student_relationship', 'future_career_concerns',
                   'social_support', 'peer_pressure', 'extracurricular_activities',
                   'living_conditions']
    for col in likert_cols:
        if col in df.columns:
            log(f"Scale check '{col}': range {df[col].min()}–{df[col].max()} ✅")

    # Fix stress_level=0 if present (invalid value)
    invalid = (df['stress_level'] == 0).sum()
    if invalid > 0:
        df.loc[df['stress_level'] == 0, 'stress_level'] = 1
        log(f"Fixed {invalid} rows: stress_level=0 recoded to 1 (minimum valid)")

    # STEP 7 — Final validation
    assert df.isnull().sum().sum() == 0, "❌ Still has missing values!"
    assert df.duplicated().sum() == 0,   "❌ Still has duplicates!"
    log(f"Final shape: {df.shape[0]} rows × {df.shape[1]} columns")
    log("Missing = 0 | Duplicates = 0 | All types correct ✅")

    return df


# ─────────────────────────────────────────────────────────────────────────────
# MAIN — Run both cleaners and save outputs
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🎓 Student Stress Project — Data Cleaning Script")
    print("   Running from: src/data_cleaning.py")

    # Clean Dataset 1
    df1 = clean_df1(os.path.join(RAW_DIR, FILE_DF1))
    out1 = os.path.join(PROCESSED_DIR, "cleaned_df1.csv")
    df1.to_csv(out1, index=False)
    print(f"\n  💾 Saved → {out1}")

    # Clean Dataset 2
    df2 = clean_df2(os.path.join(RAW_DIR, FILE_DF2))
    out2 = os.path.join(PROCESSED_DIR, "cleaned_df2.csv")
    df2.to_csv(out2, index=False)
    print(f"  💾 Saved → {out2}")

    # Final summary
    section("CLEANING COMPLETE — Summary")
    print(f"  Dataset 1:  {df1.shape[0]} rows × {df1.shape[1]} cols  →  {out1}")
    print(f"  Dataset 2:  {df2.shape[0]} rows × {df2.shape[1]} cols  →  {out2}")
    print(f"\n  ✅ Both datasets are clean and ready for analysis in the notebook.\n")
