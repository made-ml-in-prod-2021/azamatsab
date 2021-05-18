from dataclasses import dataclass


@dataclass
class Config:
    model_path: str
    pipeline_path: str
