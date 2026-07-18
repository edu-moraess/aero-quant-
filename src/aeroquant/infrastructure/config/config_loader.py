import yaml
from pathlib import Path
from typing import Any, Dict

class ConfigLoader:
    _instance = None
    _configs = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_config(self, config_name: str) -> Dict[str, Any]:
        if config_name in self._configs:
            return self._configs[config_name]

        config_path = Path(f"configs/{config_name}.yaml")
        if not config_path.exists():
            raise FileNotFoundError(f"Config file {config_name}.yaml not found")

        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            self._configs[config_name] = config
            return config