def clean_data(df):
    try:
        df = df.drop_duplicates()
        print("✅ Removed duplicate rows")

        
        df = df.ffill().bfill()

        print("✅ Missing values handled")
        return df
    except Exception as e:
        print("❌ Error in cleaning:", e)
        exit()
