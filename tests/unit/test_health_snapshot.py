import unittest
from datetime import datetime

from aeroquant.domain.entities.health_snapshot import HealthSnapshot

class TestHealthSnapshot(unittest.TestCase):
    def setUp(self):
        self.snapshot = HealthSnapshot(
            aircraft_id="AIRCRAFT_001",
            timestamp=datetime.now(),
            component_health={"engine": 90.0, "wing": 85.0},
            overall_health=87.5,
            anomalies=[],
        )

    def test_health_snapshot_creation(self):
        self.assertEqual(self.snapshot.aircraft_id, "AIRCRAFT_001")
        self.assertEqual(self.snapshot.overall_health, 87.5)
        self.assertEqual(self.snapshot.component_health["engine"], 90.0)
        self.assertEqual(len(self.snapshot.anomalies), 0)

if __name__ == "__main__":
    unittest.main()