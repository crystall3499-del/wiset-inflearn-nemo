import sqlite3
import pandas as pd
import json
import os

def extract_data():
    db_path = 'data/nemo_data.db'
    if not os.path.exists(db_path):
        print(f"Error: {db_path} not found")
        return

    conn = sqlite3.connect(db_path)
    
    # Get table names
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables: {tables}")

    # Assume there's an 'articles' table based on previous EDA report context
    table_name = tables[0][0] if tables else 'articles'
    
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()

    # Basic stats
    stats = {
        "total_count": len(df),
        "avg_deposit": float(df['firstDeposit'].mean()) if 'firstDeposit' in df else 0,
        "avg_rent": float(df['firstMonthlyRent'].mean()) if 'firstMonthlyRent' in df else 0,
        "avg_size": float(df['size'].mean()) if 'size' in df else 0,
    }

    # Distribution of article types
    if 'businessLargeCodeName' in df:
        type_dist = df['businessLargeCodeName'].value_counts().to_dict()
    else:
        type_dist = {}

    # Monthly rent distribution for histogram
    if 'firstMonthlyRent' in df:
        rent_bins = pd.cut(df['firstMonthlyRent'], bins=10).value_counts().sort_index()
        rent_dist = {str(k): int(v) for k, v in rent_bins.items()}
    else:
        rent_dist = {}

    # Top locations (nearSubwayStation)
    if 'nearSubwayStation' in df:
        top_locations = df['nearSubwayStation'].value_counts().head(10).to_dict()
    else:
        top_locations = {}

    # Size vs Rent correlation
    if 'size' in df and 'firstMonthlyRent' in df:
        corr_data = df[['size', 'firstMonthlyRent']].dropna().head(100).to_dict(orient='records')
    else:
        corr_data = []

    # Combine all
    dashboard_data = {
        "stats": stats,
        "type_dist": type_dist,
        "rent_dist": rent_dist,
        "top_locations": top_locations,
        "corr_data": corr_data
    }

    with open('data/dashboard_data.json', 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, ensure_ascii=False, indent=2)
    
    print("Data extracted to data/dashboard_data.json")

if __name__ == "__main__":
    extract_data()
