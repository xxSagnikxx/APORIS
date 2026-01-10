import pandas as pd

#anomaly gulo summarize korar jonne

OUTPUT_PATH = "../../outputs/reports/"

def summarize_anomalies():
    df = pd.read_csv(OUTPUT_PATH + "anomaly_detection_results.csv")

    summary = df[[
        "state",
        "update_ratio",
        "quality_score",
        "future_load_pressure",
        "is_anomaly",
        "anomaly_score"
    ]]

    summary.to_csv(OUTPUT_PATH + "anomaly_summary.csv", index=False)

if __name__ == "__main__":
    summarize_anomalies()
