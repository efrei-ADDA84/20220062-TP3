from fastapi import FastAPI

import os
import requests

app = FastAPI()
API_KEY = os.environ.get('API_KEY')
@app.get("/")
async def root(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()

    return data
