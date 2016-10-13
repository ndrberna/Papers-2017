from selenium import webdriver
from time import sleep
from PIL import Image
import re
import time
import os
import csv
from subprocess import call

video_list=[]



def fileRead(url):

	with open(url, 'rb') as f:
	    reader = csv.reader(f)
	    video_list = list(reader)

	return video_list
	

video_list=fileRead("url.txt")

for tag,video in video_list:
	try:
		title="-o videoArchive/"+str(tag)+"_%(id)s"
		call(["youtube-dl",title,str(video)])

	except:
		pass	