from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

#g are defaults which can be overridden later on
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 4, 15),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('umbrella', default_args=default_args)


fetch_weather_forecast = BashOperator(task_id="fetch_weather_forecast",bash_command='echo "fetch_weatger_forecast"', dag=dag)
fetch_sales_data = BashOperator(task_id="fetch_sales_data",bash_command='echo "fetch_sales_data"', dag=dag)



# Set dependencies between all tasks
fetch_weather_forecast >> clean_forecast_data >> join_datasets


