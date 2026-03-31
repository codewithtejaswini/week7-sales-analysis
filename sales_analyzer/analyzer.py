def analyze_data(df):
    results = {}

    results['total_sales'] = df['total_amount'].sum()
    results['average_sales'] = df['total_amount'].mean()

    # Top products
    results['top_products'] = df.groupby('product_id')['total_amount'].sum().sort_values(ascending=False).head(5)

    # Monthly sales
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')

    results['monthly_sales'] = df.groupby('month')['total_amount'].sum()

    return results
