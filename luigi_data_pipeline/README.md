# Luigi Data Pipeline

This repository showcases a simple **Luigi** data pipeline that processes raw CSV data, applies basic transformations, and generates a summary.

## Project Structure

- **data/**: Contains the raw data file (`raw_data.csv`).
- **output/**: Contains the output from the pipeline (processed data and summary).
- **scripts/**: Contains the main Luigi pipeline script (`pipeline.py`).
- **requirements.txt**: Lists Python dependencies.

## Tasks

- **LoadData**: Reads raw data from `data/raw_data.csv`, processes it (multiplying the `value` column by 2), and saves it to `output/processed_data.csv`.
- **SummarizeData**: Summarizes the processed data and writes it to `output/summary.txt`.

## How to Run the Pipeline

1. Clone the repository.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Luigi pipeline:
   ```bash
   python scripts/pipeline.py --local-scheduler 
   ```

## BOutput
- processed_data.csv: Contains the processed data.

- summary.txt: Contains a summary of the processed data.
