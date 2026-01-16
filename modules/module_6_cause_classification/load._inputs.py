import pandas as pd

#previous module gulo theke data load korar jonne

REPORT_PATH = "../../outputs/reports/"

def load_anomaly_data():
    return pd.read_csv(REPORT_PATH + "anomaly_detection_results.csv")

def load_quality_scores():
    return pd.read_csv(REPORT_PATH + "quality_scores.csv")

def load_forecast_summary():
    return pd.read_csv(REPORT_PATH + "forecast_master_summary.csv")
