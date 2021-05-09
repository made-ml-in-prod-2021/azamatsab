import os
from collections import namedtuple

import pytest
import yaml

from src.report_generator import generate_report
from src.entities.config import ReportConfig

INPUT_PATH = 'tests/data/heart.csv'
OUTPUT_PATH = 'tests/data/test_report/report.html'

def test_generate_report():
    Conf = namedtuple('Conf', ['input_path', 'output_path'])
    conf = Conf(INPUT_PATH, OUTPUT_PATH)
    generate_report(conf)
    assert os.path.exists(OUTPUT_PATH)
