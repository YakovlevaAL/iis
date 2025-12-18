from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Union
from api_handler import handler  # Импортируем наш обработчик

# Создаем экземпляр FastAPI приложения
app = FastAPI()

# Определяем модель данных для запроса на основе ваших данных
class PredictionRequest(BaseModel):
    Car_Name: str
    Year: int
    Present_Price: float
    Driven_kms: int
    Fuel_Type: str
    Selling_type: str
    Transmission: str
    Owner: int
    
    # Пример для документации
    class Config:
        schema_extra = {
            "example": {
                "Car_Name": "verna",
                "Year": 2015,
                "Present_Price": 9.4,
                "Driven_kms": 61381,
                "Fuel_Type": "Petrol",
                "Selling_type": "Dealer",
                "Transmission": "Manual",
                "Owner": 0
            }
        }

# Обработка GET-запросов к корню приложения /
@app.get("/")
async def root():
    return {"Hello": "World"}

# Создаем endpoint /api/prediction для предсказаний
@app.post("/api/prediction")
async def predict(item_id: int, request: PredictionRequest):
    """
    Endpoint для получения предсказаний цены автомобиля
    
    Args:
        item_id: ID объекта (автомобиля)
        request: Признаки автомобиля для предсказания цены
    
    Returns:
        Словарь с ID объекта и предсказанной ценой
    """
    try:
        # Преобразуем запрос в словарь
        features = request.dict()
        
        # Получаем предсказание из handler
        prediction = handler.predict(features)
        
        return {
            "item_id": item_id,
            "price": prediction
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

# Добавляем endpoint для проверки здоровья сервиса
@app.get("/health")
async def health_check():
    """Endpoint для проверки здоровья сервиса"""
    return {
        "status": "healthy", 
        "model_loaded": handler.model is not None,
        "service": "car_price_prediction"
    }

@app.get("/model-info")
async def model_info():
    """Endpoint для получения информации о модели"""
    if handler.model is None:
        return {"error": "Model not loaded"}
    
    info = {
        "model_type": str(type(handler.model)),
        "features_count": getattr(handler.model, 'n_features_in_', 'unknown'),
    }
    
    if hasattr(handler.model, 'feature_names_in_'):
        info["feature_names"] = list(handler.model.feature_names_in_)
    
    return info
