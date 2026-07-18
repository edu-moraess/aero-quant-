from typing import Optional

import numpy as np

from aeroquant.domain.ports.i_model_repository import IModelRepository

class ViTClassifier:
    def __init__(self, model_repository: IModelRepository):
        self.model_repository = model_repository

    def predict(self, image: np.ndarray) -> int:
        model = self.model_repository.load_model("vit_classifier")
        if model is None:
            raise ValueError("ViT model not found")

        # Placeholder: Lógica real de classificação seria implementada aqui
        return model.predict(image)