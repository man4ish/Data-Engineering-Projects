# RNA-Seq Pipeline with Apache Airflow
This repository contains an RNA-Seq analysis pipeline designed to run through Apache Airflow. The pipeline processes raw sequencing data (FASTQ files) and performs essential steps like trimming, alignment, and quantification. The final output is uploaded to AWS S3 for further analysis.

## Table of Contents

- Introduction

- Pipeline Overview

- Setup and Installation

- Configuration

- Running the Pipeline

- CI/CD Pipeline

- Output Files



## Introduction
This repository automates the RNA-Seq analysis pipeline using Apache Airflow. The pipeline supports the following steps:

- Downloading raw FASTQ files from S3.

- Trimming raw reads (adapter and low-quality bases).

- Running Kallisto for transcript quantification.

- Running STAR for alignment.

- Sorting and indexing the BAM files.

- Generating a summary report.

- Uploading output files to S3.

## Tools Used
- Apache Airflow: To manage and schedule pipeline tasks.

- Kallisto: For transcript quantification.

- STAR: For RNA-Seq alignment.

- Samtools: For sorting and indexing BAM files.

- AWS CLI: For interacting with S3 buckets.

## Pipeline Overview
The pipeline is designed to work as an Airflow Directed Acyclic Graph (DAG), where each task corresponds to a step in the RNA-Seq analysis workflow. The tasks are organized in such a way that they can run independently or in sequence, based on their dependencies.

### Steps in the Pipeline:
- Download from S3: Downloads raw FASTQ files.

- Trim Reads: Trims adapters and low-quality sequences from the raw reads.

- Run Kallisto: Performs transcript quantification.

- Run STAR: Aligns reads to a reference genome.

- Sort and Index BAM: Sorts the resulting BAM files and indexes them for downstream analysis.

- Generate Summary: Generates a summary of the analysis results.

- Upload to S3: Uploads the processed files and summary reports to an S3 bucket.

## Setup and Installation

### Requirements

- Python 3.7+

- Apache Airflow 2.0 or above

- AWS CLI (for interacting with S3)

- Kallisto (for transcript quantification)

- STAR (for RNA-Seq alignment)

- Samtools (for BAM file manipulation)

### Install Dependencies
Clone the repository and install the necessary dependencies.

```
git clone https://github.com/yourusername/rnaseq-pipeline.git
cd rnaseq-pipeline
pip install -r requirements.txt
```

### Configure AWS CLI
Ensure the AWS CLI is configured to allow access to your S3 buckets:

```
aws configure
```

Enter your AWS Access Key, AWS Secret Key, and Default region when prompted.

### Configuration
Configuration File (config.json)
Before running the pipeline, update the config.json file with the necessary parameters such as:

- S3 Bucket Locations (for input and output files)

- Reference Genome Path (for STAR alignment)

- Kallisto Index Path

Example config.json:

```
{
  "s3_input_bucket": "s3://your-input-bucket/raw_fastq/",
  "s3_output_bucket": "s3://your-output-bucket/processed_data/",
  "kallisto_index": "s3://your-index-bucket/kallisto_index.idx",
  "star_genome_index": "s3://your-index-bucket/star_genome_index/",
  "reference_genome": "/path/to/reference/genome.fasta"
}
```


### Running the Pipeline
## Initialize Airflow
Before running the DAG, ensure Airflow is set up properly. Initialize the Airflow database:

```
airflow db init
```

### Start the Airflow Scheduler

To schedule and monitor the DAG, start the Airflow scheduler:

```
airflow scheduler
```

### Run the DAG
You can trigger the DAG manually or set it up to run on a schedule. To trigger it manually, run:

```
airflow dags trigger <your_dag_id>
```

Make sure your DAG ID corresponds to the one specified in your pipeline configuration.

### CI/CD Pipeline

The repository is configured with GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD). The CI/CD pipeline ensures that changes are tested, linted, and validated before being deployed.

### Workflow Steps

### CI:

- Install dependencies and run tests.

- Validate the Airflow DAG.

- Lint the Python code.

### CD:

- Deploy the Airflow DAG to AWS.

- Upload processed files to S3.

### GitHub Actions Configuration
The pipeline is triggered on push or pull_request events to the main branch. It automatically runs unit tests, validates the DAG, and deploys the results.

### Output Files
The following output files are generated at different steps:

- Trimmed Reads: After the trimming step.

- Kallisto Quantification: Transcripts and their counts.

- STAR Aligned BAM Files: The aligned RNA-Seq data in BAM format.

- Summary Report: A summary of the entire RNA-Seq workflow, including statistics.

All output files are uploaded to the S3 bucket specified in the config.json file.
