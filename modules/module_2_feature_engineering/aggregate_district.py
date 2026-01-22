import pandas as pd
import os
from clean_data import clean_all
OUT_DIR = os.path.abspath(os.path.join("data", "features"))
def aggregate_district_level():
    enrol, _, _ = clean_all()
    df = enrol.groupby(["state", "district"]).agg(
        total_enrolment=("total_enrolment", "sum"),
        records=("pincode", "count")
    ).reset_index()
    df.to_csv(os.path.join(OUT_DIR, "district_level_features.csv"), index=False)
    print("district_level_features.csv saved")
if __name__ == "__main__":
    aggregate_district_level()
