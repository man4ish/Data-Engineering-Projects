"""
databricks_data_processing.py

This script demonstrates a basic data processing workflow using PySpark on Databricks.
It includes:

1. Reading a CSV file into a Spark DataFrame.
2. Filtering rows based on a condition.
3. Displaying the filtered results.

Replace `'sample.csv'` with the actual path to your file, which can be a DBFS path like `/dbfs/FileStore/sample.csv`.

Author:
    Manish Kumar
"""

from pyspark.sql import SparkSession

# Step 1: Initialize Spark session
spark = SparkSession.builder.appName('Databricks Data Processing').getOrCreate()

# Step 2: Load data from CSV
# If using DBFS in Databricks, use a path like 'sample.csv'
df = spark.read.csv('path_to_data.csv', header=True, inferSchema=True)

# Optional: Show schema and preview raw data
df.printSchema()
df.show(5)

# Step 3: Perform basic filtering (e.g., filter rows where 'column_name' > 0)
df_filtered = df.filter(df['column_name'] > 0)

# Step 4: Show filtered data
df_filtered.show(10)
