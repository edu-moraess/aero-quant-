import unittest
from datetime import datetime

from aeroquant.domain.entities.rul_estimate import RULEstimate

class TestRULEstimate(unittest.TestCase):
    def setUp(self):
        self.rul_estimate = RULEstimate(
            component_id="engine",
            aircraft_id="AIRCRAFT_001",
            timestamp=datetime.now(),
            estimated_rul=150.0,
            confidence=0.95,
        )

    def test_rul_estimate_creation(self):
        self.assertEqual(self.rul_estimate.component_id, "engine")
        self.assertEqual(self.rul_estimate.aircraft_id, "AIRCRAFT_001")
        self.assertEqual(self.rul_estimate.estimated_rul, 150.0)
        self.assertEqual(self.rul_estimate.confidence, 0.95)

if __name__ == "__main__":
    unittest.main()