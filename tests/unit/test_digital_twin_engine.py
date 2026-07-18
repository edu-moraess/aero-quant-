import unittest
from datetime import datetime

from aeroquant.domain.entities.aircraft import Aircraft
from aeroquant.domain.entities.component import Component
from aeroquant.domain.entities.health_state import HealthState
from aeroquant.infrastructure.twin.digital_twin_engine import DigitalTwinEngine
from aeroquant.infrastructure.twin.twin_repository import TwinRepository

class MockSensorSource:
    def get_sensor_data(self, aircraft_id: str):
        return {"engine": 80.0, "wing": 90.0}

    def get_fleet_sensor_data(self):
        return {"AIRCRAFT_001": {"engine": 80.0, "wing": 90.0}}

class TestDigitalTwinEngine(unittest.TestCase):
    def setUp(self):
        self.twin_repository = TwinRepository()
        self.sensor_source = MockSensorSource()
        self.engine = DigitalTwinEngine(self.sensor_source, self.twin_repository)

        aircraft = Aircraft(id="AIRCRAFT_001", model="Boeing 737")
        aircraft.add_component(Component(id="engine", name="Engine", aircraft_id="AIRCRAFT_001"))
        aircraft.add_component(Component(id="wing", name="Wing", aircraft_id="AIRCRAFT_001"))
        self.twin_repository.save_twin(aircraft)

    def test_update_twin(self):
        twin = self.engine.update_twin("AIRCRAFT_001")
        self.assertIsNotNone(twin)
        self.assertEqual(twin.id, "AIRCRAFT_001")
        self.assertEqual(twin.components[0].current_health.health_index, 80.0)

    def test_detect_anomalies(self):
        anomalies = self.engine.detect_anomalies("AIRCRAFT_001")
        self.assertEqual(len(anomalies), 0)

if __name__ == "__main__":
    unittest.main()