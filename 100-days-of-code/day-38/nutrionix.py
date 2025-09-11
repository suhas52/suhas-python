import requests
import os

NUT_ID = os.environ.get('nut_id')
NUT_KEY = os.environ.get('nut_key')
nut_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": NUT_ID,
    "x-app-key": NUT_KEY,
}


def get_user_exercise():
    return input("Input today's exercise in natural language: ")

def get_user_parameters(exercise):
    return {
    "query": exercise,
    "weight_kg": "51",
    "height_cm": "165.50",
    "age": "23",
}    

def get_exercise_stats(user_parameters):
    response = requests.post(url=nut_endpoint, json=user_parameters, headers=headers)
    return response.json()
