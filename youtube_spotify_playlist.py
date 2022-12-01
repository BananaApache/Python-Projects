
from cmd import PROMPT
from copyreg import pickle
from termios import VDISCARD
from textwrap import indent
from colorama import Fore as F
import sys
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json
import pickle
import spotify_request
import time as t

try:
    print()
    print(F.WHITE)

    # START LOADING CREDENTIALS

    credentials = None

    if os.path.exists("token.pickle"):
        print("Loading Credentials From File...")
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print("Refreshing Acccess Token...")
            credentials.refresh(Request())
        else:
            print("Fetching New Tokens")
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', scopes=["https://www.googleapis.com/auth/youtube",
                                              "https://www.googleapis.com/auth/youtube.third-party-link.creator",
                                              "https://www.googleapis.com/auth/youtube.readonly",
                                              "https://www.googleapis.com/auth/youtubepartner",
                                              "https://www.googleapis.com/auth/youtube.force-ssl"]
            )

            flow.run_local_server(port=8080, prompt='consent',
                                  authorization_prompt_message='')

            credentials = flow.credentials

            with open("token.pickle", "wb") as f:
                print("Saving Credentials for Future Use")
                pickle.dump(credentials, f)

    youtube = build('youtube', 'v3', credentials=credentials)

    # END

    # MAKES NEW PLAYLIST IF INPUT IS YES

    inp = input("Create new playlist? ")

    if inp == "y":
        playlist_name = input("Enter playlist name: ")
        request = youtube.playlists().insert(
            part="snippet,contentDetails,status",
            body={
                "snippet": {
                    "title": playlist_name
                },
                "status": {
                    "privacyStatus": "public"
                }
            }
        )

        response = request.execute()

        playlist_id = response['id']

    # END

    # GETS SONGS IN SPOTIFY PLAYLIST

    rapper = input("Which rapper to get songs from? ")

    playlist_dict = spotify_request.playlist_ids()

    for n, i in playlist_dict.items():
        if n == rapper:
            spotify_playlist_id = i
            break

    songs_json = spotify_request.get_playlist_songs(
        playlist_id=spotify_playlist_id)

    total = songs_json['total']

    div = total / 50

    if type(div) == float:
        loop_time = int(div) + 1
    else:
        loop_time = int(div)

    offset_count = 0
    c = 0

    song_names = []

    for i in range(loop_time):
        songs = spotify_request.get_playlist_songs(
            playlist_id=spotify_playlist_id, offset=offset_count)

        for name in songs['items']:
            song_names.append(name['track']['name'])

        offset_count += 50

    # END

    # SEARCHES FOR VIDEO

    for song in song_names:
        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            q=f"{song} {rapper}"
        )
        response = request.execute()

        vid_id = response['items'][0]['id']['videoId']

        # END

        # ADD VIDEO TO PLAYLIST

        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "position": 0,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": vid_id
                    }
                }
            }
        )
        response = request.execute()

        t.sleep(5)

    # END

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(F.LIGHTRED_EX, e)
    print(exc_type, fname)
    print('Line:', exc_tb.tb_lineno, F.RESET)

print(F.RESET)
print()
