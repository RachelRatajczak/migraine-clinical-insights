# Migraine Clinical Insights & Operational Burden

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)](https://www.sqlite.org/)
[![Tableau](https://img.shields.io/badge/Visualization-Tableau-orange.svg)](https://tableau.com/)

An end-to-end data analytics project exploring a clinical migraine dataset. This project simulates a healthcare analytics workflow—moving from raw data hygiene and relational database ingestion to advanced SQL aggregations and export-ready outputs for visual dashboarding.

## Project Architecture
```text
Migraine_Clinical_Insights/
│
├── data/
│   ├── migraine_data.csv             # Raw source dataset
│   ├── cleaned_migraine_data.csv     # Standardized cleaning output
│   ├── migraine_database.db          # Local SQLite relational database
│   ├── tableau_migraine_type_summary.csv # Pre-aggregated SQL export for Tableau
│   └── tableau_age_summary.csv       # Pre-aggregated SQL export for Tableau
│
├── scripts/
│   ├── 01_data_cleaning.py           # Python data hygiene & standardization
│   ├── 02_sql_ingestion.py           # SQLite relational table load & verification
│   └── 03_exploratory_queries.py     # SQL analysis & metric aggregation
│
└── README.md
```

##  Technical Stack & Skills Demonstrated
* **Python (pandas):** Automated data cleaning, schema normalization, missing value handling, and duplicate management.
* **SQL (SQLite):** Relational database ingestion (`to_sql`), table creation, and analytical querying using `GROUP BY`, `CASE` conditional bucketing, and aggregate functions (`AVG`, `COUNT`, `ROUND`).
* **Tableau Prep Workflow:** Exporting clean, pre-aggregated relational tables (`.csv`) optimized for clean dashboard performance.

##  Key Analytical Highlights
1. **Clinical Data Hygiene:** Standardized raw clinical strings (lowercase, stripped spaces, underscore notation) and resolved structural anomalies to ensure data integrity.
2. **Relational Ingestion:** Built a repeatable data pipeline piping pandas DataFrames directly into a local SQLite instance (`clinical_encounters` table).
3. **Advanced SQL Aggregations:** 
   * Calculated case volume and average pain intensity broken down by clinical migraine type.
   * Utilized conditional `CASE` statements to segment patient demographics into age brackets (`18-29`, `30-44`, etc.) while filtering out null values to assess severity trends safely.

##  How to Run the Project
1. Clone the repository and navigate into the project directory.
2. Set up and activate your Python virtual environment.
3. Install dependencies:
   ```bash
   pip install pandas sqlite3

4. Run the pipeline scripts sequentially:
    ```
   python scripts/01_data_cleaning.py
   python scripts/02_sql_ingestion.py
   python scripts/03_exploratory_queries.py