from typing import Optional

import numpy as np

from aeroquant.domain.ports.i_model_repository import IModelRepository

class Autoencoder:
    def __init__(self, model_repository: IModelRepository):
        self.model_repository = model_repository

    def encode_decode(self, image: np.ndarray) -> np.ndarray:
        model = self.model_repository.load_model("autoencoder")
        if model is None:
            raise ValueError("Autoencoder model not found")

        # Placeholder: Lógica real de codificação/decodificação seria implementada aqui
        return model.predict(image)