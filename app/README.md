# Kola Market Inventory Recommendation API

This FastAPI app provides product recommendations for inventory planning in Ghanaian towns using real Google Trends data and a machine learning model.

## Features

- `/recommend` endpoint: Get top product recommendations for a region and quarter.
- Uses a trained Random Forest model and label encoders.
- Ready for production deployment (see requirements.txt).

## Folder Structure

```
app/
  main.py           # FastAPI app
  requirements.txt  # Python dependencies
  models/           # Trained model and encoders (joblib files)
  README.md         # This file
```

## Usage

1. Place the trained model and encoder files in `app/models/`:
   - `rf_model.joblib`
   - `le_region.joblib`
   - `le_quarter.joblib`
   - `le_product.joblib`
2. Place `ghana_product_trends.csv` in the project root.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Access the docs at `http://127.0.0.1:8000/docs`

## Extending & Integrating

- Integrate with WhatsApp or dashboards via the API.
- Add more endpoints for explainability or batch recommendations.
- Deploy on cloud (Azure, AWS, GCP) for scalability.

## Data & Model

- Data sourced from Google Trends, World Bank, and Ghana Statistical Service.
- Model: Random Forest regressor trained on real trend data.

---

For more, see the notebook for data sourcing, logic, and model training.

# FastAPI Application

This folder contains the production-ready FastAPI application for Inventory Recommendations.

## Structure

- `main.py`: Entry point for the FastAPI server.
- `models/`: Contains the serialized machine learning models and encoders.
- `schemas/`: Contains Pydantic models for request and response validation.
- `utils/`: Utility functions and helper scripts.

## Setup

1. Install dependencies from the project root:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Access the interactive API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Testing

- Place tests in the `../tests` directory and run them using your preferred test runner.

## Deployment

For production deployments, consider using a process manager (e.g., Gunicorn) with Uvicorn workers behind a reverse proxy (e.g., NGINX).

## License

MIT License
