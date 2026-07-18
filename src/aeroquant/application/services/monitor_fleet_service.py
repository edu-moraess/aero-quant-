from typing import Dict, List

from aeroquant.domain.entities.aircraft import Aircraft
from aeroquant.domain.entities.health_snapshot import HealthSnapshot
from aeroquant.domain.ports.i_sensor_source import ISensorSource
from aeroquant.domain.ports.i_twin_repository import ITwinRepository

class MonitorFleetService:
    def __init__(
        self,
        sensor_source: ISensorSource,
        twin_repository: ITwinRepository,
    ):
        self.sensor_source = sensor_source
        self.twin_repository = twin_repository

    def monitor_fleet(self) -> Dict[str, HealthSnapshot]:
        fleet_data = self.sensor_source.get_fleet_sensor_data()
        twins = self.twin_repository.list_all_twins()

        results = {}
        for aircraft_id, sensor_data in fleet_data.items():
            twin = next((t for t in twins if t.id == aircraft_id), None)
            if twin:
                snapshot = self._generate_health_snapshot(twin, sensor_data)
                results[aircraft_id] = snapshot
        return results

    def _generate_health_snapshot(
        self, aircraft: Aircraft, sensor_data: Dict[str, float]
    ) -> HealthSnapshot:
        component_health = {}
        anomalies = []

        for component in aircraft.components:
            component_id = component.id
            health_index = sensor_data.get(component_id, 100.0)
            component_health[component_id] = health_index

            if health_index < 50.0:
                anomalies.append(f"{component_id}_low_health")

        overall_health = sum(component_health.values()) / len(component_health) if component_health else 100.0
        return HealthSnapshot(
            aircraft_id=aircraft.id,
            timestamp=None,  # TODO: Adicionar timestamp real
            component_health=component_health,
            overall_health=overall_health,
            anomalies=anomalies,
        )