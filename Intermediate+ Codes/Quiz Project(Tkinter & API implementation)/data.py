import requests

parameters = {
    "amount": 3,
    "difficulty": "",
    "category": "",
    "type": "boolean"
}

question_data = []


def get_categories():
    response = requests.get("https://opentdb.com/api_category.php")
    categories = response.json()["trivia_categories"]
    return categories


def load_data(amount: int = None, difficulty: str = None, q_type: str = None, cat_id=None):
    global question_data
    parameters["amount"] = amount if amount is not None else parameters["amount"]
    parameters["difficulty"] = difficulty if difficulty is not None else parameters["difficulty"]
    parameters["type"] = q_type if q_type is not None else parameters["type"]
    parameters["category"] = cat_id if cat_id is not None else parameters["type"]

    print(parameters)
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    question_data = response.json()["results"]