
from ntpath import join
from colorama import Fore as F
import sys
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import json

load_dotenv()

try:
    print()
    print(F.WHITE)

    api_key = os.getenv("yt_api_key")
    youtube = build('youtube', 'v3', developerKey=api_key)

    pl_request = youtube.playlists().list(
        part='contentDetails, snippet',
        channelId='UCCezIgC97PvUuR4_gbFUs5g',
    )

    pl_response = pl_request.execute()

    playlist_ids = []

    for item in pl_response['items']:
        playlist_ids.append(item['id'])

    for x in range(len(playlist_ids)):
        pli_request = youtube.playlistItems().list(
            part="contentDetails, snippet",
            playlistId=playlist_ids[x]
        )
        pli_response = pli_request.execute()

        vid_id_lst = []

        for item in pli_response['items']:
            vid_id_lst.append(item['contentDetails']['videoId'])
            print(json.dumps(item, indent=4))

        vid_request = youtube.videos().list(
        part="contentDetails, snippet, statistics",
        id=','.join(vid_id_lst)
    )

        vid_response = vid_request.execute()

        min_total = 0
        sec_total = 0

        total_iso_lst = []

        for item in vid_response['items']:
            new_iso_lst = []
            iso = item['contentDetails']['duration']
            iso_lst = iso[2: len(iso) - 1].split("M")
            new_iso_lst.extend(iso_lst[0].split("H"))
            if len(iso_lst) == 2:
                new_iso_lst.append(iso_lst[1])
            elif len(iso_lst) == 1:
                new_iso_lst.append(0)
            total_iso_lst.append(new_iso_lst)

        for item in total_iso_lst:
            if len(item) == 3:
                min_duration = int(item[0]) * 60 + int(item[1])
                sec_duration = item[2]
            elif len(item) == 2:
                min_duration = int(item[0])
                sec_duration = int(item[1])
            min_total = min_total + min_duration
            sec_total = sec_total + int(sec_duration)

        if sec_total > 60:
            extra_min = int(sec_total/60)
            sec_total = int(sec_total%60)
            min_total = min_total + extra_min

        print("Playlist:", pl_response['items'][x - 1]['snippet']['title'], str(min_total),
              "minutes and", str(sec_total), "seconds long.")

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(F.LIGHTRED_EX, e)
    print(exc_type, fname)
    print('Line:', exc_tb.tb_lineno, F.RESET)

print(F.RESET)
print()
