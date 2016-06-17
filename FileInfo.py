#!/usr/bin/python

import os
import sys
import pwd

fileStat = os.stat(sys.argv[1])

if fileStat:
     print('Filename: %s' % sys.argv[1])
     print('Size: %d' %fileStat.st_size)
     print('Owner: username is %s' %(fileStat.st_uid,pwd.getpwuid(fileStat.st_uid).pw_name))
