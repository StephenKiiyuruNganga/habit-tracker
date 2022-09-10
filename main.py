from datetime import datetime
import requests

USERNAME = "XXXXXXX"
TOKEN = "XXXXXXX"
GRAPH_ID = "graph1"

pixela_api = "https://pixe.la/v1/users"

user_data = {
    "token": "snash111007",
    "username": "snash007",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_api, json=user_data)
# print(response.status_code, response.text)

pixela_create_graph_api = f"{pixela_api}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Masterclass",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_create_graph_api,
#                          json=graph_config,
#                          headers=headers)

# print(response.status_code, response.text)

pixela_add_pixel_api = f"{pixela_create_graph_api}/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")
another_day = datetime(year=2022, month=5, day=13).strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "1.5",
}

# response = requests.post(url=pixela_add_pixel_api,
#                          json=pixel_data,
#                          headers=headers)
# print(response.status_code, response.text)

pixela_update_pixel_api = f"{pixela_add_pixel_api}/{today}"

new_pixel_data = {
    "quantity": "1.7",
}

# response = requests.put(url=pixela_update_pixel_api,
#                         json=new_pixel_data,
#                         headers=headers)
# print(response.status_code, response.text)

response = requests.delete(url=pixela_update_pixel_api, headers=headers)
print(response.status_code, response.text)
