import unittest

from aeroquant.domain.entities.health_state import HealthState

class TestHealthState(unittest.TestCase):
    def setUp(self):
        self.health_state = HealthState(health_index=85.0, is_operational=True, last_anomaly="")

    def test_health_state_creation(self):
        self.assertEqual(self.health_state.health_index, 85.0)
        self.assertTrue(self.health_state.is_operational)
        self.assertEqual(self.health_state.last_anomaly, "")

if __name__ == "__main__":
    unittest.main()