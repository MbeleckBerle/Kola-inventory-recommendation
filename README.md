# Kola Inventory Recommendation Prototype

This repository implements a data-driven inventory recommendation system for two Ghanaian towns—**Accra** (urban/coastal) and **Tamale** (northern/savannah). It includes:

- A Jupyter notebook for data exploration and model training
- A FastAPI service exposing a recommendation endpoint
- Machine learning model artifacts (Random Forest) and encoders
- Suggestions for WhatsApp integration via Azure Bot Service

## Folder Structure

```
Kola-inventory-recommendation/
│
├── app/
│   ├── main.py            # FastAPI application entry point
│   ├── notebook/          # Jupyter notebook for data analysis and ML
│   ├── models/            # Trained model and encoder artifacts
│   └── utils/             # Utility functions (if any)
│
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation (this file)
└── docs/                  # Documentation templates (e.g., Overleaf .tex)
```

## Installation

1. Clone the repository:
   ```powershell
   git clone https://github.com/MbeleckBerle/Kola-inventory-recommendation.git
   cd Kola-inventory-recommendation
   ```
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the Jupyter Notebook

1. Install Jupyter:
   ```powershell
   pip install notebook
   ```
2. Launch the notebook:
   ```powershell
   jupyter notebook app/notebook/inventory_recommendation.ipynb
   ```
3. Follow cells to fetch data, train the model, and visualize results.

## FastAPI Recommendation Service

1. Ensure model artifacts are available in `app/models/` (exported from the notebook).
2. Start the API server:
   ```powershell
   uvicorn app.main:app --reload --port 8000
   ```
3. Access the interactive Swagger UI:
   `http://localhost:8000/docs`
4. Example request:
   ```url
   GET http://localhost:8000/recommend?town=Accra&quarter=Q2&top_n=5
   ```

## Dependencies

Key packages are listed in `requirements.txt`:

- pandas, numpy
- scikit-learn
- pytrends
- fastapi, uvicorn
- joblib

## Documentation

- Overleaf LaTeX template: `docs/overleaf.tex`
- Use it to generate a full project report.

## Future Enhancements

- Integrate real-time sales and weather data
- Deploy a web dashboard for interactive queries
- Implement WhatsApp channel via Azure Bot Service
- Explore time series forecasting models (ARIMA, LSTM)

## Folder Structure

- `app/`
  - `main.py`: FastAPI application entry point.
  - `models/`: Serialized machine learning models and related files.
  - `schemas/`: Pydantic models for request/response validation.
  - `utils/`: Utility functions and helper scripts.
- `tests/`: Automated tests for the application.
- `requirements.txt`: Project dependencies.
- `README.md`: Project documentation.
- `.gitignore`: Files and folders to be ignored by Git.

## Setup Instructions

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI app using Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```

## Deployment

For production deployment, consider using a process manager like Gunicorn or Uvicorn with workers behind a reverse proxy (NGINX).

## Render hosting: https://kola-inventory-recommendation.onrender.com/docs
