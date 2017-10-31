from selenium import webdriver
from time import sleep
from PIL import Image
import re
import time
import os,sys
import csv
from subprocess import call

video_list=[]
url_dir="frames25_10_2016/"
#ffmpeg -i input.flv -ss 00:00:14.435 -vframes 1 out.png
frame_number=4
def fileRead(url):

	with open(url, 'rb') as f:
	    reader = csv.reader(f)
	    video_list = list(reader)

	return video_list
	


video_list=fileRead("url.txt")

directory=call(["pwd"])




video_format=["mp4","mpg","mpeg", "mkv"]

results=os.listdir(os.curdir+"/videoArchive25_10_2016")
for single_result in results:
	length=call(["avprobe", "videoArchive25_10_2016/" + single_result])

	print length


	if (single_result.split(".")[1]) in video_format:
		print single_result.split(".")[1]
		#call("mkdir",single_result.split(".")[0])
		for x in range(1, frame_number):
			try:
	
				call(["avconv", "-i","videoArchive25_10_2016/"+str(single_result), "-ss", "00:0"+str(x)+":00", "-t", "1", "-qscale", "1", "-r", "1", "-f", "image2", url_dir+str(single_result.split(".")[0])+str(x)+"_1.jpg"])
				call(["avconv", "-i","videoArchive25_10_2016/"+str(single_result), "-ss", "00:0"+str(x)+":30", "-t", "1", "-qscale", "1", "-r", "1", "-f", "image2", url_dir+str(single_result.split(".")[0])+str(x)+"_2.jpg"])
				
			except:
				pass
