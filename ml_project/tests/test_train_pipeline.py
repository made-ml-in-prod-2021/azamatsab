import pytest
from hydra.experimental import compose, initialize
from omegaconf import OmegaConf

from src.train import train

@pytest.fixture
def config():
    with initialize(config_path="../src/conf", job_name="test_train"):
        cfg = compose(config_name="config")
    return cfg

def test_train(config):
    train(config)
