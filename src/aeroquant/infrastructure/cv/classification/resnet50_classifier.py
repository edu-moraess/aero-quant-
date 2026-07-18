from typing import Optional

import numpy as np

from aeroquant.domain.ports.i_model_repository import IModelRepository

class ResNet50Classifier:
    def __init__(self, model_repository: IModelRepository):
        self.model_repository = model_repository

    def predict(self, image: np.ndarray) -> int:
        model = self.model_repository.load_model("resnet50_classifier")
        if model is None:
            raise ValueError("ResNet50 model not found")

        # Placeholder: Lógica real de classificação seria implementada aqui
        return model.predict(image)