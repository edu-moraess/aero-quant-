import numpy as np
from typing import Optional

def gaussian_noise(mean: float = 0.0, std: float = 1.0, seed: Optional[int] = None) -> float:
    rng = np.random.default_rng(seed)
    return rng.normal(mean, std)

def random_walk_degradation(
    initial_value: float,
    drift: float,
    volatility: float,
    steps: int,
    seed: Optional[int] = None,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    walk = np.zeros(steps)
    walk[0] = initial_value
    for i in range(1, steps):
        walk[i] = walk[i - 1] + drift + rng.normal(0, volatility)
    return walk

def degradation_to_health_index(degradation: float, max_degradation: float = 100.0) -> float:
    return max(0.0, min(100.0, max_degradation - degradation))

def transient_anomaly(
    base_value: float,
    severity: float,
    duration: int,
    current_step: int,
    seed: Optional[int] = None,
) -> float:
    rng = np.random.default_rng(seed)
    if current_step < duration:
        return base_value + rng.normal(-severity, severity / 2)
    return base_value