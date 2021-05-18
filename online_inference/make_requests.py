import copy
import json
import logging

import requests

from utils import load_config
from entities.config import TestConfig

config = TestConfig(**load_config("tests/test_conf/test_conf.yml"))
data = json.load(open(config.data_path))


def make_request_pos_class():
    response = requests.post(config.url, json=data[0])
    assert response.status_code == 200


def make_request_neg_class():
    response = requests.post(config.url, json=data[1])
    assert response.status_code == 200


def make_request_bad_type():
    data_bad = copy.deepcopy(data[1])
    data_bad["age"] = "twenty two"
    response = requests.post(config.url, json=data_bad)
    logging.warning(response.text)
    assert response.status_code == 400


def make_request_wrong_size():
    data_bad = copy.deepcopy(data[1])
    del data_bad["age"]
    response = requests.post(config.url, json=data_bad)
    logging.warning(response.text)
    assert response.status_code == 400


if __name__ == "__main__":
    make_request_pos_class()
    make_request_neg_class()
    make_request_bad_type()
    make_request_wrong_size()
