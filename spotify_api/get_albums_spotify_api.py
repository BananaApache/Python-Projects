
from lib2to3.pgen2 import token
from colorama import Fore as F
import sys
import os
import requests
import base64
from urllib.parse import urlencode
import json
import urllib.request
from datetime import datetime, date


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

    artist_name_inp = str(input("Enter artist name: "))

    artist_data = urlencode(
        {"q": f"{artist_name_inp}", "type": "artist", "limit": "1"})

    lookup_url = f"{endpoint}?{artist_data}"
    r = requests.get(lookup_url, headers=headers)

    spotify_json = r.json()

    try:
        data = str(spotify_json['artists']['items'][0]['id'])
    except:
        print(F.RED + "Artist does not exist." + F.RESET, "\n")
        exit()

    # data = "2hlmm7s2ICUX0LVIhVFlZQ"
    endpoint = "https://api.spotify.com/v1/artists"
    queries = urlencode(
        {"limit": "50", "offset": "50", "include_groups": "album,single"}
    )

    lookup_url = f"{endpoint}/{data}/albums?{queries}"
    r = requests.get(lookup_url, headers=headers)

    spotify_json = r.json()

    total_albums = spotify_json['total']

    div = total_albums / 50

    if type(div) == float:
        loop_time = int(div) + 1
    else:
        loop_time = int(div)

    offset_count = 0
    num = 1
    count = 0

    print()

    for i in range(loop_time):
        queries = urlencode({"limit": "50", "offset": f"{offset_count * 50}",
                            "include_groups": "album,single"})
        lookup_url = f"{endpoint}/{data}/albums?{queries}"
        r = requests.get(lookup_url, headers=headers)

        spotify_json = r.json()

        for remove in spotify_json:
            # spotify_json['items'][count].pop("available_markets")
            # spotify_json['items'][count].pop("id")
            # spotify_json['items'][count].pop("href")
            # spotify_json['items'][count].pop("external_urls")
            # spotify_json['items'][count].pop("release_date_precision")
            # spotify_json['items'][count].pop("uri")

            # print(json.dumps(spotify_json['items'][count], indent=4))
            album_dict = {}

            for name in spotify_json['items']:
                album_name = name['name']
                album_pic = name['images'][0]['url']
                album_release = name['release_date']
                album_id = name['id']
                try:
                    dt_release = date.fromisoformat(str(album_release))
                    dt_release = dt_release.strftime('%B %d, %Y')
                except:
                    dt_release = album_release
                album_dict.update({
                    f"{album_name} " + F.GREEN + f"{dt_release}": album_pic + " " + album_id
                })

            count += 1

        key_lst = []
        no_dupe_album_dict = {}

        for k, v in album_dict.items():
            if k not in key_lst:
                key_lst.append(k)

        for pic in key_lst:
            no_dupe_album_dict.update({pic: album_dict.get(pic)})

        for song, pic in no_dupe_album_dict.items():
            print(F.RED + str(num) + ".", F.CYAN + song + F.WHITE + ":", pic + F.RESET)
            # print(song, "is being saved..")
            # urllib.request.urlretrieve(pic, f"./apis_python/spotify_api/gunna_albums/{song}.jpg")
            print()
            num += 1

        offset_count += 1

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(F.LIGHTRED_EX, e)
    print(exc_type, fname)
    print('Line:', exc_tb.tb_lineno, F.RESET)

print(F.RESET)
print()
