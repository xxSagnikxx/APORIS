import pandas as pd
from load_inputs import load_anomaly_data
OUTPUT_PATH = "../../outputs/reports/"
def generate_labels():
    df = load_anomaly_data()
    def assign_cause(row):
        if row["update_ratio"] > 5:
            return "High_Update_Frequency"
        elif row["quality_score"] < 50:
            return "Poor_Service_Quality"
        elif row["future_load_pressure"] > row["future_load_pressure"].mean():
            return "Future_Load_Risk"
        else:
            return "Normal"
    df["cause_label"] = df.apply(assign_cause, axis=1)
    df.to_csv(OUTPUT_PATH + "cause_labeled_data.csv", index=False)
if __name__ == "__main__":
    generate_labels()
