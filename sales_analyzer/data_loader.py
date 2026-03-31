# src/data/loader.py

import pandas as pd
from pathlib import Path


class DataLoader:
    """Handles loading of datasets."""

    @staticmethod
    def load_csv(file_path: str) -> pd.DataFrame:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} not found")

        return pd.read_csv(path)

