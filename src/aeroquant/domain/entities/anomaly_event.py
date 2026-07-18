from dataclasses import dataclass
from datetime import datetime

@dataclass
class AnomalyEvent:
    id: str
    component_id: str
    aircraft_id: str
    timestamp: datetime
    severity: float
    description: str