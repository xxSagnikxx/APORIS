import pandas as pd
from load_inputs import load_quality_scores, load_forecast_summary
OUTPUT_PATH = "../../outputs/reports/"
def prepare_features():
    quality = load_quality_scores()
    forecast = load_forecast_summary()
    df = quality.copy()
    forecast["ds"] = pd.to_datetime(forecast["ds"])
    last_date = forecast["ds"].max()
    future_load = forecast[forecast["ds"] > last_date - pd.Timedelta(days=7)]
    avg_future_enrol = future_load["yhat_enrol"].mean()
    df["future_load_pressure"] = avg_future_enrol
    df["future_load_type"] = "national_forecast"
    df["inverse_quality"] = 100 - df["quality_score"]
    df.to_csv(OUTPUT_PATH + "anomaly_features.csv", index=False)
if __name__ == "__main__":
    prepare_features()
