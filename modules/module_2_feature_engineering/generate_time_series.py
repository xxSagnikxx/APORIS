import pandas as pd
from clean_data import clean_all

#daily time series bananor jonne

OUTPUT_PATH = "../../data/features/"

def generate_daily_series():
    enrol, demo, bio = clean_all()

    enrol_daily = enrol.groupby("date").agg(
        total_enrolments=("enrolments", "sum")
    ).reset_index()

    update_daily = demo.groupby("date").agg(
        total_updates=("updates", "sum")
    ).reset_index()

    daily_series = enrol_daily.merge(
        update_daily, on="date", how="left"
    )

    daily_series.to_csv(
        OUTPUT_PATH + "daily_time_series.csv",
        index=False
    )

if __name__ == "__main__":
    generate_daily_series()
