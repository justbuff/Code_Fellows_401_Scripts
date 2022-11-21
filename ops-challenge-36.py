#!/usr/bin/env python3

import sys
import socket
import time
import subprocess

prompt_address = input("Please enter an IP or URL address: ")
prompt_port = input("Please enter a port number: ")
content = "GET / HTTP/1.1\n.Host: scanme.nmap.org\n\n"

def netcat(pa, pp):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((pa, pp))
  sock.sendall(content)
  time.sleep(0.5)
  sock.shutdown(socket.SHUT_WR)
  res = ""
  while True:
    data = sock.recv(1024)
    if (not data):
      break
    res += data.decode() 
  print(res)
  sock.close()
 
netcat(prompt_address, prompt_port, content.encode())

telnet prompt_address prompt_port

nmap -Pn -p prompt_port -sV -script=banner prompt_address

