import matplotlib.pyplot as plt

def create_charts(df):
    try:
        df['month'] = df['date'].dt.to_period('M')
        monthly = df.groupby('month')['total_amount'].sum()

        monthly.plot(title="Monthly Sales")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("❌ Error in visualization:", e)
