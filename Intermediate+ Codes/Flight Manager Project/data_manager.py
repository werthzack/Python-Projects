import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    price_url = f"https://api.sheety.co/{os.getenv('SHEETY_API')}/flightDeals/prices"
    user_url = f"https://api.sheety.co/{os.getenv('SHEETY_API')}/flightDeals/users"

    def get_blank_cities(self) -> list:
        city_data = self.load_all_city_data()
        cities_to_update = [(city['city'], city['id']) for city in city_data if city['iataCode'] == '']
        return cities_to_update

    def load_all_city_data(self) -> dict:
        response = requests.get(url=self.price_url)
        city_data = response.json()['prices']
        return city_data

    def edit_city_code(self, city_id: int, code: str) -> None:
        details = {
            "price": {
                'iataCode': code
            }
        }
        requests.put(url=f"{self.price_url}/{city_id}", json=details)

    def get_customer_emails(self):
        response = requests.get(url=self.user_url)
        user_data = response.json()['users']
        return user_data

