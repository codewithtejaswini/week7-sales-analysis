import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        print("Data Loaded Successfully")
        print("\n📌 Columns:", df.columns)
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        exit()
