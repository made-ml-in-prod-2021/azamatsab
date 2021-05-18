from typing import Optional, Union

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

Iterable = Union[np.ndarray, pd.DataFrame]

SimpleImputer = SimpleImputer
OneHotEncoder = OneHotEncoder


class StandardScaler:
    def __init__(self) -> None:
        self.mu = None
        self.std = None

    def fit(self, x: Iterable, y: Optional[np.ndarray] = None) -> "StandardScaler":
        self.mu = x.mean(axis=0)
        self.std = x.std(axis=0)
        return self

    def transform(self, x: Iterable, y: Optional[np.ndarray] = None) -> Iterable:
        x = (x - self.mu) / self.std
        return x

    def fit_transform(self, x: Iterable, y: Optional[np.ndarray] = None) -> Iterable:
        return self.fit(x, y).transform(x, y)
