import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

#actual anomaly detection ekhane hobe.....scaling na korle isolation forest bhul signal debe

INPUT_PATH = "../../outputs/reports/"
OUTPUT_PATH = "../../outputs/reports/"

def detect():
    # anomaly feature data load
    df = pd.read_csv(INPUT_PATH + "anomaly_features.csv")

    # anomaly detect korar main feature gulo
    features = df[[
        "update_ratio",
        "inverse_quality",
        "future_load_pressure"
    ]]

    # feature scaling mandatory
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # isolation forest model
    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )

    # model fit + prediction
    df["anomaly_flag"] = model.fit_predict(features_scaled)
    df["anomaly_score"] = model.decision_function(features_scaled)

    # -1 mane anomaly, 1 mane normal
    df["is_anomaly"] = df["anomaly_flag"].apply(
        lambda x: 1 if x == -1 else 0
    )

    # final result save
    df.to_csv(OUTPUT_PATH + "anomaly_detection_results.csv", index=False)

if __name__ == "__main__":
    detect()
