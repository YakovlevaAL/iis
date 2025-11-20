#!/bin/bash
echo "Starting MLflow server with SQLite backend..."
mlflow server --backend-store-uri sqlite:///mlruns.db --host 0.0.0.0 --port 5000
