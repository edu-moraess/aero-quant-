from typing import Dict, List

from aeroquant.domain.entities.anomaly_event import AnomalyEvent
from aeroquant.domain.ports.i_model_repository import IModelRepository
from aeroquant.domain.ports.i_sensor_source import ISensorSource

class DetectAnomaliesService:
    def __init__(
        self,
        sensor_source: ISensorSource,
        model_repository: IModelRepository,
    ):
        self.sensor_source = sensor_source
        self.model_repository = model_repository

    def detect_anomalies(self, aircraft_id: str) -> List[AnomalyEvent]:
        sensor_data = self.sensor_source.get_sensor_data(aircraft_id)
        model = self.model_repository.load_model("anomaly_detection")

        anomalies = []
        if model is not None:
            for component_id, value in sensor_data.items():
                # Placeholder: Lógica real de detecção seria implementada aqui
                is_anomaly = value < 30.0  # Limiar fictício
                if is_anomaly:
                    anomalies.append(
                        AnomalyEvent(
                            id=f"{aircraft_id}_{component_id}_anomaly",
                            component_id=component_id,
                            aircraft_id=aircraft_id,
                            timestamp=None,  # TODO: Adicionar timestamp real
                            severity=100.0 - value,
                            description=f"Low value detected in {component_id}",
                        )
                    )
        return anomalies