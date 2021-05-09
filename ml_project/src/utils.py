import os
import logging
import pickle

from sklearn.base import BaseEstimator

logger = logging.getLogger("classifier.utils")

def check_dir(path: str) -> None:
    if not os.path.exists(path):
        logger.info(f"{path} does not exist. Creating ...")
        os.makedirs(path)

def save_model(model: BaseEstimator, path: str) -> None:
    logger.info(f'Saving model to {path}')
    pickle.dump(model, open(path, 'wb'))

def load_model(path: str) -> BaseEstimator:
    logger.info(f'Loading model from {path}')
    return pickle.load(open(path, 'rb'))
