#!/usr/bin/python3

# WIP

import sys
import scapy
from sys import flags
from scapy.all import sr,sr1,IP,TCP,ICMP

host = input("Please enter IP address: ")

port_range = [22, 23, 80, 443, 3389]

for port in port_range:
  
  resp = ls port_range
 
  if resp = None:
    print(host + resp, " is filtered")
  
  elif resp = TCP:
    if resp = sys.flag "0x12"
    print(host + resp, " is open")
    elif resp = sys.flag "0x14"
    print(host + resp, " is closed")
 
  elif resp = ICMP:
    print(host + resp, " is silently dropped)
  
