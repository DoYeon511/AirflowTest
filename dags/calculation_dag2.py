from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

default_args = {
    'owner': 'doyeon',
    'start_date': datetime(2026, 6, 24),
    'retries': 1,
}

def generate_numbers():
    """랜덤 숫자 5개 생성"""
    numbers = [random.randint(1, 100) for _ in range(5)]
    print(f"생성된 숫자들: {numbers}")
    return numbers

def calculate_sum(**context):
    """이전 task 결과를 받아서 합계 계산"""
    numbers = context['task_instance'].xcom_pull(task_ids='generate_numbers')
    total = sum(numbers)
    print(f"합계: {total}")
    return total

def calculate_average(**context):
    """이전 task들 결과로 평균 계산"""
    numbers = context['task_instance'].xcom_pull(task_ids='generate_numbers')
    avg = sum(numbers) / len(numbers)
    print(f"평균: {avg:.2f}")
    return avg

with DAG(
    dag_id='calculation_dag2',
    default_args=default_args,
    description='숫자 생성 후 합계와 평균 계산',
    schedule=None,
    catchup=False,
    tags=['test', 'python', 'xcom'],
) as dag:

    task_generate = PythonOperator(
        task_id='generate_numbers',
        python_callable=generate_numbers,
    )

    task_sum = PythonOperator(
        task_id='calculate_sum',
        python_callable=calculate_sum,
    )

    task_avg = PythonOperator(
        task_id='calculate_average',
        python_callable=calculate_average,
    )

    task_generate >> [task_sum, task_avg]