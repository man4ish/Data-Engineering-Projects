# Variant Pipeline with PySpark

This project showcases a realistic bioinformatics ETL pipeline built using PySpark. It filters genetic variants based on quality, annotates them with gene and impact data, and generates summary reports for downstream analysis.

## Project Structure
```
bio-variant-pipeline-pyspark/
├── data/
│   ├── variants.csv              # Variant data (VCF-like)
│   └── gene_annotations.csv      # Gene impact annotations
├── output/                       # Processed result files
├── scripts/
│   └──filter_variants.py       # Main PySpark pipeline script
├── README.md
└── requirements.txt
```

## Features

- Load and filter variants based on quality (`QUAL >= 30`) and filter status (`PASS`)
- Join with gene annotations by variant ID
- Generate:
  - Sample-wise variant counts
  - High-impact variant list
  - Gene-wise high-impact variant summaries
- Save output to Parquet and CSV formats

## How to Run

1. Install [PySpark](https://spark.apache.org/docs/latest/api/python/)
   ```bash
   pip install pyspark
   ```
2. Run the pipeline
   ```
   spark-submit scripts/variant_pipeline.py
   ```

## Output
- output/summary_by_sample.parquet

- output/high_impact_variants.csv

- output/high_impact_summary_by_gene.csv


