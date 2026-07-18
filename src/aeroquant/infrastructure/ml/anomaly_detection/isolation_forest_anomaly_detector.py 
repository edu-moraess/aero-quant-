from typing import Optional

import numpy as np

from aeroquant.domain.ports.i_model_repository import IModelRepository

class IsolationForestAnomalyDetector:
    def __init__(self, model_repository: IModelRepository):
        self.model_repository = model_repository

    def detect(self, data: np.ndarray) -> np.ndarray:
        model = self.model_repository.load_model("isolation_forest_anomaly_detector")
        if model is None:
            raise ValueError("Isolation Forest model not found")

        # Placeholder: Lógica real de detecção seria implementada aqui
        anomalies = model.predict(data) == -1
        return anomalies