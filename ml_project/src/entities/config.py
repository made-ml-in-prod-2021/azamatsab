from dataclasses import dataclass, field
from typing import Any, List, Optional
from hydra.core.config_store import ConfigStore
from hydra.utils import instantiate
from omegaconf import MISSING, DictConfig, OmegaConf


@dataclass
class ReportConfig:
    input_path: str = MISSING
    output_path: str = MISSING


@dataclass
class Transforms:
    num_transforms: List[str] = MISSING
    cat_transforms: List[str] = MISSING


@dataclass
class Base:
    _target_: str = "sklearn.ensemble.RandomForestClassifier"
    random_state: int = MISSING


@dataclass
class RFConfig:
    _target_: str = "sklearn.ensemble.RandomForestClassifier"
    n_estimators: int = MISSING
    random_state: int = MISSING
    max_depth: int = MISSING


@dataclass
class LogregConfig:
    _target_: str = "sklearn.linear_model.LogisticRegression"
    penalty: str = MISSING
    solver: str = MISSING
    C: float = MISSING
    random_state: int = MISSING
    max_iter: int = MISSING


@dataclass
class GeneralConfig:
    input_data_path: str = MISSING
    output_model_path: str = MISSING
    random_state: int = MISSING
    val: float = MISSING


@dataclass
class GeneralPredConfig:
    model_path: str = MISSING
    input_data_path: str = MISSING
    pred_path: str = MISSING


@dataclass
class FeatureParams:
    categorical_features: List[str] = MISSING
    numerical_features: List[str] = MISSING
    target_col: str = MISSING


@dataclass
class Config:
    model: Any = Base()
    general: GeneralConfig = GeneralConfig()
    features: FeatureParams = FeatureParams()
    transforms: Transforms = Transforms()


@dataclass
class PredConfig:
    general: GeneralPredConfig = GeneralPredConfig()
    features: FeatureParams = FeatureParams()
    transforms: Transforms = Transforms()


cs = ConfigStore.instance()
cs.store(name="config", node=Config)
cs.store(group="model", name="logreg", node=LogregConfig)
cs.store(group="model", name="rf", node=RFConfig)

pcs = ConfigStore.instance()
pcs.store(name="pred_config", node=PredConfig)
