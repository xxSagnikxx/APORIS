import pandas as pd
from load_features import load_time_series

#time based trend ar volatility bojhar jonne

OUTPUT_PATH = "../../outputs/reports/"

def analyze_temporal_trends():
    df = load_time_series()

    df["date"] = pd.to_datetime(df["date"])

    df["rolling_mean_7"] = df["total_enrolments"].rolling(7).mean()
    df["rolling_std_7"] = df["total_enrolments"].rolling(7).std()

    df.to_csv(OUTPUT_PATH + "temporal_trends.csv", index=False)

if __name__ == "__main__":
    analyze_temporal_trends()
