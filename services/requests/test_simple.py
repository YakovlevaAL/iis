import requests
print("Тест библиотеки requests...")
print(f"Версия requests: {requests.__version__}")

# Тестовый запрос
data = {"Car_Name": "test", "Year": 2020, "Present_Price": 15.0, "Driven_kms": 10000, "Fuel_Type": "Petrol", "Selling_type": "Dealer", "Transmission": "Automatic", "Owner": 0}

try:
    response = requests.post(
        "http://localhost:8000/api/prediction?item_id=999",
        json=data,
        timeout=5
    )
    print(f"✅ Запрос отправлен. Статус: {response.status_code}")
    print(f"Ответ: {response.text[:100]}")
except Exception as e:
    print(f"❌ Ошибка: {type(e).__name__}: {e}")
