from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
import mutagen.id3

import os
import sys

if len(sys.argv) > 1:
	substringTitle = int(sys.argv[1])
	print("Remove first " + str(substringTitle) + " caracter.")
else:
	substringTitle = 0

directory = 'out'
if not os.path.exists(directory):
    os.makedirs(directory)

for subdir, dirs, files in os.walk('./'):
	for file in files:
		print("file found : " + file)
		lastDotIndex = file.rfind('.')
		if lastDotIndex == -1:
			continue
		fileName = file[:lastDotIndex]
		extension = file[lastDotIndex + 1:]
		outputFileName = os.path.join('out', fileName[substringTitle:].replace("'", ''))
		print("fileName computed : " + file)
		print("extension computed : " + extension)
		if extension == "flac":
			print ("file found : " + fileName)
			if outputFileName + ".mp3" in files:
				print("Already convert.")
				continue
			os.system("vlc -I dummy \"" + fileName + ".flac\" \":sout=#transcode{acodec=mpga,ab=192}:std{dst='" + outputFileName + ".mp3',access=file}\" vlc://quit")
			# MP3
			mf = MP3(outputFileName + ".mp3", ID3=EasyID3)
			#FLAC
			ff = FLAC(fileName + ".flac")
			#Let's go !
			try:
				mf['title'] = ff['title']
			except:
				print ("No title")
			try:
				mf['artist'] = ff['artist']
			except:
				print ("No artist")
			try:
				mf['album'] = ff['album']
			except:
				print ("No album")
			try:
				mf['date'] = ff['date']
			except:
				print ("No date")
			try:
				mf['genre'] = ff['genre']
			except:
				print ("No genre")
			try:
				mf['tracknumber'] = ff['tracknumber']
			except:
				print ("No genre")
			mf.save()
