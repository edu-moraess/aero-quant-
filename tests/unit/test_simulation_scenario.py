import unittest

from aeroquant.domain.entities.simulation_scenario import SimulationScenario

class TestSimulationScenario(unittest.TestCase):
    def setUp(self):
        self.scenario = SimulationScenario(
            id="scenario_001",
            description="Test scenario for fleet degradation",
            parameters={"degradation_rate": 0.1, "noise_std": 0.5},
            aircraft_ids=["AIRCRAFT_001", "AIRCRAFT_002"],
        )

    def test_simulation_scenario_creation(self):
        self.assertEqual(self.scenario.id, "scenario_001")
        self.assertEqual(self.scenario.description, "Test scenario for fleet degradation")
        self.assertEqual(self.scenario.parameters["degradation_rate"], 0.1)
        self.assertEqual(len(self.scenario.aircraft_ids), 2)

if __name__ == "__main__":
    unittest.main()