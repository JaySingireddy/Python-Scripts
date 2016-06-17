#!/usr/bin/python

import os
import sys

pre = ''

for (path, dirs, files) in os.walk(sys.argv[1]):
        depth_from_root = len(path.split('/'))
        print('-'*(depth_from_root*4 +8) + '[' + path.split('/')[-1] + ']')
        for file in files:
            print('-'*(depth_from_root*4 +13) + ' ' +file)
            
