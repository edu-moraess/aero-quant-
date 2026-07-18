import unittest

from aeroquant.domain.entities.aircraft import Aircraft
from aeroquant.domain.entities.component import Component
from aeroquant.infrastructure.sensors.sensor_data_generator import SensorDataGenerator, SensorConfig
from aeroquant.infrastructure.twin.digital_twin_engine import DigitalTwinEngine
from aeroquant.infrastructure.twin.twin_repository import TwinRepository

class TestSensorToTwinIntegration(unittest.TestCase):
    def setUp(self):
        self.twin_repository = TwinRepository()
        self.sensor_configs = [
            SensorConfig(
                name="engine_temp",
                base_value=75.0,
                degradation_rate=0.1,
                noise_std=2.0,
                anomaly_probability=0.01,
                anomaly_severity=20.0,
            ),
        ]
        self.generator = SensorDataGenerator(
            aircraft_ids=["AIRCRAFT_001"],
            sensor_configs=self.sensor_configs,
            seed=42,
        )
        self.engine = DigitalTwinEngine(self.generator, self.twin_repository)

        aircraft = Aircraft(id="AIRCRAFT_001", model="Boeing 737")
        aircraft.add_component(Component(id="engine_temp", name="Engine Temp", aircraft_id="AIRCRAFT_001"))
        self.twin_repository.save_twin(aircraft)

    def test_sensor_to_twin_integration(self):
        updated_twin = self.engine.update_twin("AIRCRAFT_001")
        self.assertIsNotNone(updated_twin)
        self.assertEqual(updated_twin.id, "AIRCRAFT_001")
        self.assertGreater(updated_twin.components[0].current_health.health_index, 0.0)

if __name__ == "__main__":
    unittest.main()