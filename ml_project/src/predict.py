import os
import logging
import pickle

import hydra
from hydra.utils import instantiate, to_absolute_path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.entities.config import PredConfig
from src.features.features import drop_target, extract_target, build_transformer
from src.utils import load_model, check_dir


logger = logging.getLogger("classifier")


def predict(config: PredConfig):
    model_name = os.path.split(config.general.model_path)[1]
    logger.info(f"Starting prediction using {model_name}")

    model = load_model(to_absolute_path(config.general.model_path))

    data_path = to_absolute_path(config.general.input_data_path)
    data = pd.read_csv(data_path)
    pipeline = build_transformer(config.features, config.transforms)
    data = pipeline.fit_transform(data)
    predictions = model.predict(data)
    predictions = pd.DataFrame(predictions, columns=["target"])

    save_path = os.path.join(to_absolute_path(config.general.pred_path), model_name)
    check_dir(to_absolute_path(config.general.pred_path))
    logger.info(f"Saving predictions to {save_path}")
    predictions.to_csv(save_path, index=False)


@hydra.main(config_path="conf", config_name="pred_config")
def run(config: PredConfig) -> None:
    predict(config)


if __name__ == "__main__":
    run()
