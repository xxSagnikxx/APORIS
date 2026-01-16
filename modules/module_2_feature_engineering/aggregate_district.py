import pandas as pd
from clean_data import clean_all

#district level feature bananor jonne

OUTPUT_PATH = "../../data/features/"

def aggregate_district_level():
    enrol, demo, bio = clean_all()

    enrol_dist = enrol.groupby(["state", "district"]).agg(
        total_enrolments=("enrolments", "sum")
    ).reset_index()

    demo_dist = demo.groupby(["state", "district"]).agg(
        total_updates=("updates", "sum")
    ).reset_index()

    district_features = enrol_dist.merge(
        demo_dist, on=["state", "district"], how="left"
    )

    district_features.to_csv(
        OUTPUT_PATH + "district_level_features.csv",
        index=False
    )

if __name__ == "__main__":
    aggregate_district_level()
