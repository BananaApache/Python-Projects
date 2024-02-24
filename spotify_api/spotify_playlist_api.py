
from lib2to3.pgen2 import token
from colorama import Fore as F
import sys
import os
import requests
import base64
from urllib.parse import urlencode
import json

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
    
    artist_name = input("Type an artist name: ")
    limit_inp =input("List how many albums? ")
    print()

    data = urlencode(
        {"q": f"{artist_name}", "type": "artist,album,playlist,track", "limit": f"{limit_inp}"})

    lookup_url = f"{endpoint}?{data}"
    r = requests.get(lookup_url, headers=headers)

    spotify_json = r.json()

    count = 0

    for item in spotify_json['albums']['items']:
        artist_lst = []
        spotify_json['albums']['items'][count].pop("available_markets")
        spotify_json['albums']['items'][count].pop("images")
        spotify_json['albums']['items'][count].pop("id")
        spotify_json['albums']['items'][count].pop("href")
        spotify_json['albums']['items'][count].pop("external_urls")
        spotify_json['albums']['items'][count].pop("release_date_precision")
        spotify_json['albums']['items'][count].pop("uri")

        # print(json.dumps(item, indent=4))
        # print("\n\n")

        if len(spotify_json['albums']['items'][count]['artists']) != 1:
            for artist in spotify_json['albums']['items'][count]['artists']:
                artist_lst.append(artist['name'])
                artist_lst.append(", and ")
            print(F.RED + ''.join(artist_lst[0: len(artist_lst) - 1]),  F.WHITE + "made the album:",
                  F.CYAN + item['name'], F.WHITE + "on", F.LIGHTGREEN_EX + item['release_date'] + F.RESET)
        else:
            print(F.RED + item['artists'][0]['name'], F.WHITE + "made the album:",
                  F.CYAN + item['name'], F.WHITE + "on", F.LIGHTGREEN_EX + item['release_date'] + F.RESET)

        count += 1

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(F.LIGHTRED_EX, e)
    print(exc_type, fname)
    print('Line:', exc_tb.tb_lineno, F.RESET)

print(F.RESET)
print()
