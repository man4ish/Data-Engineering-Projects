# scripts/download_from_s3.py
import boto3
import os

def download_inputs():
    s3 = boto3.client('s3')
    bucket = 'your-bucket'
    prefix = 'rnaseq/input/'
    local_dir = '/tmp/rnaseq/input'
    os.makedirs(local_dir, exist_ok=True)

    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for obj in response.get('Contents', []):
        key = obj['Key']
        filename = os.path.basename(key)
        if filename:
            s3.download_file(bucket, key, os.path.join(local_dir, filename))
