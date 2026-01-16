import pandas as pd
import joblib

#trained model diye cause predict korar jonne

DATA_PATH = "../../outputs/reports/"
MODEL_PATH = "../../outputs/models/"
OUTPUT_PATH = "../../outputs/reports/"

def predict():
    df = pd.read_csv(DATA_PATH + "anomaly_detection_results.csv")

    model = joblib.load(MODEL_PATH + "cause_classifier.pkl")
    encoder = joblib.load(MODEL_PATH + "cause_label_encoder.pkl")

    features = df[[
        "update_ratio",
        "quality_score",
        "future_load_pressure"
    ]]

    predicted = model.predict(features)
    df["predicted_cause"] = encoder.inverse_transform(predicted)

    df.to_csv(OUTPUT_PATH + "cause_predictions.csv", index=False)

if __name__ == "__main__":
    predict()
