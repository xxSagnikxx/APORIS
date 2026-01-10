import pandas as pd

#agekar module gulo theke data load korar jonne

REPORT_PATH = "../../outputs/reports/"

def load_quality_scores():
    return pd.read_csv(REPORT_PATH + "quality_scores.csv")

def load_forecast_summary():
    return pd.read_csv(REPORT_PATH + "forecast_master_summary.csv")

def load_temporal_trends():
    return pd.read_csv(REPORT_PATH + "temporal_trends.csv")
