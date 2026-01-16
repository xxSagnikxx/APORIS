import pandas as pd
from clean_data import clean_all

#state level feature bananor jonne

OUTPUT_PATH = "../../data/features/"

def aggregate_state_level():
    enrol, demo, bio = clean_all()

    enrol_state = enrol.groupby("state").agg(
        total_enrolments=("enrolments", "sum"),
        adult_enrolments=("age", lambda x: (x >= 18).sum())
    ).reset_index()

    demo_state = demo.groupby("state").agg(
        total_demo_updates=("updates", "sum")
    ).reset_index()

    bio_state = bio.groupby("state").agg(
        total_bio_updates=("updates", "sum")
    ).reset_index()

    state_features = enrol_state.merge(demo_state, on="state", how="left")
    state_features = state_features.merge(bio_state, on="state", how="left")

    state_features["total_updates"] = (
        state_features["total_demo_updates"] +
        state_features["total_bio_updates"]
    )

    state_features.to_csv(
        OUTPUT_PATH + "state_level_features.csv",
        index=False
    )

if __name__ == "__main__":
    aggregate_state_level()
