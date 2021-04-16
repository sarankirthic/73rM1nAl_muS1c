import os
from pytube import Playlist

os.clear()
PATH = os.path.dirname(os.path.abspath(__file__))
print(f"Present Working Directory :{PATH}")

print(' __ _   _                                   __      ')
print('  / _) |_) |\\/| /| ._   /\\  |    ._ _      (_ /|  _ ')
print(" /  _) | \\ |  |  | | | /--\\ | __ | | | |_| __) | (_ ")         


PATH = PATH + '/Music'
if os.path.exists(PATH)==0:
	os.mkdir(PATH)
os.system(f'cd {PATH}')


if __name__ = "__main__":
	if i == True:
		choice1 = int(input("U Downloading\n1. One File\n2. Playlist\n")
		link = ""
		if choice1 == 1:
			i = False

		else if choice1 == 2:
			i = False
			
		else:

			print("Enter number between 1-2")
	lit = Playlist(link)
	for file in lit.videos:
		title = file.title
		title = title.replace(" ","")
		count = 0
		flag1 = 0
		flag2 = 0
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