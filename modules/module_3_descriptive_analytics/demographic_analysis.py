import pandas as pd
from load_features import load_state_features

#adult vs child enrolment gap bojhar jonne

OUTPUT_PATH = "../../outputs/reports/"

def analyze_demographics():
    df = load_state_features()

    df["adult_ratio"] = df["adult_enrolments"] / df["total_enrolments"]
    df["child_ratio"] = 1 - df["adult_ratio"]

    df[[
        "state",
        "adult_ratio",
        "child_ratio"
    ]].to_csv(OUTPUT_PATH + "demographic_summary.csv", index=False)

if __name__ == "__main__":
    analyze_demographics()
