import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data Loaded Successfully")
        return df
    except Exception as e:
        print("Error:", e)
        return None
