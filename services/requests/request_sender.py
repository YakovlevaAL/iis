
import requests as http_requests
import time
import random
import logging
def main():
    # Определяем URL
    if os.getenv('DOCKER_ENV') == 'true':
        PREDICTION_SERVICE_URL = "http://ml_service:8000"
    else:
        PREDICTION_SERVICE_URL = "http://localhost:8000"
    
    logger.info(f" Запуск скрипта запросов к {PREDICTION_SERVICE_URL}")


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

#
import os



SAMPLE_DATA = [
    {
        "item_id": 1,
        "car_data": {
            "Car_Name": "Toyota Corolla",
            "Year": 2015,
            "Present_Price": 7.5,
            "Driven_kms": 75000,
            "Fuel_Type": "Petrol",
            "Selling_type": "Dealer",
            "Transmission": "Manual",
            "Owner": 1
        }
    },
    {
        "item_id": 2,
        "car_data": {
            "Car_Name": "Honda Civic",
            "Year": 2018,
            "Present_Price": 12.0,
            "Driven_kms": 35000,
            "Fuel_Type": "Petrol",
            "Selling_type": "Individual",
            "Transmission": "Automatic",
            "Owner": 0
        }
    },
    {
        "item_id": 3,
        "car_data": {
            "Car_Name": "Hyundai Creta",
            "Year": 2020,
            "Present_Price": 15.5,
            "Driven_kms": 15000,
            "Fuel_Type": "Diesel",
            "Selling_type": "Dealer",
            "Transmission": "Automatic",
            "Owner": 1
        }
    }
]

def send_prediction_request(data):
    """Отправляет запрос на предсказание"""
    try:
        item_id = data["item_id"]
        car_data = data["car_data"]
        
        url = f"{PREDICTION_SERVICE_URL}/api/prediction?item_id={item_id}"
        logger.info(f"Отправка запроса ID {item_id} на {url}")
        
        response = http_requests.post(
            url,
            json=car_data,
            timeout=10
        )
        
        if response.status_code == 200:
            prediction = response.json()
            logger.info(f"✅ Успешный запрос ID {item_id}. Предсказание: {prediction}")
            return True, prediction
        else:
            logger.error(f"❌ Ошибка запроса ID {item_id}. Код: {response.status_code}, Ответ: {response.text}")
            return False, None
            
    except http_requests.exceptions.ConnectionError:
        logger.error("❌ Не удалось подключиться к сервису предсказаний")
        return False, None
    except Exception as e:
        logger.error(f"❌ Неожиданная ошибка: {str(e)}")
        return False, None

def main():
    """Основная функция отправки запросов"""
    logger.info(f"🚀 Запуск скрипта отправки запросов к {PREDICTION_SERVICE_URL}")
    
    request_count = 0
    successful_requests = 0
    
    try:
        while True:
            # Выбор случайных данных
            data = random.choice(SAMPLE_DATA)
            
            # Отправка запроса
            request_count += 1
            logger.info(f"📤 Отправка запроса #{request_count} (ID {data['item_id']})")
            
            success, prediction = send_prediction_request(data)
            if success:
                successful_requests += 1
            
            # Случайная задержка от 0 до 5 секунд
            delay = random.uniform(0, 5)
            logger.info(f"⏱️  Ожидание {delay:.2f} секунд...")
            time.sleep(delay)
            
            # Статистика каждые 10 запросов
            if request_count % 10 == 0:
                success_rate = (successful_requests / request_count) * 100
                logger.info(f"📊 Статистика: {request_count} запросов, {success_rate:.1f}% успешных")
                
    except KeyboardInterrupt:
        success_rate = (successful_requests / max(request_count, 1)) * 100
        logger.info(f"🛑 Остановлено. Итог: {request_count} запросов, {success_rate:.1f}% успешных")

if __name__ == "__main__":
    main()
EOF