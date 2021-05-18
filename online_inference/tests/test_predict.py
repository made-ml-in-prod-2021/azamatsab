import json

import pytest
import yaml
from fastapi.testclient import TestClient

from main import app
from utils import load_config
from entities.config import TestConfig

client = TestClient(app)

@pytest.fixture
def config():
    return TestConfig(**load_config("tests/test_conf/test_conf.yml"))

@pytest.fixture
def data(config):
    with open(config.data_path) as fout:
        data = json.load(fout)
    return data

def test_predict_item_class_true(data):
    response = client.post(
        "/predict",
        headers={"X-Token": "coneofsilence"},
        json=data[0],
    )
    assert response.status_code == 200
    assert response.json() == {"class": 1}


def test_predict_item_class_false(data):
    response = client.post(
        "/predict",
        headers={"X-Token": "coneofsilence"},
        json=data[1],
    )
    assert response.status_code == 200
    assert response.json() == {"class": 0}

def test_predict_item_bad_type(data):
    data[1]["age"] = "twenty two"
    response = client.post(
        "/predict",
        headers={"X-Token": "coneofsilence"},
        json=data[1],
    )
    assert response.status_code == 400

def test_predict_item_wrong_size(data):
    del data[1]["age"]
    response = client.post(
        "/predict",
        headers={"X-Token": "coneofsilence"},
        json=data[1],
    )
    assert response.status_code == 400