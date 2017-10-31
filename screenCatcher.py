from selenium import webdriver
from time import sleep
from PIL import Image
import re
import time
import os
import csv
site = "https://www.youtube.com/watch?v="

timing="?t=15s"
root="images18-10-2016"
delay=10
min_video_length=240
video_list=[]



def fileRead(url):

	with open(url, 'rb') as f:
	    reader = csv.reader(f)
	    video_list = list(reader)

	return video_list
	


def getScreenshots(tag,video):
	fox = webdriver.Firefox()
	fox.implicitly_wait(10)
	fox.get(site+video+timing)
	# Extract data duration
	#timeValue = fox.find_element_by_xpath("//meta[@itemprop='duration']")
	#struct_time = time.strptime(timeValue.get_attribute("content"), "PT%MM%SS")
	#durata_video=int(struct_time.tm_min*60)+int(struct_time.tm_sec)
	#print("Durata video: "+ str(durata_video)+ "secondi")
	durata_video=241
	sleep(1)
	if durata_video > min_video_length: 
		element = fox.find_element_by_css_selector('div.player-api.player-width.player-height') # find part of the page you want image of
		#player-api player-width player-height
		new_root=root+"/"+tag+"_"+video
		location = element.location
		size = element.size
		try: 
		    os.makedirs(new_root)
		except OSError:
		    if not os.path.isdir(new_root):
		        raise
		for x in range(1, 30):
			sleep(delay)
			for y in range(1, 3):
				sleep(5)
				try: 
					fox.save_screenshot(new_root+"/"+tag+"_"+video+'.png') # saves screenshot of entire page
					im = Image.open(new_root+"/"+tag+"_"+video+'.png') # uses PIL library to open image in memory
					left = location['x']
					top = location['y']
					right = location['x'] + size['width']
					bottom = location['y'] + size['height']
					label=x+y
					im = im.crop((left, top, right, bottom)) # defines crop points
					im.save(new_root+"/"+tag+"_"+video+'_'+str(x)+'_'+str(y)+'.png') # saves new cropped image
					im.save(root+"/"+tag+"_"+video+'_'+str(x)+'_'+str(y)+'.png') # saves new cropped image
					print(new_root+"/"+tag+"_"+video+'_'+str(x)+'_'+str(y)+'.png')
				except:
					pass
					x=30

		os.remove(new_root+"/"+tag+"_"+video+'.png') 
	fox.quit()


video_list=fileRead("urlRai.txt")

for tag,video in video_list:
	try:
		print(tag,video)
		getScreenshots(tag,video)
	except:
		pass	