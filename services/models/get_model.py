import mlflow
import mlflow.sklearn
import pickle
import os
from pathlib import Path

# Конфигурация
MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"  # адрес MLflow сервера
MODEL_RUN_ID = "d41f835a433f4372a3ad10ba62def68e"  # RUN_ID из MLflow (ваш может отличаться!)
OUTPUT_PATH = "model.pkl"

def download_model_from_mlflow():
    """
    Загрузка модели из MLflow по run_id
    """
    # Устанавливаем URI MLflow
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    
    print(f"Подключаемся к MLflow по адресу: {MLFLOW_TRACKING_URI}")
    print(f"Загружаем модель с run_id: {MODEL_RUN_ID}")
    print(f"Сохраняем модель в файл: {OUTPUT_PATH}")
    
    try:
        # Способ 1: Если модель залогирована как sklearn (скорее всего)
        model = mlflow.sklearn.load_model(f"runs:/{MODEL_RUN_ID}/model")
        
        # Способ 2: Если не сработает, попробуйте так:
        # model = mlflow.pyfunc.load_model(f"runs:/{MODEL_RUN_ID}/model")
        
        # Сохраняем модель в файл
        with open(OUTPUT_PATH, 'wb') as f:
            pickle.dump(model, f)
        
        print(f"Модель успешно сохранена в {OUTPUT_PATH}")
        print(f"Тип модели: {type(model)}")
        
        # Проверяем размер файла
        file_size = os.path.getsize(OUTPUT_PATH) / 1024  # в КБ
        print(f"Размер файла модели: {file_size:.2f} KB")
        
        # Проверяем, есть ли у модели метод predict
        if hasattr(model, 'predict'):
            print("У модели есть метод predict ✓")
        else:
            print("Внимание: у модели нет метода predict!")
            
    except Exception as e:
        print(f"Ошибка при загрузке модели: {str(e)}")
        print("\nВозможные решения:")
        print("1. Убедитесь, что MLflow сервер запущен")
        print("2. Проверьте правильность run_id")
        print("3. Проверьте, что модель действительно сохранена в MLflow")
        raise

if __name__ == "__main__":
    download_model_from_mlflow()