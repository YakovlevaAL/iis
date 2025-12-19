import requests
import json

url = "http://localhost:8000/api/prediction?item_id=777"
data = {
    "Car_Name": "Test Car",
    "Year": 2020,
    "Present_Price": 10.0,
    "Driven_kms": 10000,
    "Fuel_Type": "Petrol",
    "Selling_type": "Dealer",
    "Transmission": "Automatic",
    "Owner": 0
}

print(f"Отправка запроса на {url}")
print(f"Данные: {json.dumps(data, indent=2)}")

try:
    response = requests.post(url, json=data, timeout=10)
    print(f"✅ Статус: {response.status_code}")
    print(f"✅ Ответ: {response.json()}")
except requests.exceptions.ConnectionError as e:
    print(f"❌ Ошибка подключения: {e}")
except Exception as e:
    print(f"❌ Другая ошибка: {e}")
