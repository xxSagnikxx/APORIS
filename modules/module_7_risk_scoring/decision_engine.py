import pandas as pd
OUTPUT_PATH = "../../outputs/reports/"
def assign_decisions():
    df = pd.read_csv(OUTPUT_PATH + "risk_scores.csv")
    def risk_level(score):
        if score >= 75:
            return "Critical"
        elif score >= 50:
            return "High"
        elif score >= 25:
            return "Medium"
        else:
            return "Low"
    def decision_action(level):
        if level == "Critical":
            return "Immediate audit and operational intervention"
        elif level == "High":
            return "Increase monitoring and resource allocation"
        elif level == "Medium":
            return "Routine monitoring and preventive action"
        else:
            return "No immediate action required"
    df["risk_level"] = df["risk_score"].apply(risk_level)
    df["recommended_action"] = df["risk_level"].apply(decision_action)
    df.to_csv(OUTPUT_PATH + "risk_decisions.csv", index=False)
if __name__ == "__main__":
    assign_decisions()
