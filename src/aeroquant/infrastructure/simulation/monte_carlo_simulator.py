from dataclasses import dataclass
from typing import Dict, List

import numpy as np

from aeroquant.domain.entities.simulation_scenario import SimulationScenario
from aeroquant.domain.entities.simulation_result import SimulationResult

@dataclass
class MonteCarloConfig:
    num_simulations: int = 1000
    time_horizon: int = 100

class MonteCarloSimulator:
    def __init__(self, config: MonteCarloConfig):
        self.config = config

    def simulate(self, scenario: SimulationScenario) -> SimulationResult:
        # Placeholder: Lógica real de simulação seria implementada aqui
        num_aircraft = len(scenario.aircraft_ids) if scenario.aircraft_ids else 1
        fleet_health_trend = np.random.rand(self.config.time_horizon) * 100
        aircraft_results = {
            aid: {f"component_{i}": np.random.rand() * 100 for i in range(3)}
            for aid in (scenario.aircraft_ids or ["default"])
        }

        return SimulationResult(
            scenario_id=scenario.id,
            timestamp=None,  # TODO: Adicionar timestamp real
            aircraft_results=aircraft_results,
            fleet_health_trend=fleet_health_trend.tolist(),
        )