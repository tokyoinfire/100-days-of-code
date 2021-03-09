import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
exercise_endpoint = os.environ["exercise_endpoint"]
login = os.environ["login"]
password = os.environ["password"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 191,
    "age": 20,
}

response = requests.post(url = exercise_endpoint,
                         json = params,
                         headers=headers
)

result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, auth=(login, password))

    print(sheet_response.text)
