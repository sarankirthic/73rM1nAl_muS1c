import os
from pytube import Playlist

os.clear()
PATH = os.path.dirname(os.path.abspath(__file__))
print(f"Present Working Directory :{PATH}")

print( ██████████  ████████            ██████   ██████ ████               █████████   ████                                        █████████  ████          )
print(░███░░░░███ ███░░░░███          ░░██████ ██████ ░░███              ███░░░░░███ ░░███                                       ███░░░░░███░░███          )
print(░░░    ███ ░░░    ░███ ████████  ░███░█████░███  ░███  ████████   ░███    ░███  ░███            █████████████   █████ ████░███    ░░░  ░███   ██████ )
print(      ███     ██████░ ░░███░░███ ░███░░███ ░███  ░███ ░░███░░███  ░███████████  ░███           ░░███░░███░░███ ░░███ ░███ ░░█████████  ░███  ███░░███)
print(     ███     ░░░░░░███ ░███ ░░░  ░███ ░░░  ░███  ░███  ░███ ░███  ░███░░░░░███  ░███            ░███ ░███ ░███  ░███ ░███  ░░░░░░░░███ ░███ ░███ ░░░ )
print(    ███     ███   ░███ ░███      ░███      ░███  ░███  ░███ ░███  ░███    ░███  ░███            ░███ ░███ ░███  ░███ ░███  ███    ░███ ░███ ░███  ███)
print(   ███     ░░████████  █████     █████     █████ █████ ████ █████ █████   █████ █████ █████████ █████░███ █████ ░░████████░░█████████  █████░░██████ )
Print(  ░░░       ░░░░░░░░  ░░░░░     ░░░░░     ░░░░░ ░░░░░ ░░░░ ░░░░░ ░░░░░   ░░░░░ ░░░░░ ░░░░░░░░░ ░░░░░ ░░░ ░░░░░   ░░░░░░░░  ░░░░░░░░░  ░░░░░  ░░░░░░  )

def fun1:
	# for downloading 1 - Video
	print("Not Complete")

def fun2:
	# for downloading 1 - Audio
	print("Not Complete")

def fun3(URL):
	# for downloading Playlist of Video's
	PATH = PATH + '/Music'
	if os.path.exists(PATH)==0:
		os.mkdir(PATH)
	os.system(f'cd {PATH}')


	lit = Playlist(URL)
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
		file.streams.first().download(PATH, filename=title, includes_video_track=False, includes_audio_track=True)

def fun4:
	# for downloading Playlist of Audio's
	print("Not Complete")



choice1 = int(input("U Downloading a\n1. One File\n2. Playlist\n")
URL = ""
if choice1 == 1:
	URL = input(f"Enter the URL")
else if choice1 == 2:
	ch2 = input("U want to convert it into a Audio File?Y/N")
	if choice2.lower == 'y':
		fun4
	else if choice2.lower == 'n':
		URL = input(f"Enter the URL")
		fun3
else:
	print(f"Enter number between 1-2")

print(f"Enter the ")
lit = Playlist(URL)
print(f'Downloading: {lit.title}')

PATH = PATH + '/Music'
if os.path.exists(PATH)==0:
	os.mkdir(PATH)
os.system(f'cd {PATH}')

