import unittest

import numpy as np

from aeroquant.infrastructure.sensors.sensor_data_generator import SensorDataGenerator, SensorConfig

class TestSensorDataGenerator(unittest.TestCase):
    def setUp(self):
        self.sensor_configs = [
            SensorConfig(
                name="sensor1",
                base_value=50.0,
                degradation_rate=0.1,
                noise_std=1.0,
                anomaly_probability=0.01,
                anomaly_severity=10.0,
            ),
        ]
        self.generator = SensorDataGenerator(
            aircraft_ids=["AIRCRAFT_001"],
            sensor_configs=self.sensor_configs,
            seed=42,
        )

    def test_generate_sensor_data(self):
        data = self.generator.get_sensor_data("AIRCRAFT_001")
        self.assertIn("sensor1", data)
        self.assertIsInstance(data["sensor1"], float)

    def test_advance_time(self):
        initial_data = self.generator.get_sensor_data("AIRCRAFT_001")
        self.generator.advance_time()
        new_data = self.generator.get_sensor_data("AIRCRAFT_001")
        self.assertNotEqual(initial_data["sensor1"], new_data["sensor1"])

if __name__ == "__main__":
    unittest.main()