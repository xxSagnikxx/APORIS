import pandas as pd
import os
from clean_data import clean_all

OUT_DIR = os.path.abspath(os.path.join("data", "features"))

def aggregate_state_level():
    enrol, _, _ = clean_all()

    df = enrol.groupby("state").agg(
        total_enrolment=("total_enrolment", "sum"),
        districts=("district", "nunique")
    ).reset_index()

    df.to_csv(os.path.join(OUT_DIR, "state_level_features.csv"), index=False)
    print("✔ state_level_features.csv saved")

if __name__ == "__main__":
    aggregate_state_level()
