import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = ""

year = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
songs_html = response.text

soup = BeautifulSoup(songs_html, "html.parser")

all_songs = soup.find_all(name = "span", class_="chart-element__information__song text--truncate color--primary")

song_list = [song.getText() for song in all_songs]


#print(song_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri= REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = year.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(
    user = user_id,
    name = f"{year}-top-100-songs",
    public=False,
    collaborative=False,
    description=f'Billboard Top 100 Songs from {year}'
)
print(playlist["external_urls"]["spotify"])

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris, position=None)
