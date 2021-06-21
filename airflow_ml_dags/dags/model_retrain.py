import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.dates import days_ago
from airflow.models import Variable
from constants import RAW_PATH, PROCESSED_PATH, MODELS_PATH, METRICS_PATH, VOLUME

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
        "model_retrain",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(0),
) as dag:
    wait_for_data = FileSensor(
                 task_id="file_sensor_task1",
                 filepath="/opt/airflow{}/data.csv".format(RAW_PATH),
                 fs_conn_id="docker",
                 poke_interval=1,
                 mode="poke",
              )

    move_data = DockerOperator(
        image="airflow-move-data",
        command="--input-dir {} --output-dir {}".format(RAW_PATH, PROCESSED_PATH),
        task_id="docker-airflow-move",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=[VOLUME]
    )

    split_data = DockerOperator(
        image="airflow-split-data",
        command="--input-dir {} --output-dir {}".format(PROCESSED_PATH, PROCESSED_PATH),
        task_id="docker-airflow-split",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=[VOLUME]
    )

    train_model = DockerOperator(
        image="airflow-train-model",
        command="--input-dir {} --output-dir {}".format(PROCESSED_PATH, MODELS_PATH),
        task_id="docker-airflow-train",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=[VOLUME]
    )

    val_model = DockerOperator(
        image="airflow-val-model",
        command="--model-dir {} --data-dir {} --metrics-dir {}".format(MODELS_PATH, PROCESSED_PATH, METRICS_PATH),
        task_id="docker-airflow-val",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=[VOLUME]
    )

    wait_for_data >> move_data >> split_data >> train_model >> val_model