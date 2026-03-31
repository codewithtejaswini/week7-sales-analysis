import matplotlib.pyplot as plt
import os

def create_charts(df):
    os.makedirs("data/reports", exist_ok=True)

    # Monthly Sales
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')

    monthly = df.groupby('month')['total_amount'].sum()

    monthly.plot(kind='line')
    plt.title("Monthly Sales")
    plt.savefig("data/reports/monthly_sales.png")
    plt.close()

    # Category chart
    category = df.groupby('category')['total_amount'].sum()
    category.plot(kind='bar')
    plt.title("Category Sales")
    plt.savefig("data/reports/category_sales.png")
    plt.close()

