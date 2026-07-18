from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from aeroquant.domain.entities.aircraft import Aircraft
from aeroquant.domain.ports.i_sensor_source import ISensorSource

@dataclass
class SensorConfig:
    name: str
    base_value: float
    degradation_rate: float
    noise_std: float
    anomaly_probability: float
    anomaly_severity: float

class SensorDataGenerator(ISensorSource):
    def __init__(
        self,
        aircraft_ids: List[str],
        sensor_configs: List[SensorConfig],
        seed: Optional[int] = None,
    ):
        self.aircraft_ids = aircraft_ids
        self.sensor_configs = sensor_configs
        self.seed = seed
        self._rng = np.random.default_rng(seed)
        self._time = 0

    def get_sensor_data(self, aircraft_id: str) -> Dict[str, float]:
        if aircraft_id not in self.aircraft_ids:
            return {}

        sensor_data = {}
        for config in self.sensor_configs:
            base_value = config.base_value
            degradation = self._degradation(config)
            noise = self._noise(config)
            anomaly = self._anomaly(config)

            value = base_value + degradation + noise + anomaly
            sensor_data[config.name] = max(0.0, min(100.0, value))

        return sensor_data

    def get_fleet_sensor_data(self) -> Dict[str, Dict[str, float]]:
        return {aid: self.get_sensor_data(aid) for aid in self.aircraft_ids}

    def _degradation(self, config: SensorConfig) -> float:
        return self._rng.normal(0, config.degradation_rate) * self._time

    def _noise(self, config: SensorConfig) -> float:
        return self._rng.normal(0, config.noise_std)

    def _anomaly(self, config: SensorConfig) -> float:
        if self._rng.random() < config.anomaly_probability:
            return self._rng.normal(-config.anomaly_severity, config.anomaly_severity / 2)
        return 0.0

    def advance_time(self) -> None:
        self._time += 1