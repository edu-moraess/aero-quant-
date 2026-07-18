from typing import Any, Dict, Optional

from aeroquant.domain.ports.i_model_repository import IModelRepository

class ModelRepository(IModelRepository):
    def __init__(self):
        self._models: Dict[str, Any] = {}

    def save_model(self, model: Any, model_name: str) -> bool:
        self._models[model_name] = model
        return True

    def load_model(self, model_name: str) -> Optional[Any]:
        return self._models.get(model_name)