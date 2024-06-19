import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

API_KEY = os.getenv('API_KEY') # API key for openweathermap
LAT = 6.634450  # Your latitude
LNG = 3.309960  # Your longitude
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# sid and token for twilio
account_sid = os.getenv('SID')
auth_token = os.getenv('AUTH_TOKEN')

params = {
    "lat": LAT,
    "lon": LNG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params)
response.raise_for_status()

weather_info = response.json()["list"]
weather_codes = [weather["weather"][0]["id"] for weather in weather_info]
will_rain = False

for code in weather_codes:
    if code < 400:
        will_rain = True

if will_rain is True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="You may prolly want to bring an umbrella with you today",
        from_="whatsapp:+14155238886",
        to="whatsapp:+2349124306538"
    )
