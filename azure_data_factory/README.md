# Azure Data Factory Python Simulation

This repository simulates a simplified Azure Data Factory (ADF) pipeline using Python. It demonstrates an ETL (Extract, Transform, Load) process:

## Folder Structure
```
azure_data_factory_demo/
├── ingest_data_pipeline.py     # Downloads and stores raw data
├── transform_data_pipeline.py  # Applies transformations to raw data
├── load_data_pipeline.py       # Loads transformed data into SQLite DB
├── README.md                   # Project description
```

## Description
This Python project mimics the behavior of ADF with three scripts:
1. **ingest_data_pipeline.py** - Downloads JSON data from a public API and saves it as a CSV.
2. **transform_data_pipeline.py** - Adds a new column based on existing data.
3. **load_data_pipeline.py** - Loads the transformed CSV into a local SQLite database.

## How to Run
1. Clone the repo
```bash
git clone https://github.com/yourusername/azure_data_factory_demo.git
cd azure_data_factory_demo
```

2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt  # Optional if you split dependencies
```

3. Run the pipeline step-by-step
```bash
python ingest_data_pipeline.py
python transform_data_pipeline.py
python load_data_pipeline.py
```

## Showcasing ADF Skills
Each script can be imagined as an activity in a pipeline within Azure Data Factory. This project structure shows how to modularize and chain ETL processes.

