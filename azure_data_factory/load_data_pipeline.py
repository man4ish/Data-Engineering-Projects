# load_data_pipeline.py
import pandas as pd
import sqlite3

def load_to_sqlite(input_file: str, db_file: str):
    df = pd.read_csv(input_file)
    conn = sqlite3.connect(db_file)
    df.to_sql("posts", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Data loaded to {db_file}")

if __name__ == "__main__":
    load_to_sqlite("transformed_data.csv", "posts.db")
