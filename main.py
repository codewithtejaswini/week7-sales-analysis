from sales_analyzer import (
    load_data,
    clean_data,
    analyze_data,
    create_charts,
    generate_report
)

def main():
    file_path = "data/raw/sales_data.csv"

    df = load_data(file_path)
    df = clean_data(df)

    results = analyze_data(df)

    create_charts(df)
    generate_report(results)

if __name__ == "__main__":
    main()
