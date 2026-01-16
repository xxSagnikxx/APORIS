import pandas as pd

#feature sanity check korar jonne

FEATURE_PATH = "../../data/features/"

def generate_summary():
    state = pd.read_csv(FEATURE_PATH + "state_level_features.csv")
    district = pd.read_csv(FEATURE_PATH + "district_level_features.csv")
    daily = pd.read_csv(FEATURE_PATH + "daily_time_series.csv")

    print("State features:", state.shape)
    print("District features:", district.shape)
    print("Daily series:", daily.shape)

if __name__ == "__main__":
    generate_summary()
