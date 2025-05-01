"""
luigi_pipeline.py

This module defines a two-step Luigi pipeline for basic data processing.

Tasks:
    1. LoadData: Reads a date-partitioned CSV file from the `data/` directory,
       performs a simple transformation (doubling the 'value' column), and writes
       the processed data to the `output/` directory.

    2. SummarizeData: Depends on LoadData. It generates a statistical summary
       (mean, std, etc.) of the processed data and saves the summary as a text
       file in the `output/` directory.

Features:
    - Uses Luigi for dependency management and workflow orchestration.
    - Accepts a `--process-date` parameter to manage daily data partitions.
    - Includes error handling and logging for traceability.
    - Supports reproducible and modular data processing tasks.

Usage:
    Run this module using the Luigi CLI:

        python luigi_pipeline.py SummarizeData --process-date 2023-12-15 --local-scheduler

Requirements:
    - pandas
    - luigi
    - A raw input file at `data/raw_data_<YYYY-MM-DD>.csv` with a 'value' column.

Author:
    Manish Kuma
"""

import luigi
import pandas as pd
import logging
import os
from datetime import date

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('luigi-interface')

# Task 1: Load raw data from CSV and process it
class LoadData(luigi.Task):
    process_date = luigi.DateParameter(default=date.today())

    def requires(self):
        return None

    def input_file_path(self):
        return f"data/raw_data_{self.process_date}.csv"

    def output(self):
        return luigi.LocalTarget(f"output/processed_data_{self.process_date}.csv")

    def run(self):
        try:
            logger.info(f"Reading raw data for date: {self.process_date}")
            df = pd.read_csv(self.input_file_path())

            if 'value' not in df.columns:
                raise ValueError("Column 'value' not found in input file")

            df['processed'] = df['value'] * 2  # Simulated processing

            os.makedirs(os.path.dirname(self.output().path), exist_ok=True)
            df.to_csv(self.output().path, index=False)
            logger.info(f"Processed data saved to {self.output().path}")
        except Exception as e:
            logger.error(f"Error in LoadData: {e}")
            raise

# Task 2: Summarize the processed data
class SummarizeData(luigi.Task):
    process_date = luigi.DateParameter(default=date.today())

    def requires(self):
        return LoadData(process_date=self.process_date)

    def output(self):
        return luigi.LocalTarget(f"output/summary_{self.process_date}.txt")

    def run(self):
        try:
            input_path = self.input().path
            logger.info(f"Reading processed data from: {input_path}")
            df = pd.read_csv(input_path)

            summary = df.describe().to_string()
            os.makedirs(os.path.dirname(self.output().path), exist_ok=True)
            with self.output().open('w') as f:
                f.write(summary)

            logger.info(f"Summary written to {self.output().path}")
        except Exception as e:
            logger.error(f"Error in SummarizeData: {e}")
            raise

if __name__ == '__main__':
    luigi.run()
