"""Entidades de domínio para o Simulation Engine (Monte Carlo)."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class SimulationResult:
    """Resultado agregado de uma simulação de Monte Carlo.

    Attributes:
        rul_p10: Percentil 10 de RUL simulado (ciclos).
        rul_p50: Percentil 50 (mediana).
        rul_p90: Percentil 90.
        failure_probability_within_horizon: Probabilidade de falha dentro do horizonte
            simulado, estimada pela fração de trajetórias que atingem degradação máxima.
        num_runs: Número de réplicas de Monte Carlo executadas.
    """

    rul_p10: float
    rul_p50: float
    rul_p90: float
    failure_probability_within_horizon: float
    num_runs: int


@dataclass(frozen=True, slots=True)
class SimulationScenario:
    """Cenário de simulação de degradação para uma aeronave/componente.

    Attributes:
        scenario_id: Identificador do cenário.
        aircraft_id: Aeronave-alvo da simulação.
        initial_degradation: Degradação inicial em [0.0, 1.0].
        horizon_cycles: Horizonte de simulação em ciclos de voo.
        num_runs: Quantidade de réplicas de Monte Carlo.
        parameters: Parâmetros adicionais (drift, volatilidade, prob. de choque, etc.).
    """

    scenario_id: str
    aircraft_id: str
    initial_degradation: float
    horizon_cycles: int
    num_runs: int = 1000
    parameters: dict = field(default_factory=dict)