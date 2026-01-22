import pandas as pd
import os

FEATURE_PATH = "data/features/"

# load state level features
state_file = os.path.join(FEATURE_PATH, "state_level_features.csv")

if not os.path.exists(state_file):
    raise FileNotFoundError("state_level_features.csv not found")

state = pd.read_csv(state_file)

# create final dataset directly
state.to_csv("data/final_dataset.csv", index=False)

print("✔ final_dataset.csv created successfully")
