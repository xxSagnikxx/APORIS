import pandas as pd

#final cause wise summary ber korar jonne

OUTPUT_PATH = "../../outputs/reports/"

def summarize_causes():
    df = pd.read_csv(OUTPUT_PATH + "cause_predictions.csv")

    summary = df[[
        "state",
        "is_anomaly",
        "predicted_cause",
        "update_ratio",
        "quality_score",
        "future_load_pressure"
    ]]

    summary.to_csv(OUTPUT_PATH + "cause_summary.csv", index=False)

if __name__ == "__main__":
    summarize_causes()
