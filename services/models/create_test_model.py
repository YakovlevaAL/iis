import pickle
from sklearn.ensemble import RandomForestRegressor
import numpy as np

print("Создаем тестовую модель для автомобилей...")

# Создаем тестовую модель
np.random.seed(42)

# Генерируем тестовые данные (100 примеров, 8 признаков)
X_train = np.random.rand(100, 8)
# Цены от 0.1 до 15.0 (типичный диапазон для автомобилей в ваших данных)
y_train = 0.1 + 14.9 * np.random.rand(100)

model = RandomForestRegressor(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# Устанавливаем имена признаков (важно для порядка колонок)
model.feature_names_in_ = np.array(['Car_Name', 'Year', 'Present_Price', 'Driven_kms', 
                                    'Fuel_Type', 'Selling_type', 'Transmission', 'Owner'])

# Сохраняем модель
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Тестовая модель создана!")
print(f"Размер файла: {len(pickle.dumps(model)) / 1024:.1f} KB")

# Тестовое предсказание
test_data = X_train[0].reshape(1, -1)
prediction = model.predict(test_data)[0]
print(f"Тестовое предсказание: {prediction:.2f}")
