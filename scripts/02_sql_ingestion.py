# =============================================================================
# Migraine Clinical Insights & Operational Burden
# Script Name: 02_sql_ingestion.py
# Author: Rachel Ratajczak
# Dataset: Migraine Dataset (Kaggle)
# https://www.kaggle.com/datasets/ranzeet013/migraine-dataset
# =============================================================================
# Loads the cleaned migraine dataset into a local SQLite database 
# to enable SQL-based clinical querying and analysis.

import pandas as pd
import sqlite3

# =============================================================================
# 1. LOAD CLEANED DATASET
# =============================================================================

file_path = "data/cleaned_migraine_data.csv"
df = pd.read_csv(file_path)
# print(df)
print(f"Loaded {len(df)} rows for SQL ingestion.")

# =============================================================================
# 2. CREATE A LOCAL SQLite DATABASE CONNECTION
# =============================================================================

conn = sqlite3.connect("data/migraine_database.db")
cursor = conn.cursor()

# =============================================================================
# 3. WRITE DATAFRAME TO SQL TABLE CALLED 'clinical_encounters'
# =============================================================================

table_name = "clinical_encounters"
df.to_sql(table_name, conn, if_exists="replace", index=False)
print(f"Successfully loaded data into SQLite table: '{table_name}'")

# =============================================================================
# 4. VERIFY CONNECTION WITH SQL QUERY
# =============================================================================

query = "SELECT COUNT(*) FROM clinical_encounters;"
result = pd.read_sql(query, conn)
print(f"Verification query result (Total Rows in SQL): {result.iloc[0,0]}") #integer location - grab raw count instead of table structure 

# =============================================================================
# 5. CLOSE CONNECTION
# =============================================================================
conn.close()