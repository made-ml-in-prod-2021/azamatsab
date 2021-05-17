import pytest
from hydra.experimental import compose, initialize
from omegaconf import OmegaConf

from src.predict import predict


@pytest.fixture
def config():
    with initialize(config_path="../src/conf", job_name="test_predict"):
        cfg = compose(config_name="pred_config")
    return cfg


def test_train(config):
    predict(config)
