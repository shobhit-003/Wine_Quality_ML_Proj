import joblib
import numpy as np
import pandas as pd
from pathlib import Path

model_path = 'artifacts/model_trainer/model.joblib'


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path(model_path))


    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction