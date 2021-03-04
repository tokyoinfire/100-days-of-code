import requests
from twilio.rest import Client

api_key = ""
OWM_Endpoint = ""
account_sid = ""
auth_token = ""

parameters = {
    "lat": 55.7522,
    "lon": 37.6156,
    "appid": api_key,
}

response = requests.get(url = OWM_Endpoint, params = parameters)

response.raise_for_status()
weather_data = response.json()["hourly"][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+1',
        to='+7'
    )

    print(message.status)

