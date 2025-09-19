import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

get_date = input("Please enter a date in 'YYYY-MM-DD' format: ")

URL = f"https://www.billboard.com/charts/hot-100/{get_date}/"

response = requests.get(URL)

songs = response.text

soup = BeautifulSoup(songs, "html.parser")

song_names = soup.select("ul li ul li h3#title-of-a-story")

client_id = os.environ.get("OATH_CLIENT_ID")
client_key = os.environ.get("OATH_CLIENT_KEY")
redirect_url = os.environ.get("OATH_REDIRECT_URL")
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id, 
    client_secret=client_key, 
    redirect_uri=redirect_url, 
    scope=scope,
    show_dialog=True,
    cache_path="token.txt"
    ))

user_id = sp.current_user()["id"]

playlist_id = sp.user_playlist_create(user=user_id, public=False, collaborative=False, name=f"{get_date} Billboard Top 100")["id"]

song_uris = []

for song in song_names:
    stripped_song = song.getText().replace("\n", "").replace("\t", "")
    result = sp.search(q=f"track:{stripped_song}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"Song: {stripped_song} added")
    except IndexError:
        print(f"{stripped_song} doesn't exist in Spotify. Skipped")

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_uris)
