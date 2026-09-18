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

print("\n--- Migraine Type & Intensity Summary ---")
print(df_type_summary.head())

# Export this summary table for Tableau later
df_type_summary.to_csv("data/tableau_migraine_type_summary.csv", index=False)

# =============================================================================
# 2. QUERY 2: AGE-SEVERITY RELATIONSHIP
# =============================================================================

query_age_intensity = """
    SELECT 
    CASE 
        WHEN age BETWEEN 18 AND 29 THEN '18-29'
        WHEN age BETWEEN 30 AND 44 THEN '30-44'
        WHEN age BETWEEN 45 AND 59 THEN '45-59'
        ELSE '60+'
    END as age_group,
    ROUND(AVG(intensity), 2) as avg_intensity
    FROM clinical_encounters
    WHERE age IS NOT NULL
    GROUP BY age_group
    ORDER BY age_group;
"""

df__age_intensity = pd.read_sql(query_age_intensity, conn)

print("\n--- Age & Intensity ---")
print(df__age_intensity.head())

# Export this summary table for Tableau later
df__age_intensity.to_csv("data/tableau_age_intensity.csv", index=False)

# =============================================================================
# 2. QUERY 3: MULTI-SYMPTOM IN SEVERE CASES
# =============================================================================

query_multi_symptoms = """

"""

# =============================================================================
# 2. QUERY 4: DURATION BY MIGRAINE TYPE
# =============================================================================

query_duration = """

"""

# =============================================================================
# 3. CLOSE DATABASE CONNECTION
# =============================================================================

conn.close()
print("\nExploratory queries executed and summary exported successfully!")