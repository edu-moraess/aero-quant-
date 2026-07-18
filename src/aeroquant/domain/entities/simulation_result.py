from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class SimulationResult:
    scenario_id: str
    timestamp: datetime
    aircraft_results: Dict[str, Dict[str, float]]
    fleet_health_trend: List[float]