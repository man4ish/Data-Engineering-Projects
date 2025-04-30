# ingest_data_pipeline.py
import requests
import json
import pandas as pd

def download_sample_data(url: str, output_file: str):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False)
        print(f"Data downloaded and saved to {output_file}")
    else:
        print("Failed to download data")

if __name__ == "__main__":
    sample_url = "https://jsonplaceholder.typicode.com/posts"
    output_path = "sample_data.csv"
    download_sample_data(sample_url, output_path)
