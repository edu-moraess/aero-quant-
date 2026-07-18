import unittest
from datetime import datetime

from aeroquant.domain.entities.anomaly_event import AnomalyEvent

class TestAnomalyEvent(unittest.TestCase):
    def setUp(self):
        self.anomaly = AnomalyEvent(
            id="anomaly_001",
            component_id="engine",
            aircraft_id="AIRCRAFT_001",
            timestamp=datetime.now(),
            severity=0.8,
            description="High temperature detected",
        )

    def test_anomaly_event_creation(self):
        self.assertEqual(self.anomaly.id, "anomaly_001")
        self.assertEqual(self.anomaly.component_id, "engine")
        self.assertEqual(self.anomaly.aircraft_id, "AIRCRAFT_001")
        self.assertEqual(self.anomaly.severity, 0.8)
        self.assertEqual(self.anomaly.description, "High temperature detected")

if __name__ == "__main__":
    unittest.main()