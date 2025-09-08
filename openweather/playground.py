import requests
import sys
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

city = "bangalore"
GEOCODE_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
response = requests.get(GEOCODE_URL)
if response.status_code != 200:
    print("Error: ", response.status_code)
    sys.exit()
else:
    data = response.json()
    if data:
        lat = data[0]["lat"]
        lon = data[0]["lon"]
    else:
        print("Please enter valid city!")
