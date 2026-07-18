from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.aircraft import Aircraft

class ITwinRepository(ABC):
    @abstractmethod
    def save_twin(self, aircraft: Aircraft) -> bool:
        pass

    @abstractmethod
    def load_twin(self, aircraft_id: str) -> Optional[Aircraft]:
        pass

    @abstractmethod
    def list_all_twins(self) -> List[Aircraft]:
        pass