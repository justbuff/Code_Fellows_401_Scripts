#!/usr/bin/python3

import socket
import math

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 10
sockmod.settimeout(timeout)

hostip = input("Enter your host IP: ")
portno = input("Enter a port number: ")
math.floor(portno)

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)) == 0:
        print("Port closed")
    else:
        print("Port open")

portScanner(port)
