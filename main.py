import requests
import os
from datetime import datetime

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = os.environ.get("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"min",
    "type":"float",
    "color":"shibafu"

}

headers = {
    "X-USER-TOKEN":TOKEN

}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

date = today.strftime("%Y%m%d")

pixel_config = {
    "date":date,
    "quantity":input("How many minutes you code today?\t"),
}

response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)


update_pixel_endpoint = f"{pixel_endpoint}/{date}"

update_config = {
    "quantity":"50"
}

# response = requests.put(url=update_pixel_endpoint,json=update_config,headers=headers)
# print(response.text)


delete_endpoint = f"{pixel_endpoint}/{date}"
# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)