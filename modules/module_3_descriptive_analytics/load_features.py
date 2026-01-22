import pandas as pd
DATA_PATH = "../../data/features/"
def load_state_features():
    return pd.read_csv(DATA_PATH + "state_level_features.csv")
def load_district_features():
    return pd.read_csv(DATA_PATH + "district_level_features.csv")
def load_time_series():
    return pd.read_csv(DATA_PATH + "daily_time_series.csv")
