# 📊 Sales Data Analysis Dashboard

---

## 📌 1. Project Overview

The **Sales Data Analysis Dashboard** is a Python-based project designed to analyze and visualize sales data for better business decision-making. The system processes raw sales data, performs cleaning and transformation, and generates meaningful insights such as total sales, trends, and top-performing products.

This project simulates a real-world business analytics workflow using **Pandas**, making it ideal for understanding data analysis concepts.

---

## 🎯 2. Objectives

* To understand the complete data analysis pipeline
* To clean and preprocess raw data
* To perform exploratory data analysis (EDA)
* To generate business insights from sales data
* To visualize trends using graphs
* To create automated reports

---

## 🚀 3. Features

* 📂 Load data from CSV files
* 🧹 Data cleaning (handle missing values & duplicates)
* 🔍 Exploratory Data Analysis (EDA)
* 📊 Sales analysis (monthly, category-wise, product-wise)
* 📈 Data visualization (line chart, bar chart, pie chart)
* 📄 Report generation in Excel format
* 🧩 Modular code structure for scalability

---

## 🛠️ 4. Technologies Used

* **Python** – Core programming language
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **OpenPyXL** – Excel report generation
* **Jupyter Notebook** – Interactive analysis

---

## 📁 5. Project Structure

```bash
week7-sales-analysis/
│── sales_analyzer/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── reporter.py
│
│── notebooks/
│   ├── exploration.ipynb
│   └── analysis.ipynb
│
│── data/
│   ├── raw/
│   │   └── sales_data.csv
│   ├── processed/
│   └── reports/
│
│── tests/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ 6. Installation & Setup

### Step 1: Clone Repository

```bash
git clone <https://github.com/codewithtejaswini/week7-sales-analysis.git>
cd week7-sales-analysis
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Project

```bash
python main.py
```

---

## 🔄 7. Workflow of Project

1. **Data Loading**

   * Sales data is loaded from CSV file using Pandas

2. **Data Cleaning**

   * Remove duplicate records
   * Handle missing values
   * Convert data types (dates, numbers)

3. **Exploratory Data Analysis (EDA)**

   * Analyze dataset structure
   * Check statistical summary
   * Identify patterns and anomalies

4. **Data Analysis**

   * Total sales calculation
   * Average order value
   * Top-selling products
   * Category-wise sales

5. **Visualization**

   * Monthly sales trend (line chart)
   * Category-wise sales (bar chart)
   * Distribution analysis (pie chart)

6. **Report Generation**

   * Excel report with summary statistics
   * Charts saved as image files

---

## 📊 8. Key Analysis Performed

* ✅ Total Revenue Calculation
* ✅ Average Sales per Order
* ✅ Monthly Sales Trends
* ✅ Top 5 Products
* ✅ Category-wise Revenue Distribution

---

## 📈 9. Output

The system generates:

* 📉 Monthly sales trend graph
* 📊 Category-wise bar chart
* 🥧 Pie chart for distribution
* 📄 Excel report (`report.xlsx`)

---

## 🧠 10. Key Insights

* Electronics category contributes the highest revenue
* Sales show growth over time
* Few top products generate majority of income
* Seasonal trends observed in sales

---

## 🎓 11. Learning Outcomes

* Understanding of real-world data analysis process
* Hands-on experience with Pandas and data cleaning
* Visualization techniques using Matplotlib
* Writing modular and reusable Python code
* Generating automated reports

---

## 🔮 12. Future Enhancements

* Add interactive dashboard using Streamlit or Power BI
* Implement machine learning for sales prediction
* Add database integration (MySQL)
* Create web-based UI

---

## 📌 13. Conclusion

This project demonstrates how raw data can be transformed into meaningful insights using data analysis techniques. It helps businesses understand trends, optimize strategies, and improve decision-making.

---

## 👩‍💻 14. Author

**Tejaswini Sawakhande** Github: https://github.com/codewithtejaswini/week7-sales-analysis.git

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

