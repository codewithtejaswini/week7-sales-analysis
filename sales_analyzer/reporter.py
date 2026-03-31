import pandas as pd

def generate_report(results):
    with pd.ExcelWriter("data/reports/report.xlsx") as writer:
        pd.DataFrame([results]).to_excel(writer, sheet_name="Summary")

    print("Report Generated")

