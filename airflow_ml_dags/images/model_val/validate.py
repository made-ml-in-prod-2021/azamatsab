import os
import pickle

import click
import pandas as pd
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score

DATA_VAL_NAME = "data_val.csv"
TARGET_VAL_NAME = "target_val.csv"
MODEL_NAME = 'model.pickle'
METRIC_FILE_NAME = 'metrics.txt'

@click.command()
@click.option("--model-dir")
@click.option("--data-dir")
@click.option("--metrics-dir")
def validate(model_dir: str, data_dir: str, metrics_dir: str):
    data = pd.read_csv(os.path.join(data_dir, DATA_VAL_NAME))
    target = pd.read_csv(os.path.join(data_dir, TARGET_VAL_NAME))
    
    with open(os.path.join(model_dir, MODEL_NAME), 'rb') as fin:
        model = pickle.load(fin)

    target = target["target"]
    predictions = model.predict(data)

    roc_auc = round(roc_auc_score(target, predictions), 4)
    accuracy = round(accuracy_score(target, predictions), 4)
    precision = round(precision_score(target, predictions), 4)
    recall = round(recall_score(target, predictions), 4)

    os.makedirs(metrics_dir, exist_ok=True)

    with open(os.path.join(metrics_dir, METRIC_FILE_NAME), "w") as fout:
        fout.write("roc_auc: {}, accuracy: {}, precision: {}, recall: {}".format(roc_auc, accuracy, precision, recall))

if __name__ == '__main__':
    validate()