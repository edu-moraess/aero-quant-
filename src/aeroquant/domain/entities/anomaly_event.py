"""Entidade de domínio: AnomalyEvent."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class AnomalyMethod(str, Enum):
    """Método de detecção que originou o evento de anomalia."""

    ISOLATION_FOREST = "isolation_forest"
    ONE_CLASS_SVM = "one_class_svm"
    AUTOENCODER = "autoencoder"


@dataclass(frozen=True, slots=True)
class AnomalyEvent:
    """Evento de anomalia detectado em sinais de sensores.

    Attributes:
        aircraft_id: Aeronave associada ao evento.
        timestamp: Momento da leitura que originou o evento.
        score: Score de anomalia (quanto maior, mais anômalo); escala depende do método.
        method: Algoritmo que gerou a detecção.
        features_involved: Lista de sensores/features que mais contribuíram para o score.
    """

    aircraft_id: str
    timestamp: datetime
    score: float
    method: AnomalyMethod
    features_involved: tuple[str, ...] = field(default_factory=tuple)