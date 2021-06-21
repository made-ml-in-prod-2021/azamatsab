import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from constants import RAW_PATH, VOLUME

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "data_generator",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(0),
) as dag:
    generate = DockerOperator(
        image="airflow-generate",
        command="--output-dir {}".format(RAW_PATH),
        task_id="docker-airflow-generate",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=[VOLUME]
    )

    generate