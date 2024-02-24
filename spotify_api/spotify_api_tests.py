
from colorama import Fore as F
import sys
import os
import requests
import base64
from urllib.parse import urlencode
import json
import urllib.request

try:
    print()
    print(F.WHITE)

    client_id = "8365e8a828f440c992c995ac1977f442"
    client_secret = "1dbb90d2984242d9924e63cb0c8e1aeb"

    class SpotifyAPI(object):
        access_token = None
        client_id = None
        client_secret = None
        token_url = "https://accounts.spotify.com/api/token"
        method = "POST"

        def __init__(self, client_id, client_secret, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.client_id = client_id
            self.client_secret = client_secret

        def get_client_credentials(self):
            # RETURNS BASE64 ENCODED STRING
            client_id = self.client_id
            client_secret = self.client_secret
            if client_secret == None or client_id == None:
                raise Exception("SET CLIENT ID AND CLIENT SECRET")
            client_creds = f"{client_id}:{client_secret}"
            client_creds_b64 = base64.b64encode(client_creds.encode())
            return client_creds_b64.decode()

        def get_token_headers(self):
            client_creds_b64 = self.get_client_credentials()
            return {
                "Authorization": f"Basic {client_creds_b64}"
            }

        def get_token_data(self):
            return {
                "grant_type": "client_credentials"
            }

        def perform_auth(self):
            token_url = self.token_url
            token_data = self.get_token_data()
            token_headers = self.get_token_headers()
            r = requests.post(token_url, data=token_data,
                              headers=token_headers)

            if r.status_code not in range(200, 299):
                return False
            # valid_request = r.status_code in range(200, 299)
            # if valid_request:

            token_response_data = r.json()
            access_token = token_response_data['access_token']
            expires = token_response_data['expires_in']
            self.access_token = access_token
            self.expires = expires
            return True

    spotify = SpotifyAPI(client_id, client_secret)
    spotify.perform_auth()
    access_token = spotify.access_token

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    endpoint = "https://api.spotify.com/v1/search"

    # data = "2hlmm7s2ICUX0LVIhVFlZQ"

    artist_name_inp = str(input("Enter artist name: "))

    artist_data = urlencode(
        {"q": f"{artist_name_inp}", "type": "artist", "limit": "1"})

    lookup_url = f"{endpoint}?{artist_data}"
    r = requests.get(lookup_url, headers=headers)

    spotify_json = r.json()

    data = str(spotify_json['artists']['items'][0]['id'])

    print()

    # data = urlencode(
    #     {f"{id}"})

    endpoint = "https://api.spotify.com/v1/artists"
    queries = urlencode(
        {"limit": "1", "offset": "0", "include_groups": "album,single"}
    )

    lookup_url = f"{endpoint}/{data}/albums?{queries}"
    r = requests.get(lookup_url, headers=headers)

    spotify_json = r.json()

    count = 0
    album_lst = []

    spotify_json['items'][0].pop('available_markets')
    print(json.dumps(spotify_json['items'], indent=4))

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(F.LIGHTRED_EX, e)
    print(exc_type, fname)
    print('Line:', exc_tb.tb_lineno, F.RESET)

print(F.RESET)
print()
