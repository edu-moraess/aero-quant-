import unittest

from aeroquant.domain.entities.aircraft import Aircraft
from aeroquant.domain.entities.component import Component
from aeroquant.domain.entities.health_state import HealthState

class TestAircraft(unittest.TestCase):
    def setUp(self):
        self.aircraft = Aircraft(id="AIRCRAFT_001", model="Boeing 737")

    def test_add_component(self):
        component = Component(id="engine", name="Engine", aircraft_id="AIRCRAFT_001")
        self.aircraft.add_component(component)
        self.assertEqual(len(self.aircraft.components), 1)
        self.assertEqual(self.aircraft.components[0].id, "engine")

    def test_update_health_state(self):
        new_health = HealthState(health_index=95.0, is_operational=True, last_anomaly="")
        self.aircraft.update_health_state(new_health)
        self.assertEqual(self.aircraft.current_health_state.health_index, 95.0)

if __name__ == "__main__":
    unittest.main()