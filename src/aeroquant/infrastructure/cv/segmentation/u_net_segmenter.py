from typing import Optional

import numpy as np

from aeroquant.domain.ports.i_model_repository import IModelRepository

class UNetSegmenter:
    def __init__(self, model_repository: IModelRepository):
        self.model_repository = model_repository

    def segment(self, image: np.ndarray) -> np.ndarray:
        model = self.model_repository.load_model("u_net_segmenter")
        if model is None:
            raise ValueError("U-Net model not found")

        # Placeholder: Lógica real de segmentação seria implementada aqui
        return model.predict(image)