# scripts/sort_index_bam.py
import subprocess
import os

def sort_and_index():
    bam_path = '/tmp/rnaseq/star/aligned_Aligned.sortedByCoord.out.bam'
    sorted_bam = '/tmp/rnaseq/star/aligned_sorted.bam'
    subprocess.run(['samtools', 'sort', '-o', sorted_bam, bam_path], check=True)
    subprocess.run(['samtools', 'index', sorted_bam], check=True)

