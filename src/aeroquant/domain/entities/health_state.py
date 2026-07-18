from dataclasses import dataclass

@dataclass
class HealthState:
    health_index: float = 100.0
    is_operational: bool = True
    last_anomaly: str = ""