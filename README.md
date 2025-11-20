
Проект направлен на прогнозирование стоимости подержанных автомобилей на основе их характеристик. Используется датасет Car Price Prediction с Kaggle, содержащий информацию о марке, годе выпуска, пробеге, типе топлива и других параметрах автомобилей.>


## Запуск проекта

### Клонирование репозитория
```bash
git clone <https://github.com/YakovlevaAL/iis/tree/main>
cd /iis


Установка и активация виртуального окружения
python3 -m venv .venv_my_proj
source .venv_my_proj/bin/activate


Установка зависимостей
pip install -r requirements.txt

Структура проекта
my_proj/
├── data/                 # Исходные и обработанные данные
│   ├── car_data.csv      # Исходный датасет
│   └── clean_car_data.pkl # Очищенный датасет
├── eda/                  # Разведочный анализ данных
│   ├── eda.ipynb         # Блокнот с анализом
│   ├── correlation_heatmap.png
│   ├── interactive_scatter.png
│   ├── price_distribution.png
│   ├── price_vs_year_mileage.png
│   └── price_by_fuel_transmission.png
├── .venv_my_proj/        # Виртуальное окружение
├── .gitignore            # Исключения для Git
├── requirements.txt      # Зависимости проекта
└── README.md            # Документация

### Структура очищенных данных

После обработки датасет содержит:
- ** 299 Записей**: 

**Признаки:**
- `Car_Name` - название автомобиля (object)
- `Year` - год выпуска (int64)
- `Selling_Price` - цена продажи (float64)
- `Present_Price` - текущая рыночная цена (float64)
- `Driven_kms` - пробег (int64)
- `Fuel_Type` - тип топлива (category)
- `Selling_type` - тип продавца (category)
- `Transmission` - тип трансмиссии (category)
- `Owner` - количество владельцев (int64)
- `Car_Age` - возраст автомобиля (int64)



Вывод по графику price_vs_year_mileage.png: Распределение цен продажи имеет правостороннюю асимметрию. Большинство автомобилей продаются в диапазоне 2-10 , при этом присутствуют выбросы - автомобили премиум-сегмента с ценами выше 15. Медианная цена составляет около 5-6.

Вывод по графику price_distribution.png: Наблюдается сильная положительная корреляция между годом выпуска и ценой - более новые автомобили стоят дороже. Отрицательная корреляция с пробегом - автомобили с большим пробегом дешевеют. При этом зависимость нелинейная.

Вывод по графику price_by_fuel_transmission.png: Дизельные автомобили в среднем дороже бензиновых, а автомобили с автоматической трансмиссией значительно дороже механических. Тип топлива CNG ассоциируется с самыми низкими ценами.

Вывод по графику correlation_heatmap.png: Наблюдается сильная положительная корреляция между текущей ценой и ценой продажи (0.88).

Вывод по графику interactive_scatter.png: Интерактивный анализ подтверждает комплексное влияние факторов: новые дизельные автомобили с высокими текущими ценами образуют кластер самых дорогих предложений. Бензиновые автомобили распределены более равномерно по ценовым сегментам.


Создан признак 'Car_Age'
Создан признак 'Log_Selling_Price'
Создан признак 'Mileage_Category'
Создан признак 'Is_Premium'
Новые признаки созданы успешно!
Общее количество признаков: 13

Очищенный датасет сохранен в '/home/mainuser/iis/data/clean_car_data.pkl'
Финальный размер датасета: 299 записей, 9 признаков
Размер файла: 0.02 МБ
Используемые библиотеки

    pandas - обработка данных

    matplotlib - базовые графики

    seaborn - статистическая визуализация

    numpy - численные операции

    jupyter - интерактивные блокноты

# Проверьте что файл создан правильно
cat requirements.txt



# Должно быть только 6 пакетов
pandas==2.3.3
matplotlib==3.10.7
seaborn==0.13.2
numpy==2.2.6
jupyter==1.1.1
scikit-learn==1.5.2
### 3. **Проверка структуры** перед коммитом:
```bash
# Убедиться что данные не коммитятся
git status

# Добавить только нужные файлы
git add README.md requirements.txt .gitignore eda/eda.ipynb eda/*.png

# Закоммитить
git commit -m "Завершение лабораторной работы №1: EDA и документация"

# Отправить на GitHub
git push origin main

# IIS MLflow Project

Проект по машинному обучению с использованием MLflow для трекинга экспериментов.

## Запуск MLFlow

MLFlow запускается из директории проекта следующей командой:

```bash
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlartifacts \
    --host 0.0.0.0 \
    --port 5000

 Результаты исследования
Лучшая модель: baseline_final

Метрика: 1.18 (чем меньше, тем лучше)

Run ID Production модели: $(python3 -c "from mlflow.tracking import MlflowClient; client = MlflowClient(); prod_versions = client.get_latest_versions('baseline_final', stages=['Production']); print(prod_versions[0].run_id if prod_versions else 'NOT_FOUND')")

Параметры модели:

    Алгоритм: CatBoost

    Модель: CatBoostRegressor/native

Выбранные фичи: Использовался оптимальный набор фичей после feature selection

Статус: Модель переведена в Production в MLflow Model Registry   