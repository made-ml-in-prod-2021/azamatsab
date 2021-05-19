import copy
import json
import logging

import requests

from utils import load_config
from entities.config import TestConfig

logging.basicConfig(level=logging.INFO)
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
    logging.info(response.text)
    assert response.status_code == 400


def make_request_wrong_size():
    data_bad = copy.deepcopy(data[1])
    del data_bad["age"]
    response = requests.post(config.url, json=data_bad)
    logging.info(response.text)
    assert response.status_code == 400


if __name__ == "__main__":
    logging.info("Make request with good data. Must return pos class")
    make_request_pos_class()
    logging.info("Make request with good data. Must return neg class")
    make_request_neg_class()
    logging.info(
        "Make request with bad type data. Must return 400 and error message in json format"
    )
    make_request_bad_type()
    logging.info(
        "Make request with wrong size data. Must return 400 and error message in json format"
    )
    make_request_wrong_size()
