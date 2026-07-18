from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class HealthSnapshot:
    aircraft_id: str
    timestamp: datetime
    component_health: Dict[str, float]
    overall_health: float
    anomalies: List[str]