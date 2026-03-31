# src/analysis/sales_analyzer.py

from typing import Dict, Optional
import pandas as pd
import logging

logger = logging.getLogger(__name__)


class SalesAnalyzer:
    """Handles sales data analysis operations."""

    def __init__(self, dataframe: pd.DataFrame):
        if dataframe is None or dataframe.empty:
            raise ValueError("DataFrame cannot be empty")

        self.df = dataframe.copy()

    def calculate_basic_stats(self) -> Dict[str, float]:
        """Return key sales metrics."""
        try:
            stats = {
                "total_sales": float(self.df["total_amount"].sum()),
                "average_order": float(self.df["total_amount"].mean()),
                "total_orders": int(len(self.df)),
                "unique_customers": int(self.df["customer_id"].nunique()),
                "unique_products": int(self.df["product_id"].nunique()),
            }

            if "order_date" in self.df.columns:
                stats["start_date"] = self.df["order_date"].min()
                stats["end_date"] = self.df["order_date"].max()

            return stats

        except KeyError as e:
            logger.error(f"Missing column: {e}")
            raise
