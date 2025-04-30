# transform_data_pipeline.py
import pandas as pd

def transform_data(input_file: str, output_file: str):
    df = pd.read_csv(input_file)
    df['title_length'] = df['title'].apply(lambda x: len(x))
    df.to_csv(output_file, index=False)
    print(f"Transformed data saved to {output_file}")

if __name__ == "__main__":
    transform_data("sample_data.csv", "transformed_data.csv")
