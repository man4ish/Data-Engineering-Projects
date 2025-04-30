from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Databricks Data Processing').getOrCreate()

# Load data
df = spark.read.csv('path_to_data.csv', header=True, inferSchema=True)

# Perform basic data processing
df_filtered = df.filter(df['column_name'] > 0)
df_filtered.show()

