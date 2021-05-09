# ML in prod: ДЗ 1

Для управления конфигами использовал hydra, так как hydra дает возможность использовать вложенные конфиги. Так же очень удобно определять модели в конфигах (см. src/conf/model/rf либо logreg).

## Установка

```bash
git clone https://github.com/made-ml-in-prod-2021/azamatsab.git
git checkout homework1
cd ml_project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/requirements.txt
```

## Данные

Загрузите данные с [data](https://www.kaggle.com/ronitf/heart-disease-uci) и разархивируйте в `data`

## EDA

Для генерации отчета EDA запустите: 

```bash
python src/report_generator.py
```

 Отчет будет сохранен в 'data/report' в формате html. Входные данные и выходной путь указывается в src/conf/report_config.yaml

## Запуск тестов

```bash
python -m pytest . -v
```

### Для запуска обучения: 

```bash
python src/train.py model=logreg
python src/train.py model=rf transforms=transforms general=general
```
Можно указать тип модели (logreg или randomForest, трансформеры и общие параметры, такие как размер валидационной выборки, random_state)

Конфиги хранятся в src/conf

### Для запуска инференса:
```bash
python src/predict.py general.model_path=models/LogisticRegression general.input_data_path=data/heart.csv
```

general.model_path - путь к чекпойнту модели

general.input_data_path - путь к данным

## Структура проекта
------------
    ├── data                           <- Данные для обучения
    │     └── report                   <- EDA отчет в html формате
    │
    ├── models                         <- Сериализованные чекпоинты моделей
    │
    ├── notebooks                      <- Jupyter ноутбук для EDA
    │
    ├── preds                          <- Предсказания моделей
    │
    ├── src                            <- Исходный код
    │   ├── __init__.py     
    │   │
    │   ├── conf                       <- Файлы конфигов
    │   │   └── features
    │   │   │       └── simple_featuers <- Конфиги фичей, используемых для обучения
    │   │   │── general                <- Общие конфиги, в папке общие конфиги при обучении и инференсе
    │   │   │
    │   │   │── model
    │   │   │      └── logreg          <- конфиги для логистической регрессии
    │   │   │      └── rf              <- конфиги для модели случайного леса
    │   │   |── transforms             <- конфиги трансформеров
    │   │   |── config.yaml            <- конфиги обучения
    │   │   |── pred_config.yaml       <- конфиги инференса
    │   │   |── report_congig.yaml     <- конфиги для создания EDA отчета
    │   │
    │   ├── entities                   <- Датаклассы для загрузки конфигов
    │   │   ├── config.py    
    │   │
    │   ├── features                   <- Скрипты для препроцессинга данных
    │   │
    │   ├── predict.py
    │   └── train.py
    │   │
    │   │── utils.py
    │   │
    ├── tests                          <- Тесты
    │   ├── data
    │   │   └── test_custom_transformer
    │   │
    │   ├── test_features
    │   │
    │   ├── test_predict
    │   │
    │   ├── test_report_generator
    │   ├
    │   └── test_train_pipeline
    │
    ├── README.md                      <- Описание проекта
    │
    ├── requirements                   <- Требуемые пакеты для запуска проекта 
    │       ├──requirements.txt
    │
    ├── setup.py                       <- Скрипт для установки проекта через pip

------------

## Что сделано

- Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками
Вы так же можете построить в ноутбуке прототип(если это вписывается в ваш стиль работы)
Можете использовать не ноутбук, а скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (за это + 1 балл)

- Проект имеет модульную структуру(не все в одном файле =)

- использованы логгеры

- написаны тесты на отдельные модули и на прогон всего пайплайна

- Для тестов генерируются синтетические данные, приближенные к реальным 
    - можно посмотреть на библиотеки https://faker.readthedocs.io/en/, https://feature-forge.readthedocs.io/en/latest/
    - можно просто руками посоздавать данных, собственноручно написанными функциями
    как альтернатива, можно закоммитить файл с подмножеством трейна(это не оценивается) 

- Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing)

- Используются датаклассы для сущностей из конфига, а не голые dict

- Используйте кастомный трансформер(написанный своими руками) и протестируйте его

- Обучите модель, запишите в readme как это предлагается

- напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку(без меток) и запишет предикт, напишите в readme как это сделать 

- Используется hydra  (https://hydra.cc/docs/intro/)
