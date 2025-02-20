from fastapi import FastAPI
import requests

app = FastAPI()

API_URL = "https://restcountries.com/v3.1/independent?status=true"

@app.get("/extract")
def extract_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return {"message": "Data extracted successfully", "data": data[:5]}  # Showing first 5 countries
    return {"message": "Failed to extract data", "status_code": response}