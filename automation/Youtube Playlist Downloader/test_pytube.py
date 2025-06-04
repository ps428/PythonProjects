from pytube import YouTube
import os

address = input("Enter the link:	")
SAVE_PATH = os.getcwd() #to_do 
yt = YouTube(address)

mp4files = yt.filter('mp4') 

d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 

d_video.download(SAVE_PATH) 