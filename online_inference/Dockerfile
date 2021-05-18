FROM python:3.9-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

WORKDIR /src
RUN export PYTHONPATH="${PYTHONPATH}:/app/src"
COPY ./src \ 
    models \ 
    pipelines \
    /src/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]