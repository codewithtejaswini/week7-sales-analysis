"""Analyzer module.
Main SalesAnalyzer class for comprehensive sales analysis."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
from typing import Dict, Optional
from pathlib import Path
from .data_loader import load_sales_data
from .data_cleaner import DataCleaner

logger = logging.getLogger(__name__)

class SalesAnalyzer:
    """Analyzes sales data and generates insights"""
    
    def __init__(self, data_path: str | Path):
        self.data_path = Path(data_path)
        self.df = None
        self.load_data()
    
    def load_data(self):
        """Load sales data from CSV file"""
        try:
            self.df = load_sales_data(self.data_path)
            if self.df is None:
                raise ValueError("Failed to load data")
            
            # Auto clean on load
            self.df = DataCleaner.clean_sales_data(self.df)
            
            print(f"Data loaded successfully. Shape: {self.df.shape}")
            print(f"Columns: {list(self.df.columns)}")
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            print(f"Error loading data: {e}")
    
    def clean_data(self):
        """Clean the sales data (already done in load_data)"""
        if self.df is None:
            print("No data loaded")
            return
        print("Data already cleaned during loading.")
    
    def calculate_basic_stats(self) -> Dict:
        """Calculate basic sales statistics"""
        if self.df is None:
            return {}
        
        stats = {
            'total_sales': self.df['total_amount'].sum(),
            'average_order': self.df['total_amount'].mean(),
            'total_orders': len(self.df),
            'unique_customers': self.df['region'].nunique(),  # Using region as proxy
            'unique_products': self.df['product'].nunique()
        }
        
        # Add date range if available
        if 'date' in self.df.columns:
            stats['date_range'] = {
                'start': self.df['date'].min().strftime('%Y-%m-%d'),
                'end': self.df['date'].max().strftime('%Y-%m-%d')
            }
        
        return stats
    
    def analyze_sales_by_category(self) -> pd.DataFrame:
        """Analyze sales by product category"""
        if self.df is None or 'category' not in self.df.columns:
            return pd.DataFrame()
        
        category_sales = self.df.groupby('category').agg({
            'total_amount': 'sum',
            'quantity': 'sum',
            'total_amount': 'count'
        }).rename(columns={'total_amount': 'order_count'})
        
        category_sales = category_sales.sort_values('total_amount', ascending=False)
        return category_sales
    
    def analyze_monthly_trends(self) -> pd.DataFrame:
        """Analyze monthly sales trends"""
        if self.df is None or 'date' not in self.df.columns:
            return pd.DataFrame()
        
        # Extract month-year
        self.df['month_year'] = self.df['date'].dt.to_period('M')
        
        monthly_sales = self.df.groupby('month_year').agg({
            'total_amount': 'sum',
            'quantity': 'sum',
            'region': 'nunique'
        }).rename(columns={'region': 'unique_regions'})
        
        # Calculate month-over-month growth
        monthly_sales['growth_rate'] = monthly_sales['total_amount'].pct_change() * 100
        
        return monthly_sales
    
    def get_summary_report(self) -> str:
        """Generate formatted console summary matching sample output"""
        if self.df is None:
            return "No data available"
        
        stats = self.calculate_basic_stats()
        category_sales = self.analyze_sales_by_category()
        
        report = f"""📊 SALES DATA ANALYSIS REPORT
===============================

📅 Analysis Period: {stats.get('date_range', {}).get('start', 'N/A')} - {stats.get('date_range', {}).get('end', 'N/A')}

📈 BASIC STATISTICS:
- Total Sales: ${stats.get('total_sales', 0):,.2f}
- Total Orders: {stats.get('total_orders', 0):,}
- Average Order Value: ${stats.get('average_order', 0):.2f}
- Unique Regions: {stats.get('unique_customers', 0)}
- Unique Products: {stats.get('unique_products', 0)}

"""
        
        if not category_sales.empty:
            report += "🏆 TOP PRODUCT CATEGORIES:\n"
            top_cats = category_sales.head(5)
            for i, (cat, row) in enumerate(top_cats.iterrows(), 1):
                pct = (row['total_amount'] / stats['total_sales']) * 100
                report += f"{i}. {cat}: ${row['total_amount']:,.0f} ({pct:.1f}%)\n"
        
        monthly = self.analyze_monthly_trends()
        if not monthly.empty:
            report += f"\n📅 MONTHLY TRENDS:\n"
            report += f"- Highest Sales Month: {monthly['total_amount'].idxmax()} (${monthly['total_amount'].max():,.0f})\n"
            report += f"- Lowest Sales Month: {monthly['total_amount'].idxmin()} (${monthly['total_amount'].min():,.0f})\n"
            report += f"- Average Monthly Sales: ${monthly['total_amount'].mean():,.0f}\n"
        
        report += f"""
💰 RECOMMENDATIONS:
1. Focus marketing on Electronics category
2. Analyze regional performance differences
3. Consider seasonal promotions in peak months
4. Expand product range in high-performing categories
"""
        
        return report

