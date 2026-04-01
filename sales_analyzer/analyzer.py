import pandas as pd


def analyze_data(df):
    try:
        # -----------------------------
        # DATE HANDLING
        # -----------------------------
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])

        # -----------------------------
        # CREATE TOTAL AMOUNT
        # -----------------------------
        df['total_amount'] = df['quantity'] * df['price']

        # -----------------------------
        # BASIC STATISTICS
        # -----------------------------
        total_sales = df['total_amount'].sum()
        total_orders = len(df)
        avg_order = df['total_amount'].mean()
        unique_products = df['product'].nunique()

        # -----------------------------
        # DATE RANGE
        # -----------------------------
        start_date = df['date'].min().strftime("%b %Y")
        end_date = df['date'].max().strftime("%b %Y")

        # -----------------------------
        # MONTHLY ANALYSIS
        # -----------------------------
        df['month'] = df['date'].dt.to_period('M')
        monthly = df.groupby('month')['total_amount'].sum()

        highest = monthly.idxmax()
        lowest = monthly.idxmin()
        avg_monthly = monthly.mean()

        growth = monthly.pct_change().fillna(0) * 100
        best_growth = growth.idxmax()

        # -----------------------------
        # TOP PRODUCTS
        # -----------------------------
        top_products = (
            df.groupby('product')['total_amount']
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        # -----------------------------
        # CUSTOMER INSIGHTS
        # -----------------------------
        if 'customer_id' in df.columns:
            customer_spending = df.groupby('customer_id')['total_amount'].sum()

            repeat_customers = (df['customer_id'].value_counts() > 1).sum()
            total_customers = df['customer_id'].nunique()

            repeat_percent = (repeat_customers / total_customers) * 100

            avg_customer_value = customer_spending.mean()

            top_n = max(1, int(0.1 * len(customer_spending)))
            top_revenue = customer_spending.sort_values(ascending=False).head(top_n).sum()

            top_percent_revenue = (top_revenue / total_sales) * 100
        else:
            # Safe fallback if column missing
            repeat_customers = 0
            repeat_percent = 0
            avg_customer_value = 0
            top_percent_revenue = 0

        # -----------------------------
        # RETURN ALL RESULTS
        # -----------------------------
        return {
            "df": df,
            "total_sales": total_sales,
            "total_orders": total_orders,
            "avg_order": avg_order,
            "unique_products": unique_products,
            "start_date": start_date,
            "end_date": end_date,
            "monthly": monthly,
            "highest": highest,
            "lowest": lowest,
            "avg_monthly": avg_monthly,
            "best_growth": best_growth,
            "growth": growth,
            "top_products": top_products,

            # CUSTOMER INSIGHTS
            "repeat_customers": repeat_customers,
            "repeat_percent": repeat_percent,
            "avg_customer_value": avg_customer_value,
            "top_percent_revenue": top_percent_revenue
        }

    except Exception as e:
        print("❌ Error in analysis:", e)
        exit()
