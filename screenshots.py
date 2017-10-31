from selenium import webdriver
from time import sleep
from PIL import Image
import re
import time
import os

site = "https://www.youtube.com/watch?v="

timing="?t=15s"
root="imageDir"
delay=30
min_video_length=240
#RAI video_list=["mqVATxC6zE4","hCTpOZ8Zxsk","7_9_C9_KH7w","I4EcTBx5Pek","zBBLQX0xUno","oegBKgmVXCY","PgIVXZ6ZfWw","hxHodoSVAKc","mqVATxC6zE4","FbkffLWm0wg","2L2T7a102aU"]

#BBC
#tag="bbc"
#video_list=['XxO_5_0xGdw','7-eRFEE0PI0','YdU7fUXDLpI','aUxLYl0upk0','kefm18yAFco','hqIapjm7t3I','P0YKqL-bgiw','aJ7dzuwYRl4','ZTHe-8mhv0s','3D1_sRg22ms']

#France2
#tag='france2'
#video_list=['J9CpBniDRYQ','R2114URg2fs','QgMzi3Ymh9I','7RXHDEi79EI','GdKQ9xBeYj4','kBZiIu0rR9k','R-HYYJPFw3g','TsHLcHWV15E','eHMc9r6NPpE','szrLJPYAwCA']

#Ard
#tag='ard'
#video_list=['13n9i7FT2B0','l4FCe0n4RWg','ZruVC1zjWXI','XXt9Emq_TO8','XZl7esMLyDY','QddDLNmaOFI','SzvLvYOF6h4','AOYvJ4Xuaos','hJVS3wPVE40','PLQrsocOZ_VCkLO18itQZ4qyNvWJFXtfZ2','YzhE3Rm2dII&index=13&list=PLQrsocOZ_VCkLO18itQZ4qyNvWJFXtfZ2']

#RTVE
#tag='RTVE'
#video_list=['sFKIMyXw4rw','sfBIylfnGrs','K3y2KjJsiJg','qofdlL-d5l4','I0u-44PuJq0','ORDYXw9voe8','wqqMfiLcuA8','2NEOOVUngho','0rp25foJ5go','Xyib46SR3OU','DZeBh_Vf_fg','6rcOXrp4ZUU']


#RTBF
#tag='RTBF'
#video_list=['DZ9DG1fMu3A','1Yxozs6Vy44','e7ZqtntGESg','vbNPhlnBMcw','kntfWStl4GQ','m7WdSc8v3ec','gHbdbh0JZwg','vbNPhlnBMcw','Aw2wldpj0Lg','h0wwinu7wio','pxiX5eKnKB8','NYlhB1bpKyk','E3vv6dlJZAA','m5RR88UypBE','_3LrmDcyM74','ZaIe2i7Xj4U','9XQNEBXVRxo']


#tag='fakeRai'
#video_list=['FlthV_MyTOA','a0rNZu0QLbk','8N8lEQIvOYg','cflGOEAaXVc','Unrq8liEX-U','28vVjFofR9k','4WlFLAm4ujk','BFprFy3QKVI','cIH87u4w-sU','GJ1-p9KlKOM','G02we3upyAc','3ECBlyfR8c4','6bZNEYV-ft4','H0PDaQXMte8','8aINVsVO7GU','8aINVsVO7GU']


tag='Rai1'
video_list=['PRTILCNsSGE','kcGFVz9lrn4','6kYKQ-93sLA','35-YXUAkYRo','iK8f05HF3gg']


def getScreenshots(video):
	fox = webdriver.Firefox()
	fox.implicitly_wait(10)
	fox.get(site+video+timing)
	# Extract data duration
	timeValue = fox.find_element_by_xpath("//meta[@itemprop='duration']")
	#struct_time = time.strptime(timeValue.get_attribute("content"), "PT%MM%SS")
	#durata_video=int(struct_time.tm_min*60)+int(struct_time.tm_sec)
	#print("Durata video: "+ str(durata_video)+ "secondi")
	durata_video=241
	sleep(1)
	if durata_video > min_video_length: 
		element = fox.find_element_by_css_selector('div.player-api.player-width.player-height') # find part of the page you want image of
		#player-api player-width player-height
		location = element.location
		size = element.size
		try: 
		    os.makedirs(root+"/"+video)
		except OSError:
		    if not os.path.isdir(root+"/"+video):
		        raise
		for x in range(1, 4):
			sleep(delay)
			for y in range(1, 3):
				fox.save_screenshot(root+"/"+video+"/"+tag+"_"+video+'.png') # saves screenshot of entire page
				im = Image.open(root+"/"+video+"/"+tag+"_"+video+'.png') # uses PIL library to open image in memory
				left = location['x']
				top = location['y']
				right = location['x'] + size['width']
				bottom = location['y'] + size['height']
				label=x+y
				im = im.crop((left, top, right, bottom)) # defines crop points
				im.save(root+"/"+video+"/"+tag+"_"+video+'_'+str(x)+'_'+str(y)+'.png') # saves new cropped image
				print(root+"/"+video+"/"+tag+"_"+video+'_'+str(x)+'_'+str(y)+'.png')
		os.remove(root+"/"+video+"/"+tag+"_"+video+'.png') 
	fox.quit()


for video in video_list:
	getScreenshots(video)