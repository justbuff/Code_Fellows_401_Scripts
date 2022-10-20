#!/usr/bin/python3

from sys import flags
from scapy.all import sr,sr1,IP,TCP,ICMP
import random

host=input("Please enter IP address: ")
port_range=[22,23,80,443,3389]

for dst_port in port_range:
  src_port = random.randint(1025,65534)
    resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
    
    if resp is None:
        print(f"{host}:{dst_port} is filtered (silently dropped).")
    
    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags == 0x12):
            send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=1,verbose=0,)
            print(f"{host}:{dst_port} is open.")

        elif (resp.getlayer(TCP).flags == 0x14):
            print(f"{host}:{dst_port} is closed.")
  
