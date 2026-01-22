import pandas as pd
from load_features import load_state_features
OUTPUT_PATH = "../../outputs/reports/"
def analyze_states():
    df = load_state_features()
    df["update_ratio"] = df["total_updates"] / df["total_enrolments"]
    summary = df.sort_values(by="total_enrolments", ascending=False)
    summary.to_csv(OUTPUT_PATH + "state_summary.csv", index=False)
if __name__ == "__main__":
    analyze_states()
