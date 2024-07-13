import requests
from datetime import datetime as dt
from bs4 import BeautifulSoup
from spotify_manager import SpotifyManager


def is_valid_date(given_date: str):
    try:
        dt.strptime(given_date, '%Y-%m-%d')
        return True
    except ValueError:
        print("The date give is not in the correct format")
        return False


manager = SpotifyManager()

date = ""
date_given = False
while not date_given:
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")
    date_given = is_valid_date(date)

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.encoding = 'utf-8'
website = BeautifulSoup(response.text, "html.parser")
all_songs = website.find_all(class_="o-chart-results-list-row-container")

playlist = manager.create_playlist(
    f"Top 100 Songs for {dt.strptime(date, '%Y-%m-%d').strftime('%B,%Y')}", date)

song_uris: list = []
for i, song in enumerate(all_songs, start=1):
    song_title = song.select_one("h3").string.strip()
    song_artist = song.select_one("ul li ul li span").string.strip()
    print(f"Getting details for song {i}: {song_title} by {song_artist}")
    song_uri = manager.search_song(f"{song_title} {song_artist}")
    if song_uri is not None:
        song_uris.append(song_uri)
    if i % 10 == 0:
        manager.add_to_playlist(playlist, song_uris, i)
        print("Updating Playlist info")
        song_uris = []
