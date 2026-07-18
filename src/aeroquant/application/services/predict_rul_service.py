from typing import Dict, Optional

from aeroquant.domain.entities.rul_estimate import RULEstimate
from aeroquant.domain.ports.i_model_repository import IModelRepository
from aeroquant.domain.ports.i_sensor_source import ISensorSource

class PredictRULService:
    def __init__(
        self,
        sensor_source: ISensorSource,
        model_repository: IModelRepository,
    ):
        self.sensor_source = sensor_source
        self.model_repository = model_repository

    def predict_rul(self, aircraft_id: str, component_id: str) -> Optional[RULEstimate]:
        sensor_data = self.sensor_source.get_sensor_data(aircraft_id)
        model = self.model_repository.load_model(f"rul_{component_id}")

        if model is None or component_id not in sensor_data:
            return None

        # Placeholder: Lógica real de predição seria implementada aqui
        estimated_rul = 100.0  # Valor fictício
        confidence = 0.95  # Valor fictício

        return RULEstimate(
            component_id=component_id,
            aircraft_id=aircraft_id,
            timestamp=None,  # TODO: Adicionar timestamp real
            estimated_rul=estimated_rul,
            confidence=confidence,
        )