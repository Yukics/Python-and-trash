#!/bin/python3

import time
import sys
import os
from PIL import Image

file = sys.argv[1]

#Basic checking input
if file == "":
    print("Give a gif location /home/yuki/images/something.gif")

if not file.endswith(".gif"):
    print("Introduce a gif")

if os.path.isdir('/tmp/wall'):
    os.system('rm -r /tmp/wall && mkdir /tmp/wall')
else:
    os.system('mkdir /tmp/wall')

#Get number of frames of the gif
num_key_frames = int(os.popen("identify "+file+"| wc -l").read())

#Split gif into images
with Image.open(file) as im:
    for i in range(num_key_frames):
        im.seek(im.n_frames // num_key_frames * i)
        im.save('/tmp/wall/{}.png'.format(i))

#Get timings of every frame
times = os.popen("identify "+file+" | cut -d ':' -f 2").read().split("s")
timing = [s.replace("\n", "") for s in times]
while("" in timing) :
    timing.remove("")

#This slows by 4 the speed
speed=4

#This loop changes the images that compose the gif
while True:
    for pic in zip(range(num_key_frames-1), timing):
        print(pic)
        os.system('feh --bg-fill /tmp/wall/'+str(pic[0])+'.png')
        time.sleep(float(pic[1])*speed)
