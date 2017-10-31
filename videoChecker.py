from selenium import webdriver
from time import sleep
from PIL import Image
import re
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
	
directory=glob.glob(dirname+"*.*")

for file in directory:
	file=file.split(dirname)[1].split(".")[0]
	cleandir.append(file)


video_list=fileRead("url25_10_2016.csv")
#print cleandir
count_trovati=0
count_nontrovati=0

for tag,video in video_list:
	if tag+"_"+video in cleandir:
		count_trovati+=1
		
	else:
		count_nontrovati+=1
		print(tag+"_"+video)
	
print ("Mancano:", count_nontrovati)

print ("Trovati:", count_trovati)