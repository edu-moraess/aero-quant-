import unittest

from aeroquant.domain.entities.component import Component
from aeroquant.domain.entities.health_state import HealthState

class TestComponent(unittest.TestCase):
    def setUp(self):
        self.component = Component(
            id="engine",
            name="Engine",
            aircraft_id="AIRCRAFT_001",
            current_health=HealthState(health_index=100.0),
        )

    def test_component_creation(self):
        self.assertEqual(self.component.id, "engine")
        self.assertEqual(self.component.name, "Engine")
        self.assertEqual(self.component.aircraft_id, "AIRCRAFT_001")
        self.assertEqual(self.component.current_health.health_index, 100.0)

if __name__ == "__main__":
    unittest.main()