import pytest
import yaml
import pandas as pd
import numpy as np

from src.features.transforms import StandardScaler
from src.entities.config import FeatureParams
from src.features.features import drop_target, extract_target

# INPUT_PATH = 'data/heart.csv'
FEATURE_CONF_PATH = "src/conf/features/simple_featuers.yaml"


@pytest.fixture
def params():
    with open(FEATURE_CONF_PATH) as fin:
        f_params = yaml.load(fin, Loader=yaml.FullLoader)
    return FeatureParams(**f_params)


@pytest.fixture
def data():
    data = {}
    columns = ["A", "B", "target"]
    for col in columns:
        data[col] = np.random.rand(10)
    return pd.DataFrame.from_dict(data)


def test_standard_scaler_without_target(data, params):
    df = drop_target(data, params)
    scaler = StandardScaler()
    scaler.fit(df)
    out = scaler.transform(df)
    out_mean = out.mean(axis=0)
    out_std = out.std(axis=0)

    for i in range(len(out_mean)):
        assert np.isclose(out_mean.iloc[i], 0)

    for i in range(len(out_std)):
        assert np.isclose(out_std.iloc[i], 1)

    assert out.shape == df.shape


def test_standard_scaler_with_target(data, params):
    df = drop_target(data, params)
    target = extract_target(data, params)
    scaler = StandardScaler()
    scaler.fit(df, target)
    out = scaler.transform(df, target)
    out_mean = out.mean(axis=0)
    out_std = out.std(axis=0)

    for i in range(len(out_mean)):
        assert np.isclose(out_mean.iloc[i], 0)

    for i in range(len(out_std)):
        assert np.isclose(out_std.iloc[i], 1)
    assert out.shape == df.shape


def test_standard_scaler_fit_transform_without_target(data, params):
    df = drop_target(data, params)
    scaler = StandardScaler()
    out = scaler.fit_transform(df)
    out_mean = out.mean(axis=0)
    out_std = out.std(axis=0)

    for i in range(len(out_mean)):
        assert np.isclose(out_mean.iloc[i], 0)

    for i in range(len(out_std)):
        assert np.isclose(out_std.iloc[i], 1)
    assert out.shape == df.shape


def test_standard_scaler_fit_transform_with_target(data, params):
    df = drop_target(data, params)
    target = extract_target(data, params)
    scaler = StandardScaler()
    out = scaler.fit_transform(df, target)
    out_mean = out.mean(axis=0)
    out_std = out.std(axis=0)

    for i in range(len(out_mean)):
        assert np.isclose(out_mean.iloc[i], 0)

    for i in range(len(out_std)):
        assert np.isclose(out_std.iloc[i], 1)
    assert out.shape == df.shape
