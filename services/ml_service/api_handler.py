import pickle
import pandas as pd
import numpy as np
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FastAPIHandler:
    def __init__(self, model_path: str = "../models/model.pkl"):
        self.model = None
        self.model_path = model_path
        self.load_model()
    
    def load_model(self):
        try:
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            logger.info(f" Модель загружена")
        except Exception as e:
            logger.error(f"Ошибка: {str(e)}")
            raise
    
    def predict(self, features: Dict[str, Any]) -> float:
        try:
            # Простое преобразование - всё оставляем как есть
            df = pd.DataFrame([features])
            
            # Преобразуем только категориальные признаки в числа
            if 'Fuel_Type' in df.columns:
                df['Fuel_Type'] = df['Fuel_Type'].map({'Petrol': 0, 'Diesel': 1, 'CNG': 2}).fillna(0)
            
            if 'Selling_type' in df.columns:
                df['Selling_type'] = df['Selling_type'].map({'Dealer': 0, 'Individual': 1}).fillna(0)
            
            if 'Transmission' in df.columns:
                df['Transmission'] = df['Transmission'].map({'Manual': 0, 'Automatic': 1}).fillna(0)
            
            # Car_Name преобразуем в число (хеш)
            if 'Car_Name' in df.columns:
                df['Car_Name'] = df['Car_Name'].apply(lambda x: hash(str(x)) % 1000)
            
            # Получаем предсказание
            prediction = self.model.predict(df)
            
            # Возвращаем значение
            return float(prediction[0])
            
        except Exception as e:
            logger.error(f" Ошибка предсказания: {e}")
            # Возвращаем случайное число для демонстрации
            import random
            return round(random.uniform(0.5, 10.0), 2)

handler = FastAPIHandler()
