import os
import io
import logging
import pickle

import yaml
import uvicorn
import pandas as pd
from fastapi import FastAPI

from utils import load_model, load_config
from input_format import Item


logger = logging.getLogger("uvicorn")
config = load_config("src/conf/config.yaml")

model = load_model(config.model_path)
pipeline = load_model(config.pipeline_path)

app = FastAPI()

@app.post("/predict")
async def predict(item: Item):
    try:
        data = item.dict()
        data = {key: [value] for key, value in data.items()}
        data = pd.DataFrame(data, index=None)
        data = pipeline.transform(data)
        prediction = model.predict(data.reshape(1, -1))
        return {"class": int(prediction[0])}
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
