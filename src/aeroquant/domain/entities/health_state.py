"""Entidades de domínio relacionadas ao estado de saúde do Digital Twin."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class RiskLevel(str, Enum):
    """Nível de risco operacional derivado do Health Index e da incerteza de RUL."""

    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True, slots=True)
class RULEstimate:
    """Estimativa probabilística de Remaining Useful Life (RUL).

    Expressa em ciclos de voo restantes, com percentis para refletir incerteza
    (tipicamente alimentados pelo Simulation Engine / Monte Carlo).
    """

    p10_cycles: float
    p50_cycles: float
    p90_cycles: float
    generated_at: datetime

    def __post_init__(self) -> None:
        if not (self.p10_cycles <= self.p50_cycles <= self.p90_cycles):
            raise ValueError("RULEstimate requer p10 <= p50 <= p90")


@dataclass(frozen=True, slots=True)
class HealthSnapshot:
    """Snapshot imutável do estado de saúde em um instante — usado para histórico/auditoria."""

    health_index: float
    risk_level: RiskLevel
    timestamp: datetime
    rul_estimate: RULEstimate | None = None


@dataclass(slots=True)
class HealthState:
    """Estado vivo (mutável em memória, mas versionado via histórico) de uma aeronave.

    Attributes:
        aircraft_id: Identificador da aeronave.
        health_index: Índice de saúde agregado em [0.0, 1.0] (1.0 = saúde perfeita).
        risk_level: Classificação de risco operacional corrente.
        rul_estimate: Última estimativa de RUL, se disponível.
        last_updated: Timestamp da última atualização.
        history: Lista de snapshots imutáveis, em ordem cronológica.
    """

    aircraft_id: str
    health_index: float = 1.0
    risk_level: RiskLevel = RiskLevel.LOW
    rul_estimate: RULEstimate | None = None
    last_updated: datetime = field(default_factory=datetime.utcnow)
    history: list[HealthSnapshot] = field(default_factory=list)

    def record_snapshot(self) -> None:
        """Registra o estado atual como um snapshot imutável no histórico."""
        self.history.append(
            HealthSnapshot(
                health_index=self.health_index,
                risk_level=self.risk_level,
                timestamp=self.last_updated,
                rul_estimate=self.rul_estimate,
            )
        )

    @staticmethod
    def classify_risk(health_index: float) -> RiskLevel:
        """Classifica o risco operacional a partir do Health Index.

        Limiares definidos para fins de pesquisa/demonstração:
            >= 0.75 -> LOW
            >= 0.50 -> MODERATE
            >= 0.25 -> HIGH
            <  0.25 -> CRITICAL
        """
        if health_index >= 0.75:
            return RiskLevel.LOW
        if health_index >= 0.50:
            return RiskLevel.MODERATE
        if health_index >= 0.25:
            return RiskLevel.HIGH
        return RiskLevel.CRITICAL