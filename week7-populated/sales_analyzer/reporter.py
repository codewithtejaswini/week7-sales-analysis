"""Reporter module.
Generate Excel reports and summary statistics."""
import pandas as pd
import logging
from typing import Optional
from pathlib import Path
from .analyzer import SalesAnalyzer

logger = logging.getLogger(__name__)

def generate_excel_report(analyzer: SalesAnalyzer, output_path: str = 'sales_report.xlsx') -> bool:
    """Generate comprehensive Excel report with multiple sheets"""
    try:
        if analyzer.df is None:
            logger.error("No data available for reporting")
            return False
        
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Summary sheet
            stats = analyzer.calculate_basic_stats()
            stats_df = pd.DataFrame([stats])
            stats_df.to_excel(writer, sheet_name='Summary', index=False)
            
            # Monthly trends
            monthly_data = analyzer.analyze_monthly_trends()
            if not monthly_data.empty:
                monthly_data.to_excel(writer, sheet_name='Monthly Trends')
            
            # Category analysis
            category_data = analyzer.analyze_sales_by_category()
            if not category_data.empty:
                category_data.to_excel(writer, sheet_name='Category Analysis')
            
            # Region analysis
            if 'region' in analyzer.df.columns:
                region_data = analyzer.df.groupby('region').agg({
                    'total_amount': 'sum',
                    'quantity': 'sum',
                    'total_amount': 'count'
                }).rename(columns={'total_amount': 'order_count'})
                region_data.to_excel(writer, sheet_name='Region Analysis')
            
            # Full dataset sample (first 1000 rows)
            sample_data = analyzer.df.head(1000).round(2)
            sample_data.to_excel(writer, sheet_name='Sample Data', index=False)
            
            # Product performance (top 50)
            if 'product' in analyzer.df.columns:
                product_perf = analyzer.df.groupby('product').agg({
                    'total_amount': 'sum',
                    'quantity': 'sum'
                }).sort_values('total_amount', ascending=False).head(50)
                product_perf.to_excel(writer, sheet_name='Top Products')
        
        logger.info(f"Excel report generated: {output_path}")
        print(f"✅ Report generated: {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        print(f"❌ Error generating report: {e}")
        return False

def print_console_summary(analyzer: SalesAnalyzer):
    """Print formatted console summary"""
    print(analyzer.get_summary_report())

