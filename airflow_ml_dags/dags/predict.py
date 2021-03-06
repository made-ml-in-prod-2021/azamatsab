import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.dates import days_ago
from airflow.models import Variable
from constants import PROCESSED_PATH, MODELS_PATH, PRED_PATH, VOLUME, PATH_FROM_VARIABLE


default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "predict",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(0),
) as dag:
    wait_for_data = FileSensor(
                 task_id="file_sensor_task2",
                 filepath="/opt/airflow{}/data.csv".format(PROCESSED_PATH),
                 fs_conn_id="docker",
                 poke_interval=1,
                 mode="poke",
              )

    predict = DockerOperator(
        image="airflow-predict",
        command="--input-dir {} --model-path {}/{} --out {}/predictions.csv".format(PROCESSED_PATH, MODELS_PATH, PATH_FROM_VARIABLE, PRED_PATH),
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=[VOLUME]
    )

    wait_for_data >> predict