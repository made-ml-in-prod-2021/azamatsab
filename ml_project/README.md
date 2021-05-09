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

### Testing

```bash
python -m tools.predict --config-name ./configs/config_lr.yml
python -m tools.predict --config-name ./configs/config_rf.yml
```

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
    ├── LICENSE
    │
    ├── README.md                      <- The top-level README for developers using this project.
    │
    ├── requirements.txt               <- The requirements file for reproducing the analysis environment, e.g.
    │                                     generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                       <- Makes project pip installable (pip install -e .) so src can be imported.

------------
