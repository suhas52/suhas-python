import requests
import os
import sys

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_city():
    return input("Please enter the name of your city: ").capitalize()

def get_cords(city):
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
            sys.exit()
        return lat, lon
        
def get_weather(lat, lon):
    WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(WEATHER_URL)
    if response.status_code != 200:
        print("Error:", response.status_code)
        sys.exit()
    else:
        data = response.json()
        weather_status = data["weather"][0]["main"]
        return weather_status


city = get_city()
cords = get_cords(city)
lat, lon = cords
weather_status = get_weather(lat, lon)
print(f"{city} is currently {weather_status}")