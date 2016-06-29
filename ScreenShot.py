#!/usr/bin/python

import os
import sys
import time
import ImageGrab
import Image
from os import environ
import random
n = -1
while True:
        n += 1
        # generate a random time between 120 and 300 sec
        random_time = random.randrange(120,300)
        # wait between 120 and 300 seconds (or between 2 and 5 minutes)
        print "Next picture in: %.2f minutes" % (float(random_time) / 60)
        time.sleep(random_time)
        img = ImageGrab.grab()
        FILES_DIR = 'pic'
        SAVE_PATH = os.path.join(environ['HOMEDRIVE'], environ['HOMEPATH'])
        #SAVE_PATH = os.path.expanduser("~")    #It is cross-platform
        LOGFILE_NAME = "test{n:0>5}.png".format(n = n)
        LOGFILE_PATH = os.path.join(SAVE_PATH, FILES_DIR, LOGFILE_NAME)
        img.save(LOGFILE_PATH)
