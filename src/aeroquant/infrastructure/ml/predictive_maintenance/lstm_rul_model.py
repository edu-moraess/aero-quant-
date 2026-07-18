from typing import Optional

import numpy as np

from aeroquant.domain.ports.i_model_repository import IModelRepository

class LSTMRULModel:
    def __init__(self, model_repository: IModelRepository):
        self.model_repository = model_repository

    def predict(self, data: np.ndarray) -> np.ndarray:
        model = self.model_repository.load_model("lstm_rul_model")
        if model is None:
            raise ValueError("LSTM model not found")

        # Placeholder: Lógica real de predição seria implementada aqui
        return model.predict(data)