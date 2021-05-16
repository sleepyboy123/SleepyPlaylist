import os
import sys
from pytube import Playlist
from urllib.error import HTTPError

if (len(sys.argv) != 2):
    print("Invalid arguments given, please provide a youtube playlist to be downloaded")
    sys.exit(1)
  
playlist = Playlist(str(sys.argv[1]))

try:
    playlist.title
except KeyError:
    print('Invalid Youtube Playlist URL has been given')
    sys.exit(1)

cur_dir = "C:/Users/Matthew/Desktop/" + playlist.title

try:
    os.mkdir(cur_dir)
    print(str(playlist.title) + " Directory Created")
except FileExistsError:
    print(str(playlist.title) + " Directory already exists")

for video in playlist.videos:
    try:
        print('downloading : {} with url : {}'.format(video.title, video.watch_url))
        video.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(cur_dir)
    except HTTPError:
        print("HTTP Error 404 :{}".format(video.watch_url))