from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'doyeon',
    'depends_on_past': False,
    'start_date': datetime(2026, 6, 24),
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def say_hello():
    print("Hello, Airflow! 🎉")
    return "Hello World"

def say_goodbye():
    print("Goodbye, see you next run!")
    return "Goodbye"

with DAG(
    dag_id='delete_test_dag',
    default_args=default_args,
    description='Dag 삭제 test',
    schedule_interval=None,
    catchup=False,
    tags=['test', 'delete'],
) as dag:

    hello_task = PythonOperator(
        task_id='say_hello',
        python_callable=say_hello,
    )

    goodbye_task = PythonOperator(
        task_id='say_goodbye',
        python_callable=say_goodbye,
    )

    hello_task >> goodbye_task