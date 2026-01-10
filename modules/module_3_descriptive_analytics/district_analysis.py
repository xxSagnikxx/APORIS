import pandas as pd
from load_features import load_district_features

#district level extreme behavior ber korar jonne

OUTPUT_PATH = "../../outputs/reports/"

def analyze_districts():
    df = load_district_features()

    df["update_ratio"] = df["total_updates"] / df["total_enrolments"]

    # beshi risky district gulo alada kore rakha
    high_risk = df[df["update_ratio"] > 5]

    high_risk.to_csv(OUTPUT_PATH + "district_summary.csv", index=False)

if __name__ == "__main__":
    analyze_districts()
