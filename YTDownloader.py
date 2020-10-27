#importing the module 
from pytube import YouTube, Playlist
import os
from os import path
import re
import requests as rq
import responses as rs 
from requests.exceptions import ConnectionError


def dlprogress(s, c, bytes_left):
	print('Downloading [{:.1f} MB / {:.1f} MB]  {:.2%}'.format((s.filesize - bytes_left)/1000000, s.filesize/1000000,  (s.filesize - bytes_left)/s.filesize), end='\r')


#DOWNLADING SINGLE VIDEO
def singleVideo(link,savePath = ''):

	try:
		rs = rq.get(link)
		yt = YouTube(link, on_progress_callback=dlprogress) 

		stream = yt.streams.first()
		stream.download(savePath)
		print('')
	except rq.ConnectionError as exception:
 		print("URL does not exist on Internet")

# #DOWNLOADING MULTIPLE VIDEOS 
def playlistVideos(link,savePath = ''):

	try:
		rs = rq.get(link)
		#Making directory 

		directory = "Downlaoded Playlist"
		SAVE_PATH = "./"
		# Parent Directory path 
		parent_dir = SAVE_PATH

		# Path 
		path = os.path.join(parent_dir, directory) 

		isdir = os.path.isdir(path)  
	
		if isdir == False:

			os.mkdir(path) 
			playlist = Playlist(link)
			playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

			

			for url in playlist.video_urls:
				yt2 = YouTube(url,on_progress_callback=dlprogress) 

				stream2 = yt2.streams.first()
				stream2.download(path)
				print('')


		else: 

			playlist = Playlist(link)
			playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

			

			for url in playlist.video_urls:
				yt2 = YouTube(url,on_progress_callback=dlprogress) 

				stream2 = yt2.streams.first()
				stream2.download(path)
				print('')
	except rq.ConnectionError as exception:
 		print("URL does not exist on Internet")


#DOWNLODING LINKS FROM A FILE 
def videoFromFiles(savePath = ''):
	
	link3=open('links.txt','r') #opening the file 
	
	for i in link3:
		#print(i)
		yt3 = YouTube(i,on_progress_callback=dlprogress) 
		stream3 = yt3.streams.first()
		stream3.download(savePath)
		print('')

	print("URL does not exist on Internet")
		
if __name__=='__main__':
	SAVE_PATH = "./" 
	print("Which value to choose? 1 to dl single video, 2 to dl playlist, 3 to dl from file, 4 to exit")
	menu=0
	while menu !=4:
		print("")
		menu = int(input("Select an option: "))

		if menu == 1:

			link1='https://www.youtube.com/watch?v=REM-L1PUMA8'
			singleVideo(link1,SAVE_PATH)
		
		elif menu== 2: 

			link2 = 'https://www.youtube.com/playlist?list=PLZbbT5o_s2xpOpsGIuk4qHek6KxeQACHf'
			playlistVideos(link2,SAVE_PATH)

		elif menu == 3:

			videoFromFiles(SAVE_PATH)
		
		else:
			print("Invalid Option ")