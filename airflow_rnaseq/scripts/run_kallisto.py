# scripts/run_kallisto.py
import subprocess
import os

def run_kallisto():
    output_dir = '/tmp/rnaseq/kallisto'
    os.makedirs(output_dir, exist_ok=True)
    index = '/tmp/rnaseq/input/kallisto_index.idx'
    r1 = '/tmp/rnaseq/trimmed/trimmed-trimmed-pair1.fastq'
    r2 = '/tmp/rnaseq/trimmed/trimmed-trimmed-pair2.fastq'
    subprocess.run(['kallisto', 'quant', '-i', index, '-o', output_dir, r1, r2], check=True)
