import pandas as pd

#time series data load korar jonne

DATA_PATH = "../../data/features/"

def load_daily_series():
    df = pd.read_csv(DATA_PATH + "daily_time_series.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df
