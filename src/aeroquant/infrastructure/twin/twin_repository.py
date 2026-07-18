from typing import List, Optional

from aeroquant.domain.entities.aircraft import Aircraft
from aeroquant.domain.ports.i_twin_repository import ITwinRepository

class TwinRepository(ITwinRepository):
    def __init__(self):
        self._twins: Dict[str, Aircraft] = {}

    def save_twin(self, aircraft: Aircraft) -> bool:
        self._twins[aircraft.id] = aircraft
        return True

    def load_twin(self, aircraft_id: str) -> Optional[Aircraft]:
        return self._twins.get(aircraft_id)

    def list_all_twins(self) -> List[Aircraft]:
        return list(self._twins.values())