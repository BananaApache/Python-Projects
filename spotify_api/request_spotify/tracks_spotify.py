
from colorama import Fore as F
import sys
import os
from . import request_spotify as rs
from urllib.parse import urlencode
from datetime import date
import json


def track_links_dict(rapper_name):
    spotify_json = rs.get_raw_albums(artist_name=rapper_name)
    total_albums = spotify_json['total']
    div = total_albums / 50
    if type(div) == float:
        loop_time = int(div) + 1
    else:
        loop_time = int(div)
    offset_count = 0
    album_lst = []
    for i in range(loop_time):
        spotify_json = rs.get_raw_albums(artist_name=rapper_name, offset=offset_count)
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
            album_dict = {
                "album_name": album_name,
                "release_date": str(dt_release),
                "album_id": album_id,
            }
            album_lst.append(album_dict)
        offset_count += 50

    all_tracks = {}
    for alb_info in album_lst:
        # print(str(alb_id['album_id']))
        tracks = rs.get_raw_tracks(
            id=str(alb_info['album_id']), offset=0, limit=50)
        song_lst = []
        for song in tracks['items']:
            song_dict = {}
            song_dict = {
                song['name']: song['external_urls']['spotify']
            }
            song_lst.append(song_dict)
        all_tracks.update({
            alb_info['album_name']: song_lst
        })

    return all_tracks


def all_track_lst(rapper_name):
    spotify_json = rs.get_raw_albums(artist_name=rapper_name)
    total_albums = spotify_json['total']
    div = total_albums / 50
    if type(div) == float:
        loop_time = int(div) + 1
    else:
        loop_time = int(div)
    offset_count = 0
    album_lst = []
    for i in range(loop_time):
        spotify_json = rs.get_raw_albums(artist_name=rapper_name, offset=offset_count)
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
            album_dict = {
                "album_name": album_name,
                "release_date": str(dt_release),
                "album_id": album_id,
            }
            album_lst.append(album_dict)
        offset_count += 50

    all_tracks = []

    for alb_info in album_lst:
        # print(str(alb_id['album_id']))
        tracks = rs.get_raw_tracks(
            id=str(alb_info['album_id']), offset=0, limit=50)

        count = 0

        for track_link in tracks['items']:
            all_tracks.append(track_link['uri'])
            count += 1

    return all_tracks

def all_track_dict(rapper_name):
    spotify_json = rs.get_raw_albums(artist_name=rapper_name)
    total_albums = spotify_json['total']
    div = total_albums / 50
    if type(div) == float:
        loop_time = int(div) + 1
    else:
        loop_time = int(div)
    offset_count = 0
    album_lst = []
    for i in range(loop_time):
        spotify_json = rs.get_raw_albums(artist_name=rapper_name, offset=offset_count)
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
            album_dict = {
                "album_name": album_name,
                "release_date": str(dt_release),
                "album_id": album_id,
            }
            album_lst.append(album_dict)
        offset_count += 50

    all_tracks = {}

    for alb_info in album_lst:
        # print(str(alb_id['album_id']))
        tracks = rs.get_raw_tracks(
            id=str(alb_info['album_id']), offset=0, limit=50)

        count = 0

        for track_link in tracks['items']:
            all_tracks.update({track_link['name']: track_link['uri']})
            count += 1

    return all_tracks
