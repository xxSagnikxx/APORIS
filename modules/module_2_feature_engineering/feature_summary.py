import pandas as pd
import os
BASE = os.path.join("data", "features")
def generate_summary():
    for f in os.listdir(BASE):
        df = pd.read_csv(os.path.join(BASE, f))
        print(f"\n=== {f} ===")
        print(df.head())
if __name__ == "__main__":
    generate_summary()
