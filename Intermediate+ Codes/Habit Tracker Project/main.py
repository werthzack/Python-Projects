import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USERNAME = "machine11"
TOKEN = os.getenv('PIXELA_TOKEN')
GRAPH_ID = "test1"

# pixela_endpoint = "https://pixe.la/v1/users"
# params = {
#     "token": "#################",
#     "username": "machine11",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
config = {
    "id": "test1",
    "name": "Minutes Graph",
    "unit": "min",
    "type": "float",
    "color": "sora"
}

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime(year=2024, month=6, day=23)

pixel_update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"
pixel_data = {
    "quantity": "8.5"
}

response = requests.delete(headers=headers, url=pixel_update_endpoint)
print(response.text)
