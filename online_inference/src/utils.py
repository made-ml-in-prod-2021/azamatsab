import os
import logging
import pickle

import yaml
from sklearn.base import BaseEstimator

from input_format import Item

logger = logging.getLogger("uvicorn")


def load_config(path: str) -> dict:
    with open(path) as fin:
        config = yaml.safe_load(fin)
    return config


def check_dir(path: str) -> None:
    if not os.path.exists(path):
        logger.info(f"{path} does not exist. Creating ...")
        os.makedirs(path)


def save_model(model: BaseEstimator, path: str) -> None:
    logger.info(f"Saving model to {path}")
    pickle.dump(model, open(path, "wb"))


def load_model(path: str) -> BaseEstimator:
    logger.info(f"Loading model from {path}")
    return pickle.load(open(path, "rb"))
