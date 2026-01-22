import pandas as pd
import os
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..", "modules", "module_1_data_ingestion", "clean_data")
)
def load_enrolment():
    return pd.read_csv(os.path.join(DATA_DIR, "enrolment_cleaned.csv"))
def load_demographic():
    return pd.read_csv(os.path.join(DATA_DIR, "demographic_updates_cleaned.csv"))
def load_biometric():
    return pd.read_csv(os.path.join(DATA_DIR, "biometric_updates_cleaned.csv"))
