import luigi
import pandas as pd

# Task 1: Load raw data from CSV
class LoadData(luigi.Task):
    input_file = luigi.Parameter(default="data/raw_data.csv")

    def output(self):
        return luigi.LocalTarget("output/processed_data.csv")

    def run(self):
        # Simulate reading data
        df = pd.read_csv(self.input_file)
        df['processed'] = df['value'] * 2  # Some simple processing
        
        # Write output to file
        df.to_csv(self.output().path, index=False)

# Task 2: Summarize processed data
class SummarizeData(luigi.Task):
    input_file = luigi.Parameter(default="output/processed_data.csv")

    def requires(self):
        return LoadData()

    def output(self):
        return luigi.LocalTarget("output/summary.txt")

    def run(self):
        # Simulate summarizing data
        df = pd.read_csv(self.input_file)
        summary = df.describe().to_string()

        with self.output().open('w') as f:
            f.write(summary)

if __name__ == '__main__':
    luigi.run(main_task_cls=SummarizeData)  # Explicitly specify the task to run

