# =============================================================================
# Migraine Clinical Insights & Operational Burden
# Script Name: 01_data_cleaning.py
# Author: Rachel Ratajczak
# Dataset: Migraine Dataset (Kaggle)
# https://www.kaggle.com/datasets/ranzeet013/migraine-dataset
# =============================================================================
# This script performs initial data hygiene on raw clinical migraine data. 
# It standardizes column names, removes duplicate entries, handles missing values, 
# and exports a clean dataset ready for SQL and Tableau visualization.

# Inputs:
#   - ../data/migraine_data.csv
# Outputs:
#    - ../data/cleaned_migraine_data.csv
# =============================================================================

import pandas as pd

# =============================================================================
# 1. LOAD DATA
# =============================================================================
# Download from Kaggle:
# https://www.kaggle.com/datasets/ranzeet013/migraine-dataset

file_path = "data/migraine_data.csv"
df = pd.read_csv(file_path)

#print(df)
print(f"\nOriginal row count: {len(df)}")

# =============================================================================
# 2. FORMAT COLUMNS
# =============================================================================

#print(df.columns)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
column_list = df.columns.tolist()
print("\n--- Cleaned Column Names ---")
print(column_list)

# =============================================================================
# 3. HANDLE MISSING VALUES AND DUPLICATES
# =============================================================================

missing_counts = df.isnull().sum()
print("Missing values per column:")
print(missing_counts)

duplicate_count = df.duplicated().sum()
print(f"Total duplicate rows: {duplicate_count}")
duplicate_rows = df[df.duplicated()]
print("Duplicate Rows:")
print(duplicate_rows)
df = df.drop_duplicates()
print(f"\nRow count without duplicates: {len(df)}")

# =============================================================================
# 4. EXPORT CLEANED DATA
# =============================================================================

output_path = "data/cleaned_migraine_data.csv"
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset saved successfully to {output_path}")