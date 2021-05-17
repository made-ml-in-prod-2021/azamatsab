import os
import logging
import pickle

import hydra
from hydra.utils import instantiate, to_absolute_path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from entities.config import Config
from features.features import drop_target, extract_target, build_transformer
from utils import save_model, check_dir

logger = logging.getLogger("classifier")


def train(config: Config):
    logger.info(f"Start training {config.model._target_} model")

    model = instantiate(config.model)

    data_path = to_absolute_path(config.general.input_data_path)
    data = pd.read_csv(data_path)
    target = extract_target(data, config.features)
    data = drop_target(data, config.features)
    pipeline = build_transformer(config.features, config.transforms)
    data = pipeline.fit_transform(data)
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=config.general.val
    )

    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    logger.info(f"Accuracy score = {accuracy_score(y_test, prediction)}")

    check_dir(to_absolute_path(config.general.output_model_path))
    save_path = to_absolute_path(config.general.output_model_path)
    save_path = os.path.join(save_path, config.model._target_.split(".")[-1])
    save_model(model, save_path)


@hydra.main(config_path="conf", config_name="config")
def run(config: Config) -> None:
    train(config)


if __name__ == "__main__":
    run()
