# scripts/generate_summary.py
import subprocess
import os

def run_picard():
    bam = '/tmp/rnaseq/star/aligned_sorted.bam'
    metrics = '/tmp/rnaseq/star/alignment_metrics.txt'
    subprocess.run([
        'picard', 'CollectAlignmentSummaryMetrics',
        'I=' + bam,
        'O=' + metrics,
        'R=/tmp/rnaseq/input/reference.fasta'
    ], check=True)
