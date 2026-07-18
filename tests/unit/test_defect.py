import unittest
from datetime import datetime

from aeroquant.domain.entities.defect import Defect

class TestDefect(unittest.TestCase):
    def setUp(self):
        self.defect = Defect(
            id="defect_001",
            component_id="engine",
            aircraft_id="AIRCRAFT_001",
            timestamp=datetime.now(),
            description="Oil leak detected",
            severity=0.9,
            estimated_repair_time=2.5,
        )

    def test_defect_creation(self):
        self.assertEqual(self.defect.id, "defect_001")
        self.assertEqual(self.defect.component_id, "engine")
        self.assertEqual(self.defect.aircraft_id, "AIRCRAFT_001")
        self.assertEqual(self.defect.severity, 0.9)
        self.assertEqual(self.defect.estimated_repair_time, 2.5)

if __name__ == "__main__":
    unittest.main()