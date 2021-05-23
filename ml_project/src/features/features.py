import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from entities.config import FeatureParams, Transforms
from features.transforms import StandardScaler
import features.transforms as transformers


def build_categorical_pipeline(params: Transforms) -> Pipeline:
    transforms = []

    for transform in params.cat_transforms:
        transforms.append((transform, getattr(transformers, transform)()))
    categorical_pipeline = Pipeline(transforms)
    return categorical_pipeline


def build_numerical_pipeline(params: Transforms) -> Pipeline:
    transforms = []

    for transform in params.num_transforms:
        transforms.append((transform, getattr(transformers, transform)()))
    num_pipeline = Pipeline(transforms)
    return num_pipeline


def build_transformer(
    params: FeatureParams, tr_params: Transforms
) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [
            (
                "categorical_pipeline",
                build_categorical_pipeline(tr_params),
                list(params.categorical_features),
            ),
            (
                "numerical_pipeline",
                build_numerical_pipeline(tr_params),
                list(params.numerical_features),
            ),
        ]
    )
    return transformer


def extract_target(df: pd.DataFrame, params: FeatureParams) -> pd.Series:
    target = df[params.target_col]
    return target


def drop_target(df: pd.DataFrame, params: FeatureParams) -> pd.DataFrame:
    df = df.drop(columns=[params.target_col])
    return df


def split_by_feature_type(df: pd.DataFrame, params: FeatureParams) -> dict:
    num_features = df[params.numerical_features]
    cat_features = df[params.categorical_features]
    return {"num_features": num_features, "cat_features": cat_features}
