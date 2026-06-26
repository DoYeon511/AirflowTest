from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id='auto_test_dag',
    start_date=datetime(2026, 6, 26),
    schedule=None,
    catchup=False,
    tags=['test'],
) as dag:
    PythonOperator(
        task_id='hello',
        python_callable=lambda: print("test"),
    )