from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def extract(**kwargs):
    print("Extracting data")

def load(**kwargs):
    print("Loading data")

def transform(**kwargs):
    print("Transforming data")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'simple_etl',
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval=timedelta(days=1),
)

t1 = PythonOperator(
    task_id='extract',
    provide_context=True,
    python_callable=extract,
    dag=dag,
)

t2 = PythonOperator(
    task_id='transform',
    provide_context=True,
    python_callable=transform,
    dag=dag,
)

t3 = PythonOperator(
    task_id='load',
    provide_context=True,
    python_callable=load,
    dag=dag,
)

t1 >> t2 >> t3
