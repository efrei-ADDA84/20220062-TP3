FROM python:3.9.12

WORKDIR /weather-app

COPY tp2.py .
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "tp2:app", "--host", "0.0.0.0", "--port", "8081", "--reload" ]
