import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

print("Создаем простую совместимую модель...")

np.random.seed(42)
X_train = np.random.rand(100, 8)
y_train = 0.5 + 9.5 * np.random.rand(100)  # Цены от 0.5 до 10.0

model = RandomForestRegressor(n_estimators=5, random_state=42)
model.fit(X_train, y_train)

# Сохраняем
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Модель создана!")
