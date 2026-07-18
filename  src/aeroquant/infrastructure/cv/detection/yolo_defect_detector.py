from typing import Optional

import numpy as np

from aeroquant.domain.ports.i_model_repository import IModelRepository

class YOLODefectDetector:
    def __init__(self, model_repository: IModelRepository):
        self.model_repository = model_repository

    def detect(self, image: np.ndarray) -> np.ndarray:
        model = self.model_repository.load_model("yolo_defect_detector")
        if model is None:
            raise ValueError("YOLO model not found")

        # Placeholder: Lógica real de detecção seria implementada aqui
        return model.predict(image)