import json
import pathlib


import requests
import requests.exceptions as requests_exceptions

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 4, 15),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    dag_id="listing_2_3",
    description="Download rocket pictures of recently launched rockets.",
    default_args=default_args)
}
