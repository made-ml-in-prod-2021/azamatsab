import json

import pytest
import yaml
from fastapi.testclient import TestClient

from main import app
from utils import load_config
from entities.config import TestConfig


BAD_TYPE_MESSAGE = "value is not a valid float"
BAD_SIZE_MESSAGE = "field required"
FEATURE_NAME = "age"


@pytest.fixture
def config():
    return TestConfig(**load_config("tests/test_conf/test_conf.yml"))


@pytest.fixture
def data(config):
    with open(config.data_path) as fout:
        data = json.load(fout)
    return data


def test_predict_class_true(data):
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            headers={"X-Token": "coneofsilence"},
            json=data[0],
        )
        assert response.status_code == 200
        assert response.json() == {"class": 1}


def test_predict_class_false(data):
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            headers={"X-Token": "coneofsilence"},
            json=data[1],
        )
        assert response.status_code == 200
        assert response.json() == {"class": 0}


def test_predict_bad_type(data):
    with TestClient(app) as client:
        data[1][FEATURE_NAME] = "twenty two"
        response = client.post(
            "/predict",
            headers={"X-Token": "coneofsilence"},
            json=data[1],
        )
        message = json.loads(response.text)
        assert response.status_code == 400
        assert message["detail"][0]["msg"] == BAD_TYPE_MESSAGE
        assert FEATURE_NAME in message["detail"][0]["loc"]


def test_predict_wrong_size(data):
    with TestClient(app) as client:
        del data[1][FEATURE_NAME]
        response = client.post(
            "/predict",
            headers={"X-Token": "coneofsilence"},
            json=data[1],
        )
        message = json.loads(response.text)
        assert response.status_code == 400
        assert message["detail"][0]["msg"] == BAD_SIZE_MESSAGE
        assert FEATURE_NAME in message["detail"][0]["loc"]
