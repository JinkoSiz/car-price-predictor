import joblib
import pandas as pd
from django.shortcuts import render
from .forms import CarForm
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Загрузка данных из CSV файла
df = pd.read_excel('./static/dataset/car_dataset.xlsx')

# Предварительная обработка данных
le = LabelEncoder()
for col in ['Модель', 'Марка', 'Коробка']:
    df[col] = le.fit_transform(df[col])

scaler = StandardScaler()
df[['Пробег', 'Объем']] = scaler.fit_transform(df[['Пробег', 'Объем']])

# Подготовка данных для модели
X = df[['год_выпуска', 'Пробег', 'Объем', 'Коробка']]
y = df['Цена']

# Обучение модели XGBoost
model = XGBRegressor(random_state=42)
model.fit(X, y)

# Сохранение модели
joblib.dump(model, 'xgboost_model.pkl')

# Загрузка модели
model = joblib.load('xgboost_model.pkl')


def predict_price(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            model_name = form.cleaned_data['model']
            year = form.cleaned_data['year']
            mileage = form.cleaned_data['mileage']
            engine = form.cleaned_data['engine']
            gearbox = form.cleaned_data['gearbox']

            # Подготовка данных для модели
            data = pd.DataFrame([[year, mileage, engine, gearbox]],
                                columns=['год_выпуска', 'Пробег', 'Объем', 'Коробка'])
            data['Коробка'] = le.transform(data['Коробка'])
            data[['Пробег', 'Объем']] = scaler.transform(data[['Пробег', 'Объем']])
            predicted_price = model.predict(data)[0]

            context = {
                'form': form,
                'predicted_price': predicted_price,
                'car_info': {
                    'brand': brand,
                    'model': model_name,
                    'year': year,
                    'mileage': mileage,
                    'engine': engine,
                    'gearbox': gearbox
                }
            }
            return render(request, 'prediction/result.html', context)
    else:
        form = CarForm()

    return render(request, 'prediction/index.html', {'form': form})
