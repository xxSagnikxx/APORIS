import pandas as pd
from load_inputs import load_anomaly_summary, load_cause_summary

#numeric risk score calculate korar jonne

OUTPUT_PATH = "../../outputs/reports/"

def calculate_risk_score():
    anomaly = load_anomaly_summary()
    cause = load_cause_summary()

    df = anomaly.merge(
        cause,
        on="state",
        suffixes=("_anomaly", "_cause")
    )

    # normalize inputs
    df["update_risk"] = df["update_ratio"] * 10
    df["quality_risk"] = (100 - df["quality_score"]) * 0.5
    df["anomaly_risk"] = df["is_anomaly"] * 30

    # cause based weight
    def cause_weight(cause):
        if cause == "High_Update_Frequency":
            return 15
        elif cause == "Poor_Service_Quality":
            return 20
        elif cause == "Future_Load_Risk":
            return 10
        else:
            return 0

    df["cause_risk"] = df["predicted_cause"].apply(cause_weight)

    # final risk score
    df["risk_score"] = (
        df["update_risk"] +
        df["quality_risk"] +
        df["anomaly_risk"] +
        df["cause_risk"]
    )

    df["risk_score"] = df["risk_score"].clip(0, 100)

    df.to_csv(OUTPUT_PATH + "risk_scores.csv", index=False)

if __name__ == "__main__":
    calculate_risk_score()

