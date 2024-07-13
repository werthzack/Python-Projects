import os
import base64
import requests
import webbrowser
from datetime import datetime as dt
import json
from dotenv import load_dotenv

load_dotenv()

spotify_url = "https://api.spotify.com/v1"
token_url = "https://accounts.spotify.com/api/token"
auth_url = "https://accounts.spotify.com/authorize?"


class SpotifyManager:
    def __init__(self):
        self_input = input("Do you have your own spotify client key and secret? Y/N")
        if self_input.upper() == "Y":
            self.client = input("Enter your client ID: ")
            self.secret = input("Enter your client secret: ")
        else:
            self.client = os.getenv('SPOTIFY_CLIENT')
            self.secret = os.getenv('SPOTIFY_SECRET')
        self.access_token = ""
        self.refresh_token = ""
        self.cache_manager()

    def cache_manager(self):
        try:
            with open(".cache", "r") as file:
                data = json.load(file)
                if dt.now().timestamp() >= data['expires_in']:
                    token_data = self.token_refresh(data['refresh_token'])
                    json.dump(token_data, file)
                else:
                    self.access_token = data['access_token']
                    self.refresh_token = data['refresh_token']
        except FileNotFoundError:
            token_data = self.authorize()
            print(token_data)
            token_data['expires_in'] += dt.now().timestamp()
            with open(".cache", "w") as file:
                json.dump(token_data, file)

    def authorize(self):
        params = {
            "client_id": self.client,
            "response_type": "code",
            "redirect_uri": "https://example.com",
            "scope": "playlist-modify-private playlist-modify-public"
        }
        url = requests.Request('GET', url=auth_url, params=params).prepare().url
        webbrowser.open(url)
        redirect_url = input("Enter the redirect url given: ")
        code = redirect_url.lstrip(f"{params['redirect_uri']}?code=")
        return self.get_access_token(code)

    def get_access_token(self, code: str):
        credentials = f"{self.client}:{self.secret}"
        encoded_cred = base64.b64encode(credentials.encode()).decode()
        headers = {
            'Authorization': f"Basic {encoded_cred}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {
            'grant_type': "authorization_code",
            'code': code,
            'redirect_uri': 'https://example.com'
        }

        response = requests.post(url=token_url, headers=headers, params=params)
        self.access_token = response.json()['access_token']
        return response.json()

    def token_refresh(self, token: str):
        credentials = f"{self.client}:{self.secret}"
        encoded_cred = base64.b64encode(credentials.encode()).decode()
        headers = {
            'Authorization': f"Basic {encoded_cred}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {
            'grant_type': "refresh_token",
            'refresh_token': token,
            'client_id': self.client
        }

        response = requests.post(url=token_url, headers=headers, data=params)
        print(response.json())
        self.access_token = response.json()['access_token']
        self.refresh_token = response.json()['refresh_token']
        return response.json()

    def get_current_user(self):
        user_url = f"{spotify_url}/me"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(url=user_url, headers=headers)
        print(response.json())
        return response.json()

    def create_playlist(self, name: str, year: str):
        user_id = self.get_current_user()['id']
        playlist_url = f"{spotify_url}/users/{user_id}/playlists"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        params = {
            "name": name,
            "public": False,
            "description": f"Playlist of the top songs during {year}"
        }
        response = requests.post(url=playlist_url, headers=headers, json=params)
        print(response.json())
        return response.json()['id']

    def search_song(self, song: str) -> (dict, None):
        search_url = f"{spotify_url}/search"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            'q': song,
            'type': ['track']
        }
        try:
            response = requests.get(url=search_url, headers=headers, params=params)
            song_id = response.json()['tracks']['items'][0]['uri']
            return song_id
        except requests.ConnectionError:
            print("There was an error with connection for this request")
            return None

    def add_to_playlist(self, playlist_id: str, uris: list[str], position: int):
        playlist_url: str = f"{spotify_url}/playlists/{playlist_id}/tracks"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        params = {
            "uris": uris,
            "position": position - 10,
        }
        response = requests.post(url=playlist_url, headers=headers, params=params)
