import pytest
import pandas as pd
import yaml

from src.features.features import drop_target, extract_target, split_by_feature_type, build_transformer
from src.features.features import build_categorical_pipeline, build_numerical_pipeline
from src.entities.config import FeatureParams, Transforms

INPUT_PATH = 'tests/data/heart.csv'
FEATURE_CONF_PATH = 'src/conf/features/simple_featuers.yaml'
TRANS_CONF_PATH = 'src/conf/transforms/transforms.yaml'

@pytest.fixture
def params():
    with open(FEATURE_CONF_PATH) as fin:
        f_params = yaml.load(fin, Loader=yaml.FullLoader)
    return FeatureParams(**f_params)

@pytest.fixture
def tr_params():
    with open(TRANS_CONF_PATH) as fin:
        f_params = yaml.load(fin, Loader=yaml.FullLoader)
    return Transforms(**f_params)

@pytest.fixture
def data():
    return pd.read_csv(INPUT_PATH)

def test_drop_target(data, params):
    df = drop_target(data, params)
    assert params.target_col not in list(df.columns)

def test_extract_target(data, params):
    target = extract_target(data, params)
    assert len(target) == len(data)

def test_split_by_feature_type(data, params):
    splitted = split_by_feature_type(data, params)
    assert isinstance(splitted, dict)
    assert len(splitted) == 2
    assert 'num_features' in splitted
    assert 'cat_features' in splitted
    assert len(splitted['num_features'].columns) == len(params.numerical_features)
    assert len(splitted['cat_features'].columns) == len(params.categorical_features)

def test_build_transformer(data, params, tr_params):
    transformer = build_transformer(params, tr_params)
    transformer.fit_transform(data)

def test_build_cat_pipeline(data, params, tr_params):
    splitted = split_by_feature_type(data, params)
    pipeline = build_categorical_pipeline(tr_params)
    pipeline.fit_transform(splitted['cat_features'])

def test_build_num_pipeline(data, params, tr_params):
    splitted = split_by_feature_type(data, params)
    pipeline = build_numerical_pipeline(tr_params)
    pipeline.fit_transform(splitted['num_features'])
