from abc import ABC, abstractmethod
from typing import Any, Optional

class IModelRepository(ABC):
    @abstractmethod
    def save_model(self, model: Any, model_name: str) -> bool:
        pass

    @abstractmethod
    def load_model(self, model_name: str) -> Optional[Any]:
        pass