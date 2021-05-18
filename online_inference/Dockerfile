FROM python:3.9-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

WORKDIR /src
COPY ./src \ 
    models \ 
    pipelines \
    /src/
ENV PATH_TO_CONFIG=/src/conf/docker_config.yaml
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]