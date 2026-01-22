import pandas as pd
from load_features import load_state_features
OUTPUT_PATH = "../../outputs/reports/"
def calculate_quality_score():
    df = load_state_features()
    df["update_ratio"] = df["total_updates"] / df["total_enrolments"]
    df["quality_score"] = 100 - (df["update_ratio"] * 10)
    df["quality_score"] = df["quality_score"].clip(0, 100)
    df[[
        "state",
        "quality_score",
        "update_ratio"
    ]].to_csv(OUTPUT_PATH + "quality_scores.csv", index=False)
if __name__ == "__main__":
    calculate_quality_score()
