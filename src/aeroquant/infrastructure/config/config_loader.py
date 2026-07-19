"""Carregador centralizado de configuração a partir de arquivos YAML.

Uso:
    from aeroquant.infrastructure.config.config_loader import ConfigLoader

    config = ConfigLoader.load("configs/base.yaml")
    seed = config["random_seed"]

    sensors_cfg = ConfigLoader.load("configs/sensors.yaml")
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class ConfigLoadError(RuntimeError):
    """Erro ao carregar ou validar um arquivo de configuração."""


class ConfigLoader:
    """Carrega e faz cache de arquivos de configuração YAML.

    Cache implementado manualmente em um dicionário de classe (em vez de
    decorators empilhados como ``@staticmethod`` + ``@functools.lru_cache``),
    para evitar armadilhas de indentação/versão de Python ao copiar este
    arquivo entre ambientes.
    """

    _cache: dict[str, dict[str, Any]] = {}

    @staticmethod
    def load(path: str) -> dict[str, Any]:
        """Carrega um arquivo YAML e retorna seu conteúdo como dicionário.

        Args:
            path: Caminho relativo ou absoluto para o arquivo YAML.

        Returns:
            Dicionário com o conteúdo do arquivo.

        Raises:
            ConfigLoadError: Se o arquivo não existir ou não for um YAML válido.
        """
        if path in ConfigLoader._cache:
            return ConfigLoader._cache[path]

        file_path = Path(path)
        if not file_path.exists():
            raise ConfigLoadError(f"Arquivo de configuração não encontrado: {path}")

        try:
            with file_path.open("r", encoding="utf-8") as f:
                content = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            raise ConfigLoadError(f"YAML inválido em {path}: {exc}") from exc

        if not isinstance(content, dict):
            raise ConfigLoadError(f"Conteúdo de {path} deve ser um mapeamento (dict) no topo")

        ConfigLoader._cache[path] = content
        return content

    @staticmethod
    def clear_cache() -> None:
        """Limpa o cache de configurações carregadas (útil em testes)."""
        ConfigLoader._cache.clear()