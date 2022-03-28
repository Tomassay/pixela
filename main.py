import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "tomassay"
TOKEN = "nxlsewöü312234öüiüsöd"
GRAPH_ID = "graph1"

today = datetime.datetime.now().date()

todayYYYYMMDD = today.strftime("%Y%m%d")

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Gym Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN.encode('utf-8')
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": str(todayYYYYMMDD),
    "quantity": "1",
}

# pixel = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
# print(PIXEL_CREATION_ENDPOINT)
# print(pixel.text)

UPDATE_endpoint = PIXEL_CREATION_ENDPOINT + "/" + todayYYYYMMDD

update_data = {
    "message": "Success",
    "quantity": input("How many hours did you train? "),
}

updated = requests.put(url=UPDATE_endpoint, json=update_data, headers=headers)
# deleted = requests.delete(url=UPDATE_endpoint, json=update_data, headers=headers)

print(updated.text)