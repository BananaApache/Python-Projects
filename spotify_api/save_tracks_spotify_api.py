
from colorama import Fore as F
import sys
import os
from request_spotify import tracks_spotify as ts
from request_spotify import request_spotify as rs
import base64
import requests

try:
    print()
    print(F.WHITE)

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
        'Accept': 'application/json',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Authorization': 'Bearer BQB89D3HoGPq9bSNMdY-QowMac36xWarSByNxCsdXu3Ti6ImgJ7Yv2MUiFZ4NhzGUhSigmwLD3_WyHjysMY_PW9kmZVm3QnfmzE80q4MYHoefY6ZPHLSbPTuJxqaSnTvt9bC2lISJY4hNWzSTxeJlj4NIXDJmGmTyni_O1ZICaab3epLQTmo-9YjMfDrt5Ea8hSO3dWn30qVwfY1X-hCSax4-i1XvTQ',
    }

    json_data = {
        'name': 'Every Kendrick Lamar song ever',
        'description': 'New playlist description',
        'public': True,
    }

    response = requests.post(
        'https://api.spotify.com/v1/users/pmmvtbs15n5tb9t0trofa07ld/playlists', headers=headers, json=json_data)

    track_lst = ts.all_track_lst()

    playlist_id = input("Get playlist ID: ")

    for uri in track_lst:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer BQCfThSGL497kFnY9w7O6r-EMCDtL5r9lfqv9F78PTXHhlcV-W8PKn5GVWEfu7dy3X3tZaAzIIhhbM5RrAuhyX_6vcc0QBwDMJ03eF6hdXO0DRB-uxArOje_54pJaWZT_Ax_W7GEneniIEiDUnZF3BY8gor3mogwGdUna8hyXJf6dhNFEBHIMK7OMXzME8LdeZi3vo2lO9ghHW2xJJrrbHK8vymWXps',
        }

        params = {
            'position': '0',
            'uris': uri,
        }

        response = requests.post(
            f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', params=params, headers=headers)
        
    # uris = ','.join(track_lst[0:11])
    # print(uris)

    # rs.save_track(uris)

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(F.LIGHTRED_EX, e)
    print(exc_type, fname)
    print('Line:', exc_tb.tb_lineno, F.RESET)

print(F.RESET)
print()

# import requests
# from request_spotify import tracks_spotify as ts
# import json

# tracks = ts.all_track_lst()

# for uri in tracks:

#     headers = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer BQA6Seni3ww3OvgI_e3gMXfYJQsLKObx1F0kri0vX3LsRGQaG7fC6Aqfc89X6YuZ1bHydxLxiobfrg15-G_7Z49HgZLboEDLghhwaj18cuRXEdv8X6kkZl4D8dj3JBzc1D1FPyWFu3qEb67aolp_W8nIW8SwWg4TTotVhlpDTXdQgT0Qo79x5T8pOx-Uu9c',
#     }

#     params = {
#         'position': '0',
#         'uris': uri
#     }

#     response = requests.post(
#         f'https://api.spotify.com/v1/playlists/0lpC1s4xAMjzBirmHsHgFS/tracks', params=params, headers=headers)
