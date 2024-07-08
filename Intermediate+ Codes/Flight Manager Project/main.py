import datetime

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

manager = DataManager()
search = FlightSearch()
notifier = NotificationManager()

cities_to_update = manager.get_blank_cities()

if len(cities_to_update) > 0:
    for city in cities_to_update:
        city_name = city[0]
        city_id = city[1]
        city_code = search.get_iata_code(city_name)
        manager.edit_city_code(city_id, city_code)

all_city_information = manager.load_all_city_data()

target_mail = input("What's the target mail?")

for city_information in all_city_information:
    city = city_information['city']
    max_price = city_information['lowestPrice']

    print(f"Analysing flights for {city}")
    possible_flight = search.get_possible_flight_data("LON", city_information["iataCode"], max_price)
    if possible_flight is None or possible_flight == []:
        print(f"There are no current available flights from London to {city} in our database")
        continue
    notifier.send_mail(target_mail, possible_flight, city)
