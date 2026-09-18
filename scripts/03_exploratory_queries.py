# =============================================================================
# Migraine Clinical Insights & Operational Burden
# Script Name: 03_exploratory_queries.py
# Author: Rachel Ratajczak
# Dataset: Migraine Dataset (Kaggle)
# https://www.kaggle.com/datasets/ranzeet013/migraine-dataset
# =============================================================================
# Queries the SQLite database to extract clinical insights, such as top triggers, 
# average pain intensity by migraine type, and neurological symptom breakdowns.

import pandas as pd
import _sqlite3

# =============================================================================
# 1. CONNECT TO THE MIGRAINE DATABASE
# =============================================================================

conn = _sqlite3.connect("data/migraine_database.db")

# =============================================================================
# 2. QUERY 1: AVERAGE PAIN INTENSITY AND CASE COUNT BY MIGRAINE TYPE 
# =============================================================================

query_type_summary = """
    SELECT type, COUNT(*) as total_cases, ROUND(AVG(intensity), 2) as avg_intensity
    FROM clinical_encounters
    GROUP BY type
    ORDER BY total_cases DESC;
"""
df_type_summary = pd.read_sql(query_type_summary, conn)

print("--- Migraine Type & Intensity Summary ---")
print(df_type_summary.head())

# Export this summary table for Tableau later
df_type_summary.to_csv("data/tableau_migraine_type_summary.csv", index=False)


# =============================================================================
# 3. CLOSE DATABASE CONNECTION
# =============================================================================

conn.close()
print("\nExploratory queries executed and summary exported successfully!")