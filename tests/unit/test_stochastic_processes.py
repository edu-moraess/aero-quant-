import unittest

import numpy as np

from aeroquant.infrastructure.sensors.stochastic_processes import (
    gaussian_noise,
    random_walk_degradation,
    degradation_to_health_index,
    transient_anomaly,
)

class TestStochasticProcesses(unittest.TestCase):
    def test_gaussian_noise(self):
        noise = gaussian_noise(mean=0.0, std=1.0, seed=42)
        self.assertIsInstance(noise, float)

    def test_random_walk_degradation(self):
        walk = random_walk_degradation(
            initial_value=100.0,
            drift=-0.1,
            volatility=0.5,
            steps=10,
            seed=42,
        )
        self.assertEqual(len(walk), 10)
        self.assertIsInstance(walk, np.ndarray)

    def test_degradation_to_health_index(self):
        health = degradation_to_health_index(degradation=20.0, max_degradation=100.0)
        self.assertEqual(health, 80.0)

    def test_transient_anomaly(self):
        anomaly = transient_anomaly(
            base_value=50.0,
            severity=10.0,
            duration=5,
            current_step=2,
            seed=42,
        )
        self.assertIsInstance(anomaly, float)

if __name__ == "__main__":
    unittest.main()