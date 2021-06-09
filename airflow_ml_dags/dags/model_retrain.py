import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

def _wait_for_file():
    return os.path.exists("/opt/airflow/data/wait.txt")

with DAG(
        "model_retrain",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(0),
) as dag:
    wait_for_data = FileSensor(
                 task_id="file_sensor_task1",
                 filepath="/opt/airflow/data/raw/{{ ds }}/data.csv",
                 fs_conn_id="docker",
                 poke_interval=1,
                 mode="poke",
              )

    move_data = DockerOperator(
        image="airflow-move-data",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/processed/{{ ds }}",
        task_id="docker-airflow-move",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=["/home/azamat/Documents/MADE/ml_on_production/airflow_ml_dags/data:/data"]
    )

    split_data = DockerOperator(
        image="airflow-split-data",
        command="--input-dir /data/processed/{{ ds }} --output-dir /data/processed/{{ ds }}",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=["/home/azamat/Documents/MADE/ml_on_production/airflow_ml_dags/data:/data"]
    )

    train_model = DockerOperator(
        image="airflow-train-model",
        command="--input-dir /data/processed/{{ ds }} --output-dir /data/models/{{ ds }}",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=["/home/azamat/Documents/MADE/ml_on_production/airflow_ml_dags/data:/data"]
    )

    val_model = DockerOperator(
        image="airflow-val-model",
        command="--model-dir /data/models/{{ ds }} --data-dir /data/processed/{{ ds }} --metrics-dir /data/metrics/{{ ds }}",
        task_id="docker-airflow-val",
        do_xcom_push=False,
        network_mode="bridge",
        volumes=["/home/azamat/Documents/MADE/ml_on_production/airflow_ml_dags/data:/data"]
    )

    wait_for_data >> move_data >> split_data >> train_model >> val_model