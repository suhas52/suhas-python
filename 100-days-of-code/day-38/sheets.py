import requests
import os
import datetime as dt


sheets_endpoint = "https://api.sheety.co/aabbbd554dd6ab75e625ae63538839fd/"
spreedsheet_id = "myWorkouts/workouts"

def get_columns_length():
    response = requests.get(f"{sheets_endpoint}/{spreedsheet_id}")
    data = response.json()
    return len(data["workouts"])

def get_current_date():
    today = dt.datetime.now()
    return {
        "date": today.strftime("%d/%m/%y"),
        "time": today.strftime("%H:%M:%S"),
    }
    

def create_body(exercise_stats):
    date = get_current_date()
    return {
        "workout" : {
            "date": date["date"],
            "time": date["time"],
            "exercise":exercise_stats["exercises"][0]["user_input"],
            "duration":str(exercise_stats["exercises"][0]["duration_min"]),
        "calories":exercise_stats["exercises"][0]["nf_calories"],
        },
    }
    
def send_to_sheets(to_sheets = 0):
    length = get_columns_length()
    requests.put(f"{sheets_endpoint}/{spreedsheet_id}/{length + 2}", json=to_sheets)