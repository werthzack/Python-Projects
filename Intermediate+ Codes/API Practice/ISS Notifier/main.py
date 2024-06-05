import requests
from datetime import datetime
import time

MY_LAT = 6.621639  # Your latitude
MY_LONG = 3.318873  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def within_position():
    min_lat = parameters["lat"] - 5
    max_lat = parameters["lat"] + 5
    min_lng = parameters["lng"] - 5
    max_lng = parameters["lng"] + 5

    with_lat, with_lng = False, False

    if min_lat <= iss_latitude <= max_lat:
        print("It is within Latitude")
        with_lat = True
    if min_lng <= iss_longitude <= max_lng:
        print("It is within Longitude")
        with_lng = True

    if with_lat and with_lng:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = int(str(datetime.now()).split()[1].split(":")[0])


def is_dark():
    rise_dist = abs(sunrise - time_now)
    set_dist = abs(sunset - time_now)

    if rise_dist < set_dist:
        print("It's around sunrise")
        return False
    else:
        print("It's around sunset")
        return True


while True:
    print("Checking...")
    is_dark()
    if within_position() and is_dark():
        print("Look Up")
    try:
        time.sleep(60)
    except KeyboardInterrupt:
        print("Exited Successfully")
        break

# If the ISS is close to your current position,
# and it is currently dark
# Notify to look up.
# run the code every 60 seconds.
