#!/usr/bin/python

from sys import argv
import subprocess

replica = argv
name = str(replica[0])
print(name)

for x in range(0,1):
    folderName = 'Windows' +str(x)
    subprocess.call(['mkdir',folderName])
    subprocess.call(['cp', name,folderName])
