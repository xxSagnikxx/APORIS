import pandas as pd
import os
from clean_data import clean_all
OUT_DIR = os.path.abspath(os.path.join("data", "features"))
def generate_daily_series():
    enrol, _, _ = clean_all()
    enrol["date"] = pd.to_datetime(enrol["date"])
    daily = enrol.groupby("date").agg(
        total_enrolment=("total_enrolment", "sum")
    ).reset_index()
    daily.to_csv(os.path.join(OUT_DIR, "daily_time_series.csv"), index=False)
    print("daily_time_series.csv saved")
if __name__ == "__main__":
    generate_daily_series()
