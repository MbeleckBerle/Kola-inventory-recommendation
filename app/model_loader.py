import os
import pandas as pd
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), "models")
TREND_CSV = os.path.join(os.path.dirname(__file__), "..", "ghana_product_trends.csv")


def load_artifacts():
    trends_long = pd.read_csv(TREND_CSV, parse_dates=["date"])
    le_region = joblib.load(os.path.join(MODEL_PATH, "le_region.joblib"))
    le_quarter = joblib.load(os.path.join(MODEL_PATH, "le_quarter.joblib"))
    le_product = joblib.load(os.path.join(MODEL_PATH, "le_product.joblib"))
    rf = joblib.load(os.path.join(MODEL_PATH, "rf_model.joblib"))
    return trends_long, le_region, le_quarter, le_product, rf
