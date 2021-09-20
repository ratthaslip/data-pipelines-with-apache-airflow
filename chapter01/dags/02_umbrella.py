"""DAG demonstrating the umbrella use case with dummy operators."""

import airflow.utils.dates
from airflow import DAG
from airflow.operators.dummy import DummyOperator

dag = DAG(
    dag_id="01_umbrella",
    description="Umbrella example with DummyOperators.",
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily",
)


fetch_sales_data = DummyOperator(task_id="fetch_sales_data", dag=dag)
clean_sales_data = DummyOperator(task_id="clean_sales_data", dag=dag)


# Set dependencies between all tasks
fetch_sales_data >> clean_sales_data

