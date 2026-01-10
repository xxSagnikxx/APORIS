import pandas as pd
from prophet import Prophet
from load_time_series import load_daily_series

#update volume predict korar jonne

OUTPUT_PATH = "../../outputs/reports/"

def forecast_updates(days=30):
    df = load_daily_series()

    prophet_df = df[["date", "total_updates"]]
    prophet_df.columns = ["ds", "y"]

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )

    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    forecast[[
        "ds",
        "yhat",
        "yhat_lower",
        "yhat_upper"
    ]].to_csv(OUTPUT_PATH + "update_forecast.csv", index=False)

if __name__ == "__main__":
    forecast_updates(30)
