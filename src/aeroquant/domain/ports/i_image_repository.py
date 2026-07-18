from abc import ABC, abstractmethod
from typing import Optional

import numpy as np

class IImageRepository(ABC):
    @abstractmethod
    def save_image(self, image: np.ndarray, path: str) -> bool:
        pass

    @abstractmethod
    def load_image(self, path: str) -> Optional[np.ndarray]:
        pass