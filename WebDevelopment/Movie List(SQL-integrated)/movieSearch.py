import requests
import os
from dotenv import load_dotenv

load_dotenv()


class MovieSearch:
    url = "https://api.themoviedb.org/3/search"
    def __init__(self, token=None):
        if token is None:
            token = os.environ.get("TMDB_TOKEN")
        self.key = token
        self.headers = {
            "Authorization": f"Bearer {self.key}",
            "accept": "application/json"
        }

    def search_movie(self, query: str, adult=False):
        search_url = f"{self.url}/movie"
        params = {
            "query": query,
            "include_adult": adult,
        }

        request = requests.get(url=search_url, headers=self.headers, params=params)
        request.raise_for_status()
        response = request.json()
        return response["results"]

    def get_movie(self, movie_id):
        movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        request = requests.get(url=movie_url, headers=self.headers)
        request.raise_for_status()
        response = request.json()
        return response

