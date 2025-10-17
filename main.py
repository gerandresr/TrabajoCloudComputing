from pathlib import Path
from typing import List

import joblib
import numpy as np
from fastapi import Depends, FastAPI  # pip install "fastapi[standard]"
from pydantic import BaseModel

FEATURE_NAMES: List[str] = [
    "inflacion_cl",
    "inflacion_us",
    "tpm_cl",
    "tpm_us",
    "ipc_cl",
    "ipc_us",
    "sp500",
    "ipsa",
    "tpm_cl_cat",
    "tpm_us_cat",
    "tpm_cl_is_0",
    "tpm_us_is_0",
    "tpm_cl_is_1",
    "tpm_us_is_1",
    "tpm_cl_is_2",
    "tpm_us_is_2",
    "tpm_cl_change",
    "tpm_us_change",
    "new_max_sp500",
    "new_max_ipsa",
    "new_max_usdclp",
    "tpm_diff",
    "tpm_diff_pos",
]

MODEL_PATH = Path(__file__).with_name("model.pkl")
SCALER_PATH = Path(__file__).with_name("scaler.pkl")

# Load model and scaler from .pkl files using joblib for compatibility
MODEL = joblib.load(MODEL_PATH)
SCALER = joblib.load(SCALER_PATH)
MODEL_NAME = type(MODEL).__name__

app = FastAPI()


class ModelInput(BaseModel):
    inflacion_cl: float
    inflacion_us: float
    tpm_cl: float
    tpm_us: float
    ipc_cl: float
    ipc_us: float
    sp500: float
    ipsa: float
    tpm_cl_cat: float
    tpm_us_cat: float
    tpm_cl_is_0: float
    tpm_us_is_0: float
    tpm_cl_is_1: float
    tpm_us_is_1: float
    tpm_cl_is_2: float
    tpm_us_is_2: float
    tpm_cl_change: float
    tpm_us_change: float
    new_max_sp500: float
    new_max_ipsa: float
    new_max_usdclp: float
    tpm_diff: float
    tpm_diff_pos: float


@app.get("/predict")
async def predict(input_data: ModelInput = Depends()) -> dict:
    values = np.array([[getattr(input_data, feature) for feature in FEATURE_NAMES]])
    # Apply scaler transformation before prediction
    scaled_values = SCALER.transform(values)
    prediction = MODEL.predict(scaled_values)
    return {"model_name": MODEL_NAME, "output": float(prediction[0])}


