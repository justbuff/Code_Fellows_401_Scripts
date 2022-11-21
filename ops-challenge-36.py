#!/usr/bin/env python3

import socket
import time
import subprocess

a = input("Please enter an IP or URL address: ")
p = input("Please enter a port number: ")

def netcap(a, p):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((a, int(p)))
  
  run = "nc" + a + " " + p
  sock.sendall(run.encode())
  res = " "
  
  while True:
    data = sock.recv(1024)
    if (not data):
      break
    res += data.decode()
    
  print(res)
  
  sock.close()
  
def telnet():
