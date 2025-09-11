import requests
import datetime as dt

USERNAME = "suhas991"
TOKEN = "euianfoawnoao21"
pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "NotMinor": "yes",
}


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_configuration = {
    "id": "graph1",
    "name": "Pill",
    "unit": "pill",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

def get_today_date():
    today = dt.datetime.now()
    return today.strftime("%Y%m%d")

def write_to_svg():
    response = requests.get(url=f"{graph_endpoint}/graph1", headers=headers)
    with open("tmp.svg", "w") as file:
        file.write(response.text)
        
current_date = get_today_date()
amount = "1"
update_pixel_data = {
    "date": current_date,
    "quantity": amount,
}

response = requests.post(url=f"{graph_endpoint}/graph1", json=update_pixel_data, headers=headers)
print(response.text)
write_to_svg()



