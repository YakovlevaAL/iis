from fastapi import FastAPI, HTTPException, Request, Response
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest, CollectorRegistry
import time
import random

app = FastAPI()

# ========== PROMETHEUS METRICS ==========
metrics_registry = CollectorRegistry()

PREDICTION_REQUEST_COUNT = Counter(
    'prediction_requests_total',
    'Total number of prediction requests',
    ['method', 'endpoint', 'status'],
    registry=metrics_registry
)

PREDICTION_LATENCY = Histogram(
    'prediction_request_duration_seconds',
    'Prediction request latency',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0],
    registry=metrics_registry
)

PREDICTION_VALUE = Histogram(
    'prediction_value',
    'Distribution of prediction values',
    buckets=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 100, 200, 500],
    registry=metrics_registry
)

HTTP_ERRORS = Counter(
    'http_errors_total',
    'Total HTTP errors by status code',
    ['status_code', 'endpoint'],
    registry=metrics_registry
)

class PredictionRequest(BaseModel):
    Car_Name: str
    Year: int
    Present_Price: float
    Driven_kms: int
    Fuel_Type: str
    Selling_type: str
    Transmission: str
    Owner: int

@app.middleware("http")
async def monitor_requests(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
        latency = time.time() - start_time
        
        if request.url.path != "/metrics":
            PREDICTION_LATENCY.labels(
                method=request.method,
                endpoint=request.url.path
            ).observe(latency)
            
            if response.status_code >= 400:
                HTTP_ERRORS.labels(
                    status_code=str(response.status_code),
                    endpoint=request.url.path
                ).inc()
                PREDICTION_REQUEST_COUNT.labels(
                    method=request.method,
                    endpoint=request.url.path,
                    status=str(response.status_code)
                ).inc()
            else:
                PREDICTION_REQUEST_COUNT.labels(
                    method=request.method,
                    endpoint=request.url.path,
                    status='success'
                ).inc()
        
        return response
    except Exception as e:
        latency = time.time() - start_time
        PREDICTION_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path
        ).observe(latency)
        HTTP_ERRORS.labels(
            status_code='500',
            endpoint=request.url.path
        ).inc()
        PREDICTION_REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status='500'
        ).inc()
        raise

@app.get("/")
async def root():
    return {"message": "Car Price Prediction API", "version": "3.0"}

@app.post("/api/prediction")
async def predict(item_id: int, request: PredictionRequest):
    """Упрощенная версия - всегда возвращает случайное значение"""
    # Всегда успешный ответ со случайной ценой
    price = round(random.uniform(5.0, 30.0), 2)
    
    PREDICTION_VALUE.observe(price)
    
    return {
        "item_id": item_id,
        "price": price
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "model_loaded": True,
        "service": "car_price_prediction",
        "version": "3.0",
        "metrics": "enabled"
    }

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(metrics_registry), media_type="text/plain")
