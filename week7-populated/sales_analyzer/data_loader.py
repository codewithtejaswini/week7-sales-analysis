"""Data loader module.
Load sales data from CSV files with validation."""
import pandas as pd
import logging
from typing import Optional
from pathlib import Path

logger = logging.getLogger(__name__)

def load_sales_data(file_path: str | Path) -> Optional[pd.DataFrame]:
    """
    Load sales data from CSV file.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        DataFrame with sales data or None if failed
        
    Raises:
        FileNotFoundError: If CSV file not found
        pd.errors.EmptyDataError: If CSV is empty
    """
    try:
        logger.info(f"Loading data from {file_path}")
        df = pd.read_csv(file_path)
        
        expected_columns = ['date', 'product', 'quantity', 'price', 'region']
        if not all(col in df.columns for col in expected_columns):
            missing = [col for col in expected_columns if col not in df.columns]
            raise ValueError(f"Missing required columns: {missing}")
        
        # Basic validation
        if df.empty:
            raise pd.errors.EmptyDataError("CSV file is empty")
        
        if len(df) < 10:
            logger.warning("Dataset has few records")
        
        logger.info(f"Data loaded successfully. Shape: {df.shape}")
        logger.info(f"Columns: {list(df.columns)}")
        
        return df
        
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return None

