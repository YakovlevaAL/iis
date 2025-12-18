import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

print("Создаем исправленную модель...")

# Создаем тестовую модель с 8 признаками
np.random.seed(42)
X_train = np.random.rand(100, 8)
y_train = 0.1 + 14.9 * np.random.rand(100)

model = RandomForestRegressor(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# Устанавливаем правильные имена признаков (включая Car_Name)
model.feature_names_in_ = np.array([
    'Car_Name', 'Year', 'Present_Price', 'Driven_kms',
    'Fuel_Type', 'Selling_type', 'Transmission', 'Owner'
])

# Сохраняем модель
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Новая модель создана!")
print(f"Размер файла: {len(pickle.dumps(model)) / 1024:.1f} KB")
print(f"Признаки модели: {list(model.feature_names_in_)}")
print(f"Количество признаков: {model.n_features_in_}")
