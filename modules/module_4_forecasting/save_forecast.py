import pandas as pd
OUTPUT_PATH = "../../outputs/reports/"
def prepare_forecast_summary():
    enrol = pd.read_csv(OUTPUT_PATH + "enrolment_forecast.csv")
    update = pd.read_csv(OUTPUT_PATH + "update_forecast.csv")
    summary = enrol.merge(
        update,
        on="ds",
        suffixes=("_enrol", "_update")
    )
    summary.to_csv(OUTPUT_PATH + "forecast_master_summary.csv", index=False)
if __name__ == "__main__":
    prepare_forecast_summary()
