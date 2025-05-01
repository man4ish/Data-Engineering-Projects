from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

default_args = {
    'owner': 'manish',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG('rnaseq_pipeline',
         default_args=default_args,
         schedule_interval=None,
         catchup=False,
         description='RNA-seq pipeline without Docker, using S3 and CLI tools') as dag:

    from scripts.download_from_s3 import download_inputs
    from scripts.trim_reads import run_skewer
    from scripts.run_kallisto import run_kallisto
    from scripts.run_star import run_star
    from scripts.sort_index_bam import sort_and_index
    from scripts.generate_summary import run_picard
    from scripts.upload_to_s3 import upload_outputs

    t1 = PythonOperator(task_id='download_inputs', python_callable=download_inputs)
    t2 = PythonOperator(task_id='trim_reads', python_callable=run_skewer)
    t3 = PythonOperator(task_id='quantify_kallisto', python_callable=run_kallisto)
    t4 = PythonOperator(task_id='align_star', python_callable=run_star)
    t5 = PythonOperator(task_id='sort_index_bam', python_callable=sort_and_index)
    t6 = PythonOperator(task_id='generate_summary', python_callable=run_picard)
    t7 = PythonOperator(task_id='upload_outputs', python_callable=upload_outputs)

    t1 >> t2 >> [t3, t4]
    t4 >> t5 >> t6 >> t7
    t3 >> t7  # kallisto output also gets uploaded

