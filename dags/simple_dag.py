
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id="simple_dag", 
    # start_date=datetime(2022, 7, 5),
    start_date=days_ago(3),
    schedule_interval="@daily",
    catchup=True,
    ) as dag:

    task_1 = DummyOperator(task_id="task_1")

    task_2 = DummyOperator(task_id="task_2")

    task_1 >> task_2
