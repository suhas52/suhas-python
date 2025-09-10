import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise RuntimeError("No API key found. Please set OPENWEATHER_API_KEY.")

def get_city():
    return input("Please enter the name of your city: ").strip().title()

def get_coords(city):
    GEOCODE_URL = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    response = requests.get(GEOCODE_URL)
    if response.status_code != 200:
        raise RuntimeError(f"Error: received status code {response.status_code}")
    else:
        data = response.json()
        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
        else:
            return None
        return lat, lon
        
def get_weather_data(lat, lon):
    WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(WEATHER_URL)
    if response.status_code != 200:
        return None
    else:
        return response.json()


def parse_weather(data):
    return {
        "temperature": data["main"]["temp"] - 273.15,
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"].title(),
        "city": data["name"],
    }

