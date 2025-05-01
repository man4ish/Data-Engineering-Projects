# variant_pipeline.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Bioinformatics Variant Pipeline") \
    .getOrCreate()

# Load variant data
variants = spark.read.csv("data/variants.csv", header=True, inferSchema=True)

# Load gene annotation data
annotations = spark.read.csv("data/gene_annotations.csv", header=True, inferSchema=True)

# Step 1: Filter variants by quality and pass filter
filtered_variants = variants.filter((col("QUAL") >= 30) & (col("FILTER") == "PASS"))

# Step 2: Join with gene annotation
annotated_variants = filtered_variants.join(annotations, on="ID", how="left")

# Step 3: Summarize variant counts per sample
summary_by_sample = annotated_variants.groupBy("SAMPLE_ID").agg(count("ID").alias("Variant_Count"))

# Step 4: Extract and save high-impact variants
high_impact_variants = annotated_variants.filter(col("Impact") == "HIGH")

# Step 5: Summarize high-impact variant counts per gene
summary_by_gene = high_impact_variants.groupBy("Gene").agg(count("ID").alias("High_Impact_Variant_Count"))

# Save outputs
summary_by_sample.write.mode("overwrite").parquet("output/summary_by_sample.parquet")
high_impact_variants.write.mode("overwrite").csv("output/high_impact_variants.csv", header=True)
summary_by_gene.write.mode("overwrite").csv("output/high_impact_summary_by_gene.csv", header=True)

print("Pipeline execution complete. Output saved to 'output/' folder.")

# Stop Spark session
spark.stop()

