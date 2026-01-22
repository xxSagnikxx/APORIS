import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
RAW_DIR = os.path.join(BASE_DIR, "Raw_data")
OUT_DIR = os.path.join(BASE_DIR, "clean_data")

os.makedirs(OUT_DIR, exist_ok=True)


def load_and_concat(folder_path):
    dfs = []
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            dfs.append(pd.read_csv(os.path.join(folder_path, file)))
    return pd.concat(dfs, ignore_index=True)


def clean_enrolment():
    path = os.path.join(RAW_DIR, "Aadhar_data_enrolment")
    df = load_and_concat(path)

    # basic standardization
    df.columns = df.columns.str.lower().str.strip()
    df = df.dropna(how="all")

    df.to_csv(os.path.join(OUT_DIR, "enrolment_cleaned.csv"), index=False)
    print("✔ enrolment_cleaned.csv saved")


def clean_demographic():
    path = os.path.join(RAW_DIR, "Aadhar_data_demographic")
    df = load_and_concat(path)

    df.columns = df.columns.str.lower().str.strip()
    df = df.dropna(how="all")

    df.to_csv(os.path.join(OUT_DIR, "demographic_updates_cleaned.csv"), index=False)
    print("✔ demographic_updates_cleaned.csv saved")


def clean_biometric():
    path = os.path.join(RAW_DIR, "Aadhar_data_biometric")
    df = load_and_concat(path)

    df.columns = df.columns.str.lower().str.strip()
    df = df.dropna(how="all")

    df.to_csv(os.path.join(OUT_DIR, "biometric_updates_cleaned.csv"), index=False)
    print("✔ biometric_updates_cleaned.csv saved")


if __name__ == "__main__":
    clean_enrolment()
    clean_demographic()
    clean_biometric()
