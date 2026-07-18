from typing import Optional

import numpy as np

from aeroquant.domain.ports.i_model_repository import IModelRepository

class AutoencoderAnomalyDetector:
    def __init__(self, model_repository: IModelRepository):
        self.model_repository = model_repository

    def detect(self, data: np.ndarray) -> np.ndarray:
        model = self.model_repository.load_model("autoencoder_anomaly_detector")
        if model is None:
            raise ValueError("Autoencoder model not found")

        # Placeholder: Lógica real de detecção seria implementada aqui
        reconstruction_error = np.mean(np.abs(data - model.predict(data)))
        anomalies = reconstruction_error > 0.5  # Limiar fictício
        return anomalies