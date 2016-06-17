#!/usr/bin/python

import sys

if sys.platform.startswith('darwin'):
    print('Macintosh OS X detected')
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    print('Microsoft Windows OS detected')
    print(sys.getwindowsversion())
elif sys.platform.startswith('linux'):
    print('linux OS detected')
else:
    print(sys.platform + ' ' + 'OS detected')

    
