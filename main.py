# YouTube Video Downloader (Playlist Download)

from pytube import Playlist

py = Playlist() # paste link in it of playlist you want to download...

print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()