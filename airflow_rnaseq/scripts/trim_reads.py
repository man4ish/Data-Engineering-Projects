import subprocess
import os

def run_skewer():
    input_dir = '/tmp/rnaseq/input'
    output_dir = '/tmp/rnaseq/trimmed'
    os.makedirs(output_dir, exist_ok=True)
    r1 = os.path.join(input_dir, 'sample_R1.fastq')
    r2 = os.path.join(input_dir, 'sample_R2.fastq')
    subprocess.run(['skewer', '-o', os.path.join(output_dir, 'trimmed'), r1, r2], check=True)
