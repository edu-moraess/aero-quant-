from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class SimulationScenario:
    id: str
    description: str
    parameters: Dict[str, float]
    aircraft_ids: Optional[List[str]] = None