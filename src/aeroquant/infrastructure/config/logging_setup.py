import logging
from pathlib import Path
from typing import Optional

def setup_logging(log_file: Optional[str] = None) -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_path = log_dir / (log_file or "aeroquant.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler(),
        ],
    )