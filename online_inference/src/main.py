import os
import io
import logging
import pickle

import yaml
import uvicorn
import pandas as pd
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from entities.config import Config
from utils import load_model, load_config
from input_format import Item


logger = logging.getLogger("uvicorn")
config_path = os.getenv("PATH_TO_CONFIG")
config_path = "src/conf/config.yaml" if config_path is None else config_path
config = Config(**load_config(config_path))

model = load_model(config.model_path)
pipeline = load_model(config.pipeline_path)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                "detail": exc.errors(),
                "body": exc.body,
                "your_additional_errors": {
                    "Will be": "Inside",
                    "This": " Error message",
                },
            }
        ),
    )


@app.post("/predict")
async def predict(item: Item):
    try:
        data = item.dict()
        data = {key: [value] for key, value in data.items()}
        data = pd.DataFrame(data, index=None)
        data = pipeline.transform(data)
        prediction = model.predict(data.reshape(1, -1))
        return {"class": int(prediction[0])}
    except Exception as error:
        logging.error(error)
        raise HTTPException(status_code=400, detail=error)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
