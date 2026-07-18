from dataclasses import dataclass
from datetime import datetime

@dataclass
class RULEstimate:
    component_id: str
    aircraft_id: str
    timestamp: datetime
    estimated_rul: float
    confidence: float