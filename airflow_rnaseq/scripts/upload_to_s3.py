# scripts/upload_to_s3.py
import boto3
import os

def upload_outputs():
    s3 = boto3.client('s3')
    bucket = 'your-bucket'
    output_dir = '/tmp/rnaseq/'
    s3_prefix = 'rnaseq/output/'

    for root, dirs, files in os.walk(output_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, output_dir)
            s3.upload_file(full_path, bucket, os.path.join(s3_prefix, rel_path))
