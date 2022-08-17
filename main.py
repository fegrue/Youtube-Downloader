from pytube import YouTube
from sys import argv


link = argv[1]
yt = YouTube(link)
print("Title: ", yt.title)
print("Duration: ", yt.length)

yd = yt.streams.get_highest_resolution()

yd.download('./downloaded')