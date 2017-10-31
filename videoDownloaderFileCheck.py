# CONVERSIONE
# for i in *.mkv; do avconv -i "$i" -vcodec copy -ac 2 -strict experimental "$i.mp4"; done
#
#


from selenium import webdriver
from time import sleep
from PIL import Image
import re
import time
import os
import csv
from subprocess import call
import time
import os
import csv
import glob
video_list=[]

dirname="videoArchive25_10_2016/"
cleandir=[]

def fileRead(url):

	with open(url, 'rb') as f:
	    reader = csv.reader(f)
	    video_list = list(reader)

	return video_list
	

video_list=fileRead("url_mancanti.txt")
directory=glob.glob(dirname+"*.*")



for file in directory:
	file=file.split(dirname)[1].split(".")[0]
	cleandir.append(file)


for tag,video in video_list:
	if not tag+"_"+video in cleandir:
		try:
			title="-o "+dirname+str(tag)+"_%(id)s"
			call(["youtube-dl",title,str(video)])

		except:
			pass	
