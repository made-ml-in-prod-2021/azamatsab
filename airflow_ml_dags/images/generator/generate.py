import os
import pandas as pd
import click

from sklearn.datasets import make_classification

DATA_NAME = "data.csv"
TARGET_NAME = "target.csv"

@click.command()
@click.option("--output-dir")
def generate(output_dir: str):
    data, target = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=2, n_repeated=0, n_classes=2, random_state=718)
    os.makedirs(output_dir, exist_ok=True)
    data = pd.DataFrame(data)
    target = pd.DataFrame(target, columns=["target"])
    assert len(data) == len(target)
    data.to_csv(os.path.join(output_dir, DATA_NAME), index=False)
    target.to_csv(os.path.join(output_dir, TARGET_NAME), index=False)


if __name__ == '__main__':
    generate()
