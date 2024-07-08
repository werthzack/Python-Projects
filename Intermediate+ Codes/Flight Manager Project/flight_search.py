import datetime

import requests
import os
from dotenv import load_dotenv
from datetime import datetime as dt
from datetime import timedelta

load_dotenv()


class FlightSearch:
    request_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
    token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    flight_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    def __init__(self):
        self.access_token = ""
        self.expire_time = 0

    timedelta(days=180)

    def access_token_update(self):
        current_ts = dt.now().timestamp()
        if current_ts >= self.expire_time:
            self.generate_access_token()

    def generate_access_token(self):
        access_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        access_body = {
            "grant_type": "client_credentials",
            "client_id": os.getenv('AMADEUS_ID'),
            "client_secret": os.getenv('AMADEUS_TOKEN')
        }

        access = requests.post(url=self.token_url, headers=access_header, data=access_body, verify=False)
        self.access_token = access.json()['access_token']
        self.expire_time = dt.now().timestamp() + access.json()['expires_in']

    def get_iata_code(self, city_name: str):
        self.access_token_update()
        headers = {
            "accept": "application/vnd.amadeus+json",
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            "keyword": city_name,
            "include": ['AIRPORTS'],
            "max": 10
        }

        response = requests.get(url=self.request_url, headers=headers, params=params).json()
        response_data = response.get('data')
        if response_data is None:
            return
        for data in response_data:
            if data['name'] == city_name:
                return data['iataCode']

        for data in response_data:
            if city_name in data['name'] and data.get('iataCode') is not None:
                return data['iataCode']

    def get_possible_flight_data(self, origin_city_code: str, destination_city_code: str, maximum_ticket_price: int):
        self.access_token_update()
        auth_headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
            "adults": 1,
            "maxPrice": maximum_ticket_price,
            "max": 10
        }

        response = requests.get(url=self.flight_url, headers=auth_headers, params=params, verify=False)
        response_data = response.json().get('data')
        if response_data is None or len(response_data) < 1:
            return None
        flight_data = {
            "total_price": response_data[0]['price']['grandTotal'],
            "flight_date": response_data[0]['lastTicketingDate']
        }
        return flight_data
