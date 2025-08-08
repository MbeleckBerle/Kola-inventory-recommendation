from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from typing import List, Optional
import pandas as pd
import numpy as np
import joblib
import os

app = FastAPI(title="Kola Market Inventory Recommendation API")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "models")
TREND_CSV = os.path.join(os.path.dirname(__file__), "data", "ghana_product_trends.csv")

trends_long = None
le_region = None
le_quarter = None
le_product = None
rf = None


def load_artifacts():
    global trends_long, le_region, le_quarter, le_product, rf
    trends_long = pd.read_csv(TREND_CSV, parse_dates=["date"])
    le_region = joblib.load(os.path.join(MODEL_PATH, "le_region.joblib"))
    le_quarter = joblib.load(os.path.join(MODEL_PATH, "le_quarter.joblib"))
    le_product = joblib.load(os.path.join(MODEL_PATH, "le_product.joblib"))
    rf = joblib.load(os.path.join(MODEL_PATH, "rf_model.joblib"))


@app.on_event("startup")
def startup_event():
    load_artifacts()


@app.post("/recommend")
async def recommend_products(
    region: str = Form(..., description="Region name, e.g. Accra or Tamale"),
    quarter: str = Form(..., description="Quarter, e.g. Q2 or Q4"),
    top_n: int = Form(5, description="Number of top products to recommend"),
):
    region = region.title()
    quarter = quarter.upper()
    region_enc = le_region.transform([region])[0]
    quarter_enc = le_quarter.transform([quarter])[0]
    products = le_product.classes_
    product_encs = le_product.transform(products)
    X_pred = pd.DataFrame(
        {
            "region_enc": region_enc,
            "quarter_enc": quarter_enc,
            "product_enc": product_encs,
        }
    )
    preds = rf.predict(X_pred)
    top_idx = np.argsort(preds)[::-1][:top_n]
    recommendations = [products[i] for i in top_idx]
    scores = [float(preds[i]) for i in top_idx]
    return JSONResponse(
        {
            "region": region,
            "quarter": quarter,
            "recommendations": recommendations,
            "scores": scores,
        }
    )


@app.get("/")
def root():
    return {
        "message": "Kola Market Inventory Recommendation API. Use /recommend endpoint."
    }
