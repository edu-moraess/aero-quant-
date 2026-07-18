from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Defect:
    id: str
    component_id: str
    aircraft_id: str
    timestamp: datetime
    description: str
    severity: float
    estimated_repair_time: Optional[float] = None