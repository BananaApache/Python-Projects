
from colorama import Fore as F
import os
from dotenv import load_dotenv
from request_spotify import tracks_spotify as ts
from request_spotify import request_spotify as rs
import base64
import requests

# try:

print(F.WHITE)

load_dotenv()

client_id = os.getenv("spotify_client_id")
client_secret = os.getenv("spotify_client_secret")
user_id = os.getenv("spotify_user_id")
scope = "playlist-modify-public"
redirect_uri = "http://localhost:8080/"
token_url = "https://accounts.spotify.com/api/token"
client_creds = f"{client_id}:{client_secret}"
b64_client_creds = base64.b64encode(client_creds.encode())
token_data = {
    "grant_type": "client_credentials"
}
token_headers = {
    "Authorization": f"Basic {b64_client_creds.decode()}"
}
r_foraccess = requests.post(
    token_url, data=token_data, headers=token_headers)

access_token = r_foraccess.json()['access_token']

oauth_token = os.getenv("spotify_oauth_token")

headers = {
    'Accept': 'application/json',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Authorization': f'Bearer {oauth_token}',
}

rapper = input("Enter rapper name: ")

json_data = {
    'name': f'Every {rapper} song ever',
    'description': 'New playlist description',
    'public': True,
}

response = requests.post(
    f'https://api.spotify.com/v1/users/{user_id}/playlists', headers=headers, json=json_data)

print("Made playlist called:", F.CYAN + f"Every {rapper} song ever" + F.RESET)

track_lst = ts.all_track_dict(rapper_name=rapper)

print(f"Got all songs from", F.LIGHTYELLOW_EX + rapper + F.RESET)

user_playlists = rs.get_user_playlist()

for playlist in user_playlists:
    if playlist['name'] == f"Every {rapper} song ever":
        playlist_id = playlist['id']

spotify_json = rs.get_raw_albums(artist_name=rapper)
total_albums = spotify_json['total']

time_complete = (int(total_albums) * 9) / 2

print(f"{rapper} has", F.GREEN + str(total_albums), "albums" + F.RESET)
print(f"Estimated time of completion:", F.GREEN +
      str(time_complete),  "seconds \n" + F.RESET)

for song_name, uri in track_lst.items():
    print(F.WHITE + f"Adding song", F.RED + song_name, end="\r")
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {oauth_token}',
    }

    params = {
        'position': '0',
        'uris': uri,
    }

    response = requests.post(
        f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', params=params, headers=headers)


print("\n" + F.RESET)
