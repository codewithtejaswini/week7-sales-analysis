"""Data cleaner module.
Clean and preprocess sales data."""
import pandas as pd
import numpy as np
import logging
from typing import Optional
from pathlib import Path

logger = logging.getLogger(__name__)

class DataCleaner:
    """Class for cleaning sales data."""
    
    @staticmethod
    def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean sales data: remove duplicates, handle missing values,
        fix data types, derive total_amount and category.
        
        Args:
            df: Raw sales DataFrame
            
        Returns:
            Cleaned DataFrame
        """
        if df is None or df.empty:
            logger.error("No data to clean")
            return pd.DataFrame()
        
        logger.info("Starting data cleaning...")
        cleaned_df = df.copy()
        
        # 1. Remove duplicates
        initial_rows = len(cleaned_df)
        cleaned_df = cleaned_df.drop_duplicates()
        logger.info(f"Removed {initial_rows - len(cleaned_df)} duplicates")
        
        # 2. Handle missing values
        missing = cleaned_df.isnull().sum()
        logger.info(f"Missing values before cleaning:\n{missing[missing > 0]}")
        
        # Fill numeric with median
        numeric_cols = ['quantity', 'price']
        for col in numeric_cols:
            if col in cleaned_df.columns:
                median_val = cleaned_df[col].median()
                cleaned_df[col].fillna(median_val, inplace=True)
        
        # Fill categorical with mode
        cat_cols = ['product', 'region']
        for col in cat_cols:
            if col in cleaned_df.columns:
                mode_val = cleaned_df[col].mode()
                if not mode_val.empty:
                    cleaned_df[col].fillna(mode_val.iloc[0], inplace=True)
        
        # Drop rows still missing critical data
        cleaned_df.dropna(subset=['date'], inplace=True)
        
        # 3. Fix data types
        cleaned_df['date'] = pd.to_datetime(cleaned_df['date'], errors='coerce')
        cleaned_df['quantity'] = pd.to_numeric(cleaned_df['quantity'], errors='coerce').astype(int)
        cleaned_df['price'] = pd.to_numeric(cleaned_df['price'], errors='coerce')
        
        # 4. Derive total_amount
        cleaned_df['total_amount'] = cleaned_df['quantity'] * cleaned_df['price']
        
        # 5. Extract category from product name (simple heuristic)
        def get_category(product: str) -> str:
            product_lower = product.lower()
            if any(word in product_lower for word in ['laptop', 'monitor', 'ssd', 'keyboard']):
                return 'Electronics'
            elif any(word in product_lower for word in ['phone', 'iphone', 'smartphone', 'case']):
                return 'Mobile'
            elif any(word in product_lower for word in ['shirt', 'jeans', 'dress', 'skirt']):
                return 'Clothing'
            elif any(word in product_lower for word in ['book', 'notebook', 'textbook']):
                return 'Books'
            elif any(word in product_lower for word in ['shoes', 'sneakers', 'boots']):
                return 'Sports'
            elif any(word in product_lower for word in ['desk', 'chair', 'table', 'sofa']):
                return 'Furniture'
            else:
                return 'Other'
        
        cleaned_df['category'] = cleaned_df['product'].apply(get_category)
        
        # 6. Remove outliers (price > 3 std dev)
        before_outliers = len(cleaned_df)
        price_std = cleaned_df['price'].std()
        price_mean = cleaned_df['price'].mean()
        cleaned_df = cleaned_df[
            (cleaned_df['price'] >= price_mean - 3*price_std) & 
            (cleaned_df['price'] <= price_mean + 3*price_std)
        ]
        logger.info(f"Removed {before_outliers - len(cleaned_df)} outliers")
        
        # Remove invalid dates and negative values
        cleaned_df = cleaned_df[
            (cleaned_df['date'].notna()) &
            (cleaned_df['quantity'] > 0) &
            (cleaned_df['price'] > 0) &
            (cleaned_df['total_amount'] > 0)
        ]
        
        logger.info(f"Cleaning complete. Final shape: {cleaned_df.shape}")
        logger.info(f"Date range: {cleaned_df['date'].min()} to {cleaned_df['date'].max()}")
        logger.info(f"Categories: {cleaned_df['category'].value_counts().to_dict()}")
        
        return cleaned_df

