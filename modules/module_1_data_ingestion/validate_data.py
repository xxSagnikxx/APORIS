import pandas as pd
import os
BASE_DIR = os.path.dirname(__file__)
CLEAN_DIR = os.path.join(BASE_DIR, "clean_data")
def validate_file(file_name):
    path = os.path.join(CLEAN_DIR, file_name)
    if not os.path.exists(path):
        print(f"{file_name} not found")
        return
    df = pd.read_csv(path)
    print(f"{file_name}")
    print(f"  Rows: {len(df)} | Columns: {len(df.columns)}")
if __name__ == "__main__":
    validate_file("enrolment_cleaned.csv")
    validate_file("demographic_updates_cleaned.csv")
    validate_file("biometric_updates_cleaned.csv")
