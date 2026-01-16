import pandas as pd

#cleaned data load korar jonne

DATA_PATH = "../../data/cleaned/"

def load_enrolment():
    df = pd.read_csv(DATA_PATH + "enrolment_cleaned.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

def load_demographic_updates():
    df = pd.read_csv(DATA_PATH + "demographic_updates_cleaned.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

def load_biometric_updates():
    df = pd.read_csv(DATA_PATH + "biometric_updates_cleaned.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df
