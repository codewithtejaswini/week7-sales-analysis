def generate_report(result):
    try:
        print("\n📊 SALES DATA ANALYSIS REPORT")
        print("=" * 35)

        print(f"\n📅 Analysis Period: {result['start_date']} - {result['end_date']}")

        print("\n📈 BASIC STATISTICS:")
        print(f"- Total Sales: ${result['total_sales']:,.2f}")
        print(f"- Total Orders: {result['total_orders']}")
        print(f"- Average Order Value: ${result['avg_order']:,.2f}")
        print(f"- Unique Products: {result['unique_products']}")

        print("\n🏆 TOP PRODUCTS:")
        for i, (p, v) in enumerate(result['top_products'].items(), 1):
            percent = (v / result['total_sales']) * 100
            print(f"{i}. {p}: ${v:,.0f} ({percent:.1f}%)")

        print("\n📅 MONTHLY TRENDS:")
        print(f"- Highest Sales Month: {result['highest']} (${result['monthly'].max():,.0f})")
        print(f"- Lowest Sales Month: {result['lowest']} (${result['monthly'].min():,.0f})")
        print(f"- Average Monthly Sales: ${result['avg_monthly']:,.2f}")
        print(f"- Best Growth Month: {result['best_growth']} ({result['growth'].max():.1f}%)")


        print("\n👥 CUSTOMER INSIGHTS:")
        print(f"- Repeat Customers: {result['repeat_customers']} ({result['repeat_percent']:.1f}%)")
        print(f"- Average Customer Value: ${result['avg_customer_value']:,.2f}")
        print(f"- Top 10% Customers Generate: {result['top_percent_revenue']:.1f}% of revenue")

        print("\n💰 RECOMMENDATIONS:")
        print("1. Focus on top-selling products")
        print("2. Improve low-sales months")
        print("3. Increase stock for high-demand items")
        print("4. Analyze seasonal trends\n")

    except Exception as e:
        print("❌ Error in report:", e)
