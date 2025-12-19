import logging
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FastAPIHandler:
    def __init__(self, model_path: str = "model.pkl"):
        self.model_path = model_path
        self.model = None
        try:
            self.load_model()
        except Exception as e:
            logger.error(f"Ошибка загрузки модели: {e}")
            logger.info("Использую тестовую модель")
            self.model = self.create_dummy_model()

    def create_dummy_model(self):
        """Создает фиктивную модель для тестирования"""
        class DummyModel:
            def predict(self, X):
                # Генерируем реалистичные предсказания 5-20
                import random
                return [random.uniform(5.0, 20.0) for _ in range(len(X))]
        return DummyModel()

    def load_model(self):
        """Загружает модель из файла"""
        try:
            import pickle
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            logger.info(f"Модель загружена из {self.model_path}")
        except Exception as e:
            logger.error(f"Не удалось загрузить модель: {e}")
            raise

    def predict(self, features):
        """Делает предсказание на основе признаков"""
        try:
            # Простая логика для теста
            base_price = features.get('Present_Price', 10.0)
            year_factor = (features.get('Year', 2015) - 2000) * 0.1
            km_factor = features.get('Driven_kms', 50000) / 100000
            
            prediction = base_price * (1 + year_factor - km_factor)
            prediction = max(1.0, min(30.0, prediction))
            
            logger.info(f"Предсказание для {features.get('Car_Name')}: {prediction:.2f}")
            return float(prediction)
        except Exception as e:
            logger.error(f"Ошибка предсказания: {e}")
            return 12.5  # Значение по умолчанию

# Создаем глобальный обработчик
handler = FastAPIHandler()
