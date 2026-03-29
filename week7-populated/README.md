# Week 7: Sales Data Analysis Dashboard

Professional sales analysis system using Pandas, Matplotlib, and advanced data processing.

## 📋 Features

- **Data Loading**: CSV import with validation
- **Data Cleaning**: Handle missing values, outliers, derive metrics (total_amount, category)
- **EDA**: Basic statistics, category analysis, monthly trends
- **Visualizations**: 5 professional charts (line, pie, bar, histogram, region)
- **Reporting**: Multi-sheet Excel export + formatted console summary
- **CLI Interface**: `python main.py data.csv --analyze --visualize --report`

## 🛠️ Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Full analysis
python main.py data/raw/sales_data.csv --analyze --visualize --report

# Just summary
python main.py data/raw/sales_data.csv --analyze

# Generate report only
python main.py data/raw/sales_data.csv --report
```

## 📊 Sample Output

```
📊 SALES DATA ANALYSIS REPORT
===============================

📅 Analysis Period: 2023-01-15 - 2024-01-30

📈 BASIC STATISTICS:
- Total Sales: $1,245,678.90
- Total Orders: 4,567
- Average Order Value: $272.84
...
```

## 📁 Project Structure

```
week7-sales-analysis/
├── sales_analyzer/         # Core analysis modules
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── reporter.py
├── data/
│   ├── raw/sales_data.csv  # Sample dataset (500+ rows)
│   ├── processed/
│   └── reports/
├── notebooks/              # Jupyter analysis notebooks
├── output/                 # Generated viz & reports
├── main.py                 # CLI entrypoint
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎯 Key Metrics Calculated

- Total sales, average order value
- Category performance (Electronics, Clothing, etc.)
- Monthly growth rates & trends
- Regional sales distribution
- Top products & outlier detection

## 🧪 Testing

```bash
pip install pytest
pytest tests/
```

## 📈 Sample Visualizations Generated

1. **Monthly Sales Trend** (line chart)
2. **Category Pie Chart**
3. **Top 10 Categories Bar**
4. **Order Value Distribution**
5. **Sales by Region**

## 🔧 Development

```bash
# Activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\\Scripts\\activate  # Windows

# Install dev dependencies
pip install -r requirements.txt
pip install pre-commit black flake8

# Code formatting
black .
pre-commit install
```

---

**Built with professional Python standards: type hints, logging, error handling, PEP8, modular design.**

