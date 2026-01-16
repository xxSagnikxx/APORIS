import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib

#ML model training ekhane hobe

DATA_PATH = "../../outputs/reports/"
MODEL_PATH = "../../outputs/models/"

def train_model():
    df = pd.read_csv(DATA_PATH + "cause_labeled_data.csv")

    features = df[[
        "update_ratio",
        "quality_score",
        "future_load_pressure"
    ]]

    labels = df["cause_label"]

    encoder = LabelEncoder()
    y = encoder.fit_transform(labels)

    X_train, X_test, y_train, y_test = train_test_split(
        features, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))

    joblib.dump(model, MODEL_PATH + "cause_classifier.pkl")
    joblib.dump(encoder, MODEL_PATH + "cause_label_encoder.pkl")

if __name__ == "__main__":
    train_model()
