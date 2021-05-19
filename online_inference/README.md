# Homework 2


## Installation

#### Build using Dockerfile
    docker build -t kurchum/simple_classifier:tagname .
      
#### Download from dockerhub
    docker pull kurchum/simple_classifier:0.0.1
      
## Run
    docker run -p 5000:5000 kurchum/simple_classifier:0.0.1

#### To make requests
    python3 make_requests.py
      
## Testing
    pip install -q pytest pytest-cov
    python -m pytest . -v --cov

## Optimization
  - Used very small python image - python:3.9-slim-buster (115 Mb)
  - Installed all packages using single RUN command using requiremnts.txt
  - Installed only necessary packages
  - Copied all files using single COPY command (one more command to copy requiremnts.txt)
  - Overall image size is 552 Mb

## Completed Tasks 
* [x] ветку назовите homework2, положите код в папку online_inference
* [x]  Оберните inference вашей модели в rest сервис(вы можете использовать как FastAPI, так и flask, другие желательно не использовать, дабы не плодить излишнего разнообразия для проверяющих), должен быть endpoint /predict (3 балла)
* [x] Напишите тест для /predict  (3 балла) (https://fastapi.tiangolo.com/tutorial/testing/, https://flask.palletsprojects.com/en/1.1.x/testing/)
* [x] Напишите скрипт, который будет делать запросы к вашему сервису -- 2 балла
* [x] Сделайте валидацию входных данных (например, порядок колонок не совпадает с трейном, типы не те и пр, в рамках вашей фантазии)  (вы можете сохранить вместе с моделью доп информацию, о структуре входных данных, если это нужно) -- 3 доп балла
https://fastapi.tiangolo.com/tutorial/handling-errors/ -- возращайте 400, в случае, если валидация не пройдена
* [x] Напишите dockerfile, соберите на его основе образ и запустите локально контейнер(docker build, docker run), внутри контейнера должен запускать сервис, написанный в предущем пункте, закоммитьте его, напишите в readme корректную команду сборки (4 балл)
* [x] Оптимизируйте размер docker image (3 доп балла) (опишите в readme.md что вы предприняли для сокращения размера и каких результатов удалось добиться)  -- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
* [x] опубликуйте образ в https://hub.docker.com/, используя docker push (вам потребуется зарегистрироваться) (2 балла)
* [x] напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель (1 балл)
Убедитесь, что вы можете протыкать его скриптом из пункта 3

Итого 21 балл
