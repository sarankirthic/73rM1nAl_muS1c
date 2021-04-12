import os
from pytube import Playlist

PATH = os.path.dirname(os.path.abspath(__file__))
print(f"Present Working Directory :{PATH}")
lit = Playlist('https://www.youtube.com/playlist?list=PLheRaNbuz8moz0JhNcqpBLMl6jFo11e2k')
print(f'Downloading: {lit.title}')

PATH = PATH + '/Music'
if os.path.exists(PATH)==0:
	os.mkdir(PATH)
	print('Hello')
os.system(f'cd {PATH}')

for file in lit.videos:
	title = file.title
	title = title.replace(" ","")
	count = 0
	flag1 = 0
	flag2
	 = 0
	for letter in title:
		count+=1
		if letter =='(':
			flag1 = count
		if letter ==')'
			flag2 = count


	if file.title in os.listdir():
		print(f"Song already Downloaded :{file.title}")
	else:
		print(f'Downloading :{title}')
		#file.streams.first().download(PATH, filename=title, includes_video_track=False, includes_audio_track=True)
