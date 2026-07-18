import unittest
from datetime import datetime

from aeroquant.domain.entities.simulation_result import SimulationResult

class TestSimulationResult(unittest.TestCase):
    def setUp(self):
        self.result = SimulationResult(
            scenario_id="scenario_001",
            timestamp=datetime.now(),
            aircraft_results={
                "AIRCRAFT_001": {"engine": 90.0, "wing": 85.0},
                "AIRCRAFT_002": {"engine": 95.0, "wing": 80.0},
            },
            fleet_health_trend=[90.0, 85.0, 80.0],
        )

    def test_simulation_result_creation(self):
        self.assertEqual(self.result.scenario_id, "scenario_001")
        self.assertEqual(self.result.aircraft_results["AIRCRAFT_001"]["engine"], 90.0)
        self.assertEqual(len(self.result.fleet_health_trend), 3)

if __name__ == "__main__":
    unittest.main()