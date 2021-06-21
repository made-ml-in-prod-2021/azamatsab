import os
import pickle

import click
import pandas as pd
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score

DATA_NAME = "data.csv"

@click.command()
@click.option("--input-dir")
@click.option("--model-path")
@click.option("--out")
def predict(input_dir: str, model_path: str, out: str):
    path = os.path.join(input_dir, DATA_NAME)
    data = pd.read_csv(path)
    
    with open(model_path, 'rb') as fin:
        model = pickle.load(fin)

    predictions = model.predict(data)

    path, _ = os.path.split(out)
    os.makedirs(path, exist_ok=True)

    pred = pd.DataFrame(predictions)
    pred.to_csv(out)

if __name__ == '__main__':
    predict()