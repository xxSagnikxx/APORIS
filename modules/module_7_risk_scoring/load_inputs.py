import pandas as pd
REPORT_PATH = "../../outputs/reports/"
def load_anomaly_summary():
    return pd.read_csv(REPORT_PATH + "anomaly_summary.csv")
def load_cause_summary():
    return pd.read_csv(REPORT_PATH + "cause_summary.csv")
def load_quality_scores():
    return pd.read_csv(REPORT_PATH + "quality_scores.csv")
