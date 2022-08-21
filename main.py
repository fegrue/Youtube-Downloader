from pytube import YouTube
from sys import argv


link = input("Enter link:")

yt = YouTube(link)
print("Title: ", yt.title)
print("Duration: ", yt.length)

yd = yt.streams.get_highest_resolution()
for stream in yt.streams:
    print(stream.resolution)



yd.download('./')