import numpy as np

def clean_data(df):
    if df is None:
        return None

    df = df.drop_duplicates()

    # Fill missing numeric values
    for col in df.select_dtypes(include=[np.number]):
        df[col].fillna(df[col].median(), inplace=True)

    # Fill missing categorical values
    for col in df.select_dtypes(include=['object']):
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df
