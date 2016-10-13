#!/usr/bin/python
import Queue
import threading
import time
from selenium import webdriver
from time import sleep
from PIL import Image
import re
import time
import os
import csv
import time
site = "https://www.youtube.com/watch?v="

timing="?t=15s"
root="imagesThread11-10-2016"
delay=30
min_video_length=240
video_list=[]

start = time.time()



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
        for x in range(1, 4):
            sleep(delay)
            for y in range(1, 3):
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
        os.remove(new_root+"/"+tag+"_"+video+'.png') 
    fox.quit()


video_list=fileRead("url.txt")

    
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data[0]+"_"+data[1])
            getScreenshots(data[0],data[1])
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3","Thread-4", "Thread-5", "Thread-6","Thread-7", "Thread-8", "Thread-9"]

queueLock = threading.Lock()
workQueue = Queue.Queue(1000)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for tag,video in video_list:
    
    workQueue.put([tag,video])


queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"

end = time.time()
print("Video Analized:",len(video_list))
print("Elaspsed computational time: ",end - start)