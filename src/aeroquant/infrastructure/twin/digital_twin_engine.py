from datetime import datetime
from typing import Dict, List, Optional

from aeroquant.domain.entities.aircraft import Aircraft
from aeroquant.domain.entities.anomaly_event import AnomalyEvent
from aeroquant.domain.entities.defect import Defect
from aeroquant.domain.entities.health_snapshot import HealthSnapshot
from aeroquant.domain.entities.health_state import HealthState
from aeroquant.domain.entities.rul_estimate import RULEstimate
from aeroquant.domain.ports.i_sensor_source import ISensorSource
from aeroquant.domain.ports.i_twin_repository import ITwinRepository

class DigitalTwinEngine:
    def __init__(
        self,
        sensor_source: ISensorSource,
        twin_repository: ITwinRepository,
    ):
        self.sensor_source = sensor_source
        self.twin_repository = twin_repository

    def update_twin(self, aircraft_id: str) -> Optional[Aircraft]:
        sensor_data = self.sensor_source.get_sensor_data(aircraft_id)
        twin = self.twin_repository.load_twin(aircraft_id)

        if twin is None:
            return None

        for component in twin.components:
            component_id = component.id
            if component_id in sensor_data:
                health_index = sensor_data[component_id]
                component.current_health = HealthState(
                    health_index=health_index,
                    is_operational=health_index > 30.0,
                    last_anomaly="" if health_index > 30.0 else f"{component_id}_low_health",
                )

        twin.current_health_state = self._calculate_overall_health(twin)
        self.twin_repository.save_twin(twin)
        return twin

    def _calculate_overall_health(self, aircraft: Aircraft) -> HealthState:
        health_indices = [c.current_health.health_index for c in aircraft.components]
        overall_health = sum(health_indices) / len(health_indices) if health_indices else 100.0
        return HealthState(
            health_index=overall_health,
            is_operational=overall_health > 30.0,
            last_anomaly="" if overall_health > 30.0 else "overall_low_health",
        )

    def detect_anomalies(self, aircraft_id: str) -> List[AnomalyEvent]:
        twin = self.twin_repository.load_twin(aircraft_id)
        if twin is None:
            return []

        anomalies = []
        for component in twin.components:
            if not component.current_health.is_operational:
                anomalies.append(
                    AnomalyEvent(
                        id=f"{aircraft_id}_{component.id}_anomaly",
                        component_id=component.id,
                        aircraft_id=aircraft_id,
                        timestamp=datetime.now(),
                        severity=100.0 - component.current_health.health_index,
                        description=f"Low health in {component.id}",
                    )
                )
        return anomalies

    def estimate_rul(self, aircraft_id: str, component_id: str) -> Optional[RULEstimate]:
        twin = self.twin_repository.load_twin(aircraft_id)
        if twin is None:
            return None

        component = next((c for c in twin.components if c.id == component_id), None)
        if component is None:
            return None

        # Placeholder: Lógica real de estimativa de RUL seria implementada aqui
        estimated_rul = 100.0  # Valor fictício
        confidence = 0.95  # Valor fictício

        return RULEstimate(
            component_id=component_id,
            aircraft_id=aircraft_id,
            timestamp=datetime.now(),
            estimated_rul=estimated_rul,
            confidence=confidence,
        )

    def diagnose_defect(self, aircraft_id: str, component_id: str) -> Optional[Defect]:
        twin = self.twin_repository.load_twin(aircraft_id)
        if twin is None:
            return None

        component = next((c for c in twin.components if c.id == component_id), None)
        if component is None or component.current_health.is_operational:
            return None

        return Defect(
            id=f"{aircraft_id}_{component_id}_defect",
            component_id=component_id,
            aircraft_id=aircraft_id,
            timestamp=datetime.now(),
            description=f"Defect in {component.id}",
            severity=100.0 - component.current_health.health_index,
        )