"""Visualizer module.
Create charts and visualizations from sales data."""
import matplotlib.pyplot as plt
import seaborn as sns
import os
from typing import Optional
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def create_visualizations(df, output_dir: str = 'output'):
    """Create comprehensive sales visualizations"""
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # 1. Monthly sales trend line chart
    if 'month_year' in df.columns:
        plt.figure(figsize=(14, 8))
        monthly_sales = df.groupby('month_year')['total_amount'].sum()
        monthly_sales.plot(kind='line', marker='o', linewidth=2.5, markersize=8)
        plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold')
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Total Sales ($)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/monthly_trend.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Saved monthly_trend.png")
    
    # 2. Sales by category pie chart
    if 'category' in df.columns:
        cat_sales = df.groupby('category')['total_amount'].sum()
        plt.figure(figsize=(12, 8))
        plt.pie(cat_sales.values, labels=cat_sales.index, autopct='%1.1f%%', startangle=90)
        plt.title('Sales Distribution by Category', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/category_pie.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Saved category_pie.png")
    
    # 3. Top categories bar chart
    if 'category' in df.columns:
        top_cats = df.groupby('category')['total_amount'].sum().nlargest(10)
        plt.figure(figsize=(12, 8))
        bars = plt.bar(range(len(top_cats)), top_cats.values, color=sns.color_palette("husl", len(top_cats)))
        plt.title('Top 10 Product Categories by Sales', fontsize=16, fontweight='bold')
        plt.xlabel('Category', fontsize=12)
        plt.ylabel('Total Sales ($)', fontsize=12)
        plt.xticks(range(len(top_cats)), top_cats.index, rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar, val in zip(bars, top_cats.values):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000,
                    f'${val:,.0f}', ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/top_categories_bar.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Saved top_categories_bar.png")
    
    # 4. Order value distribution histogram
    plt.figure(figsize=(12, 8))
    plt.hist(df['total_amount'], bins=50, edgecolor='black', alpha=0.7, color='skyblue')
    plt.title('Order Value Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Order Value ($)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.axvline(df['total_amount'].mean(), color='red', linestyle='--', 
                label=f'Mean: ${df["total_amount"].mean():.2f}')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{output_dir}/order_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    logger.info("Saved order_distribution.png")
    
    # 5. Sales by region
    if 'region' in df.columns:
        region_sales = df.groupby('region')['total_amount'].sum().sort_values(ascending=False)
        plt.figure(figsize=(12, 8))
        region_sales.plot(kind='bar', color='coral')
        plt.title('Sales by Region', fontsize=16, fontweight='bold')
        plt.xlabel('Region', fontsize=12)
        plt.ylabel('Total Sales ($)', fontsize=12)
        plt.xticks(rotation=0)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/sales_by_region.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info("Saved sales_by_region.png")
    
    print(f"✅ All visualizations saved to {output_dir}/")

