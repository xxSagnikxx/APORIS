import pandas as pd
from load_time_series import load_daily_series

#forecast ar real data compare korar jonne

OUTPUT_PATH = "../../outputs/reports/"

def evaluate_forecast():
    actual = load_daily_series()
    forecast = pd.read_csv(OUTPUT_PATH + "enrolment_forecast.csv")

    actual = actual.rename(columns={
        "date": "ds",
        "total_enrolments": "actual"
    })

    merged = actual.merge(forecast, on="ds", how="inner")

    merged["error"] = merged["actual"] - merged["yhat"]
    merged["absolute_error"] = merged["error"].abs()

    merged.to_csv(OUTPUT_PATH + "forecast_evaluation.csv", index=False)

if __name__ == "__main__":
    evaluate_forecast()
