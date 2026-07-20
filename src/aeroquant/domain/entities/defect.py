"""Entidade de domínio: Defect — resultado de inspeção visual (Computer Vision)."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class DefectType(str, Enum):
    """Tipos de defeito detectáveis pelo pipeline de Computer Vision."""

    CORROSION = "corrosion"
    CRACK = "crack"
    WEAR = "wear"
    NONE = "none"


class SeverityLevel(str, Enum):
    """Severidade estimada do defeito detectado."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True, slots=True)
class BoundingBox:
    """Caixa delimitadora normalizada (0.0 a 1.0) de um defeito na imagem."""

    x_min: float
    y_min: float
    x_max: float
    y_max: float


@dataclass(frozen=True, slots=True)
class Defect:
    """Defeito identificado em uma imagem de inspeção.

    Attributes:
        image_id: Identificador da imagem inspecionada.
        component_id: Componente ao qual a imagem se refere (se conhecido).
        defect_type: Categoria do defeito.
        bounding_box: Localização do defeito na imagem, se aplicável (detecção).
        confidence: Confiança do modelo em [0.0, 1.0].
        severity: Severidade estimada.
    """

    image_id: str
    component_id: str | None
    defect_type: DefectType
    confidence: float
    severity: SeverityLevel
    bounding_box: BoundingBox | None = None

    def __post_init__(self) -> None:
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"confidence deve estar em [0.0, 1.0], recebido: {self.confidence}")