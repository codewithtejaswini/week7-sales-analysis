from sales_analyzer.data_loader import load_data
from sales_analyzer.data_cleaner import clean_data
from sales_analyzer.analyzer import analyze_data
from sales_analyzer.visualizer import create_charts
from sales_analyzer.reporter import generate_report


def main():
    df = load_data("data/raw/sales_data.csv")

    df = clean_data(df)

    result = analyze_data(df)

    create_charts(result["df"])

    generate_report(result)


if __name__ == "__main__":
    main()
