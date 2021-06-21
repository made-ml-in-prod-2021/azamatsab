import os
import pickle

import click
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

DATA_TRAIN_NAME = "data_train.csv"
TARGET_TRAIN_NAME = "target_train.csv"
MODEL_NAME = 'model.pickle'

@click.command()
@click.option("--input-dir")
@click.option("--output-dir")
def train(input_dir: str, output_dir: str):
    data = pd.read_csv(os.path.join(input_dir, DATA_TRAIN_NAME))
    target = pd.read_csv(os.path.join(input_dir, TARGET_TRAIN_NAME))
    clf = RandomForestClassifier(max_depth=10, random_state=0)
    clf.fit(data, target["target"])

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, MODEL_NAME), 'wb') as fout:
        pickle.dump(clf, fout)

if __name__ == '__main__':
    train()