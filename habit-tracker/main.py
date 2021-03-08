import requests
import datetime

USERNAME = "tokyoinfire"
TOKEN = ""
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Hours Played",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers=headers)
# print(response.text)

pixel_add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()
today = "20210306"

    # today.strftime("%Y%m%d")

pixel_add_config = {
    "date": today,
    "quantity": "5",
}

# response = requests.post(url = pixel_add_endpoint, json = pixel_add_config, headers=headers)
# print(response.text)

pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

pixel_put_config = {
    "quantity": "8"
}

# response = requests.put(url = pixel_put_endpoint, json = pixel_put_config, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"


response = requests.delete(pixel_put_endpoint, headers=headers)
print(response.text)
