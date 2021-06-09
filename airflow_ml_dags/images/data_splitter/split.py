import os

import click
import pandas as pd
from sklearn.model_selection import train_test_split

DATA_NAME = "data.csv"
TARGET_NAME = "target.csv"
DATA_TRAIN_NAME = "data_train.csv"
DATA_VAL_NAME = "data_val.csv"
TARGET_TRAIN_NAME = "target_train.csv"
TARGET_VAL_NAME = "target_val.csv"


@click.command()
@click.option("--input-dir")
@click.option("--output-dir")
def split_data(input_dir: str, output_dir: str):
    data = pd.read_csv(os.path.join(input_dir, DATA_NAME))
    target = pd.read_csv(os.path.join(input_dir, TARGET_NAME))
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
    os.makedirs(output_dir, exist_ok=True)
    x_train.to_csv(os.path.join(output_dir, DATA_TRAIN_NAME), index=False)
    y_train.to_csv(os.path.join(output_dir, TARGET_TRAIN_NAME), index=False)
    x_test.to_csv(os.path.join(output_dir, DATA_VAL_NAME), index=False)
    y_test.to_csv(os.path.join(output_dir, TARGET_VAL_NAME), index=False)
    

if __name__ == '__main__':
    split_data()