from pytube import YouTube
import json
import os

print(os.getcwd())
# where to save
SAVE_PATH = "tmpVideos/"

link=open(SAVE_PATH + 'videos.json','r')

data = json.load(link)

print(data['minecraft']['videos'])

for i in data['minecraft']['videos']:
	print(i)
	try:

		# object creation using YouTube
		# which was imported in the beginning
		yt = YouTube(i)
	except:

		#to handle exception
		print("Connection Error")
	print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1])
	d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
	try:

		# downloading the video
		d_video.download(SAVE_PATH)
	except:
		print("Some Error!")

print('Task Completed!')
