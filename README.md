# Project Title

A production-ready FastAPI application for inventory recommendations. This project is structured with clear separation of concerns for models, schemas, utilities, and tests.

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
