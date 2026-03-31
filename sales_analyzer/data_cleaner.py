# src/data/cleaner.py

import pandas as pd


class DataCleaner:
    """Handles data cleaning operations."""

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        df = df.drop_duplicates()

        # Fill numeric columns
        numeric_cols = df.select_dtypes(include="number").columns
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].median())

        # Fill categorical columns
        cat_cols = df.select_dtypes(include="object").columns
        for col in cat_cols:
            df[col] = df[col].fillna(df[col].mode()[0])

        return df

