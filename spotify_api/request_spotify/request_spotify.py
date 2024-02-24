
import requests
import base64
from urllib.parse import urlencode
import json
from colorama import Fore as F


def get_raw_albums(artist_name, limit=50, offset=0):
    client_id = "8365e8a828f440c992c995ac1977f442"
    client_secret = "1dbb90d2984242d9924e63cb0c8e1aeb"
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
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    endpoint = "https://api.spotify.com/v1/search"
    artist_data = urlencode(
        {"q": f"{artist_name}", "type": "artist", "limit": "1"})
    lookup_url = f"{endpoint}?{artist_data}"

    r = requests.get(lookup_url, headers=headers)

    try:
        data = str(r.json()['artists']['items'][0]['id'])
    except:
        print(F.RED + "Artist does not exist." + F.RESET, "\n")
        exit()

    endpoint = "https://api.spotify.com/v1/artists"
    queries = urlencode(
        {"limit": f"{limit}", "offset": f"{offset}",
            "include_groups": "album,single"}
    )

    lookup_url = f"{endpoint}/{data}/albums?{queries}"
    r = requests.get(lookup_url, headers=headers)

    return r.json()


def get_raw_tracks(id, limit=50, offset=0):
    client_id = "8365e8a828f440c992c995ac1977f442"
    client_secret = "1dbb90d2984242d9924e63cb0c8e1aeb"
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
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    endpoint = "https://api.spotify.com/v1/albums"
    queries = urlencode(
        {"limit": f"{limit}", "offset": f"{offset}"}
    )

    lookup_url = f"{endpoint}/{id}/tracks?{queries}"
    r = requests.get(lookup_url, headers=headers)

    return r.json()


def save_track(id):
    client_id = "8365e8a828f440c992c995ac1977f442"
    client_secret = "1dbb90d2984242d9924e63cb0c8e1aeb"
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
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    endpoint = "https://api.spotify.com/v1/playlists/1Ts1gpKDsvytqrvpWedqBP/tracks"

    lookup_url = f"{endpoint}?{id}"
    r = requests.get(lookup_url, headers=headers)

    return r.json()


def get_user_playlist():
    client_id = "8365e8a828f440c992c995ac1977f442"
    client_secret = "1dbb90d2984242d9924e63cb0c8e1aeb"
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
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    endpoint = "https://api.spotify.com/v1/users/pmmvtbs15n5tb9t0trofa07ld/playlists"
    queries = urlencode(
        {}
    )

    lookup_url = f"{endpoint}"
    r = requests.get(lookup_url, headers=headers)

    return r.json()['items']

