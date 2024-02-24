
import requests
import base64
import json
import urllib.parse
import collections
import math 
from colorama import Fore as F

user_id = "pmmvtbs15n5tb9t0trofa07ld"

# Sends POST request to spotify server asking for a token
def get_access_token():
    client_id = '8365e8a828f440c992c995ac1977f442'
    client_secret = '1dbb90d2984242d9924e63cb0c8e1aeb'

    headers = {
        "Authorization" : f"Basic {base64.b64encode(str(client_id + ':' + client_secret).encode('ascii')).decode()}",
        "Content-type": "application/x-www-form-urlencoded",
        "json": "true"
    }
    data = {
        "grant_type": "client_credentials"
    }
        
    f = open('advanced/access_token.txt', 'w')
    f.write(json.loads(str(requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data).text))['access_token'])
    f.close()


def renew_access_token():
    # print(f"\nAccess Token expired. Go to this url: https://accounts.spotify.com/authorize?response_type=token&client_id=8365e8a828f440c992c995ac1977f442&redirect_uri=http://localhost:8080/&scope={urllib.parse.quote('playlist-modify-private playlist-modify-public playlist-read-private playlist-read-collaborative')}")
    # url = input("Then copy the url and paste it here: ")
    # access_token = url.split("&")[0].split("=")[1]
    
    # f = open("advanced/access_token.txt", 'w')
    # f.write(access_token)
    # f.close()

    cookies = {
        'sp_m': 'us',
        'sp_t': 'ce237c81-5f19-4623-9e18-24f1ad70c94e',
        'sp_adid': '921ebf13-89e5-44aa-a6e6-286825b837a0',
        '_scid': '493ada10-5498-49c9-9548-4e7b1fd1a83a',
        '_cs_c': '0',
        '__Host-device_id': 'AQDZJ9LdSlEutN884k7XmWheIfBkOplZGn1XHodbt9gALrIiaBz86Wqa04AX_-3y6rfUaRrs94b-aLa03zBx2ZEDtcwjpbbWmuI',
        '_gcl_au': '1.1.2002873754.1692920146',
        '__Secure-TPASESSION': 'AQCmm9gS1r0ScAjxBctX8Ly6Ehkp9z6Cr1LQgF7EN4aHH0R1HGTs0wbB8hfOrQ333zMGfCdL4y+umJ42jeyxsN7MoXn3EiAJTto=',
        'sp_tr': 'true',
        '_ga_ZWG1NSHWD8': 'GS1.1.1692920146.2.0.1692920148.0.0.0',
        'remember': 'dabbingshrekbru%40gmail.com',
        'sp_dc': 'AQCYIB9unU9msMyX9g182zu6l-yao7CUskM4DEQ6xw7R4sMG2Rf_spduPPvF2bh_QIVN3UwKmKnpA4H62vdDwFhzQjyGY_6j-V-Ou4wtDY3o5UOwOcVu1VbB64yP-E7Gqz9ZXptF6w8dy-8WwSFELmKMO1ZbGEY',
        'sp_key': 'a04048d0-2e7c-4e20-adc1-3de1317b22c5',
        'sp_gaid': '0088fc6f57d1243d9a0e0ca8f277a9641b24f8fc408ee2b62cc9c4',
        '_tt_enable_cookie': '1',
        '_ttp': 'DT1N-dvOqNGUe4kRMjQsAzIBMk-',
        '_sctr': '1%7C1692849600000',
        '_scid_r': '493ada10-5498-49c9-9548-4e7b1fd1a83a',
        '_cs_id': 'cf311f1a-27bc-ae82-c5b3-70590722f608.1676165497.2.1692922394.1692922369.1.1710329497160',
        '_ga_S35RN5WNT2': 'GS1.1.1692922369.2.1.1692922397.0.0.0',
        'sp_sso_csrf_token': '013acda719ccaa86ca613d8cdddd82da32375a294e31363932393234323637393434',
        '_ga': 'GA1.1.1351867012.1676165494',
        'sp_landing': 'https%3A%2F%2Fwww.spotify.com%2Fus%2F',
        'csrf_token': 'AQCGWk3RFzxr_1QTSxx2jkb3z79UKEzQ79QX09ePsgHM6o4ckCR-n6zD3qHs2Hq9EfP9xElOypE2OT43n8zD48mxuDp_VN1JtUyjTmBuSEeQfzrDF84',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Aug+26+2023+10%3A15%3A23+GMT-0400+(Eastern+Daylight+Time)&version=6.26.0&isIABGlobal=false&hosts=&consentId=ed678990-f97a-4d6a-9337-6fbb4bbe850f&interactionCount=1&landingPath=NotLandingPage&groups=BG154%3A1%2Ct00%3A1%2CBG155%3A1%2Cs00%3A1%2Cf00%3A1%2Cm00%3A1%2Ci00%3A1%2Cf11%3A1&AwaitingReconsent=false',
        '_ga_ZWRF3NLZJZ': 'GS1.1.1693059322.5.1.1693059339.0.0.0',
        'inapptestgroup': '',
    }
    headers = {
        'authority': 'accounts.spotify.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'sp_m=us; sp_t=ce237c81-5f19-4623-9e18-24f1ad70c94e; sp_adid=921ebf13-89e5-44aa-a6e6-286825b837a0; _scid=493ada10-5498-49c9-9548-4e7b1fd1a83a; _cs_c=0; __Host-device_id=AQDZJ9LdSlEutN884k7XmWheIfBkOplZGn1XHodbt9gALrIiaBz86Wqa04AX_-3y6rfUaRrs94b-aLa03zBx2ZEDtcwjpbbWmuI; _gcl_au=1.1.2002873754.1692920146; __Secure-TPASESSION=AQCmm9gS1r0ScAjxBctX8Ly6Ehkp9z6Cr1LQgF7EN4aHH0R1HGTs0wbB8hfOrQ333zMGfCdL4y+umJ42jeyxsN7MoXn3EiAJTto=; sp_tr=true; _ga_ZWG1NSHWD8=GS1.1.1692920146.2.0.1692920148.0.0.0; remember=dabbingshrekbru%40gmail.com; sp_dc=AQCYIB9unU9msMyX9g182zu6l-yao7CUskM4DEQ6xw7R4sMG2Rf_spduPPvF2bh_QIVN3UwKmKnpA4H62vdDwFhzQjyGY_6j-V-Ou4wtDY3o5UOwOcVu1VbB64yP-E7Gqz9ZXptF6w8dy-8WwSFELmKMO1ZbGEY; sp_key=a04048d0-2e7c-4e20-adc1-3de1317b22c5; sp_gaid=0088fc6f57d1243d9a0e0ca8f277a9641b24f8fc408ee2b62cc9c4; _tt_enable_cookie=1; _ttp=DT1N-dvOqNGUe4kRMjQsAzIBMk-; _sctr=1%7C1692849600000; _scid_r=493ada10-5498-49c9-9548-4e7b1fd1a83a; _cs_id=cf311f1a-27bc-ae82-c5b3-70590722f608.1676165497.2.1692922394.1692922369.1.1710329497160; _ga_S35RN5WNT2=GS1.1.1692922369.2.1.1692922397.0.0.0; sp_sso_csrf_token=013acda719ccaa86ca613d8cdddd82da32375a294e31363932393234323637393434; _ga=GA1.1.1351867012.1676165494; sp_landing=https%3A%2F%2Fwww.spotify.com%2Fus%2F; csrf_token=AQCGWk3RFzxr_1QTSxx2jkb3z79UKEzQ79QX09ePsgHM6o4ckCR-n6zD3qHs2Hq9EfP9xElOypE2OT43n8zD48mxuDp_VN1JtUyjTmBuSEeQfzrDF84; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Aug+26+2023+10%3A15%3A23+GMT-0400+(Eastern+Daylight+Time)&version=6.26.0&isIABGlobal=false&hosts=&consentId=ed678990-f97a-4d6a-9337-6fbb4bbe850f&interactionCount=1&landingPath=NotLandingPage&groups=BG154%3A1%2Ct00%3A1%2CBG155%3A1%2Cs00%3A1%2Cf00%3A1%2Cm00%3A1%2Ci00%3A1%2Cf11%3A1&AwaitingReconsent=false; _ga_ZWRF3NLZJZ=GS1.1.1693059322.5.1.1693059339.0.0.0; inapptestgroup=',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }
    params = {
        'continue': 'https://accounts.spotify.com/authorize?scope=playlist-modify-private+playlist-modify-public+playlist-read-private+playlist-read-collaborative&response_type=token&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&client_id=8365e8a828f440c992c995ac1977f442',
    }

    r = requests.get('https://accounts.spotify.com/en/login', params=params, cookies=cookies, headers=headers)

    f = open("advanced/access_token.txt", 'w')
    f.write(r.url.split("&")[0].split("=")[1])
    f.close()


def read_access_token():
    f = open("advanced/access_token.txt", 'r')
    access_token = f.read()
    f.close
    return access_token


tracks = []
def get_playlist_tracks(id, url=None):
    # Write code here
    
    f = open('advanced/access_token.txt', 'r')
    access_token = f.read()
    f.close()

    headers = {"Authorization": f"Bearer {access_token}"}

    if url == None:
        r = requests.get(f"https://api.spotify.com/v1/playlists/{id}/tracks", headers=headers)
    else:
        r = requests.get(url, headers=headers)


    # Checks for expiration
    try:
        if json.loads(r.text)['error']['message'] == "The access token expired":
            renew_access_token()
            get_playlist_tracks()
    except:
        # Change what output to print here
        d = json.loads(r.text)
        playlist = d['items']

        for track in playlist:
            tracks.append({ track['track']['name'] : track['track']['id'] })

        if d['next'] is not None:
            get_playlist_tracks(id, d['next'])
            return tracks
        else:
            return tracks


def find_duplicates(id):
    track_names = [list(track.keys())[0] for track in get_playlist_tracks(id)]

    return [item for item, count in collections.Counter(track_names).items() if count > 1]


def find_playlist():
    playlist_query = input("\nSearch for a playlist: ")

    f = open('advanced/access_token.txt', 'r')
    access_token = f.read()
    f.close()

    headers = {"Authorization": f"Bearer {access_token}"}
    r = requests.get(f"https://api.spotify.com/v1/search?q={playlist_query}&type=playlist", headers=headers)

    print()
    playlists = []
    for count, playlist in enumerate(json.loads(r.text)['playlists']['items'], 1):
        print(count, F.BLUE + playlist['name'].strip() + F.RESET, "by", F.GREEN + playlist['owner']['display_name'] + F.RESET, f"({playlist['tracks']['total']} total tracks)")
        playlists.append({ playlist['name'] : playlist['id']})

    number_inp = input("\nChoose playlist (1 - 20): ")

    return playlists[int(number_inp) - 1]


def create_new_playlist():
    f = open('advanced/access_token.txt', 'r')
    access_token = f.read()
    f.close()

    headers = {"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'}
    name = input("\nEnter your own playlist name: ")
    json_data = {"name": name, "description": " ", "public": True}

    r = requests.post(f"https://api.spotify.com/v1/users/{user_id}/playlists", headers=headers, json=json_data)
    created_playlist_id = json.loads(r.text)['id']
    print("\nMade playlist")

    return created_playlist_id


def add_to_playlist(playlist_id, track_ids):
    headers = {"Authorization": f"Bearer {read_access_token()}", 'Content-Type': 'application/json'}
    r = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}", headers=headers)

    for count in range(0, math.floor(len(track_ids) / 100) + 1):

        if count != math.floor(len(track_ids) / 100):
            uris = []

            for track_id in track_ids[count * 100 : (count + 1) * 100]:
                uris.append(f"spotify:track:{track_id}")

            json_data = {"uris": uris}
            requests.post(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers, json=json_data)

        else:
            uris = []
            
            for track_id in track_ids[count * 100 : ]:
                uris.append(f"spotify:track:{track_id}")

            json_data = {"uris": uris}
            requests.post(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers, json=json_data)


def duplicate_playlist():
    created_playlist_id = create_new_playlist()

    playlist_obj = find_playlist()
    playlist_name = list(playlist_obj.keys())[0]
    playlist_id = list(playlist_obj.values())[0]

    print(f"Getting all tracks from {playlist_name}...")

    playlist = get_playlist_tracks(playlist_id)

    playlist_track_ids = [list(track_id.values())[0] for track_id in playlist]

    add_to_playlist(created_playlist_id, playlist_track_ids)

    print("\nDuplicated playlist")


def rap_song_playlist():
    rap_caviar = {'name': 'RapCaviar', 'id': '37i9dQZF1DX0XUsuxWHRQd'}
    my_playlist = {'name': 'jit trippin outta this world', 'id': '6HpwiIPG2cJFT5YefGrLhl'}
    
    tracks = get_playlist_tracks(rap_caviar['id'])
    playlist_track_ids = [list(track_id.values())[0] for track_id in tracks]

    add_to_playlist(my_playlist['id'], playlist_track_ids)


rap_song_playlist()
