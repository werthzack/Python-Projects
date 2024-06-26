import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": os.getenv('NUTRITION_ID'),
    "x-app-key": os.getenv('NUTRITION_KEY')
}
body = {
    "query": input("What did you do today?")
}

response = requests.post(url=url, headers=headers, json=body)
data = response.json()['exercises']

sheet_url = "https://api.sheety.co/17b65e5e319b30b16c69c644b430f987/myWorkouts/workouts"
sheet_header = {
    "Authorization": f"Bearer {os.getenv('WORKOUT(SHEETY)_API')}"
}
for i in range(len(data)):
    current_workout = data[i]
    print(current_workout)
    config = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime('%X'),
            "exercise": current_workout['name'].title(),
            "duration": current_workout['duration_min'],
            "calories": current_workout['nf_calories']
        }
    }
    action = requests.post(url=sheet_url, json=config, headers=sheet_header)
