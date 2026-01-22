import pandas as pd
OUTPUT_PATH = "../../outputs/reports/"
def generate_master_report():
    state = pd.read_csv(OUTPUT_PATH + "state_summary.csv")
    quality = pd.read_csv(OUTPUT_PATH + "quality_scores.csv")
    demo = pd.read_csv(OUTPUT_PATH + "demographic_summary.csv")
    final = state.merge(quality, on="state", how="left")
    final = final.merge(demo, on="state", how="left")
    final.to_csv(OUTPUT_PATH + "module_3_master_summary.csv", index=False)
if __name__ == "__main__":
    generate_master_report()
