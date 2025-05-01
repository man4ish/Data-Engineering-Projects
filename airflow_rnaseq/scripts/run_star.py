# scripts/run_star.py
import subprocess
import os

def run_star():
    output_dir = '/tmp/rnaseq/star'
    os.makedirs(output_dir, exist_ok=True)
    genome_dir = '/tmp/rnaseq/input/star_index'
    r1 = '/tmp/rnaseq/trimmed/trimmed-trimmed-pair1.fastq'
    r2 = '/tmp/rnaseq/trimmed/trimmed-trimmed-pair2.fastq'
    subprocess.run([
        'STAR', '--genomeDir', genome_dir,
        '--readFilesIn', r1, r2,
        '--runThreadN', '4',
        '--outFileNamePrefix', os.path.join(output_dir, 'aligned_'),
        '--outSAMtype', 'BAM', 'SortedByCoordinate'
    ], check=True)
