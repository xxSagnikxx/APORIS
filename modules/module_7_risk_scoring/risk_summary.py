import pandas as pd

#final executive summary ber korar jonne

OUTPUT_PATH = "../../outputs/reports/"

def generate_risk_summary():
    df = pd.read_csv(OUTPUT_PATH + "risk_decisions.csv")

    summary = df[[
        "state",
        "risk_score",
        "risk_level",
        "predicted_cause",
        "recommended_action"
    ]]

    summary.to_csv(OUTPUT_PATH + "final_risk_summary.csv", index=False)

if __name__ == "__main__":
    generate_risk_summary()
