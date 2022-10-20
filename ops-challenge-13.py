#!/usr/bin/python3

# WIP

import random
from sys import flags
from ipaddress import IPv4Network
from scapy.all import ICMP,IP,sr,sr1,TCP

host=input("Please enter IP address: ")
port_range=[22,23,80,443,3389]

def ping_status(host):
  resp=sr1(IP(dst=str(host))/ICMP(),timeout=1,verbose=0)
  if resp==None: 
        print(f"{host} is not responding.")
  elif (int(response.getlayer(ICMP).type)==3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
        print(f"{host} is blocking ICMP.")
    else: 
        print(f"{host} is responding. ")
        port_scan(host,port_range)

def port_scan(host,port_range):
  for dst_port in port_range:
        src_port=random.randint(1025, 65534)
        resp=sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
        if resp is None: 
            print(f"{host}:{dst_port} is filtered (silently dropped).")
        elif (resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags==0x12):
                print(f"{host}:{dst_port} is open.")
            elif(resp.getlayer(TCP).flags==0x14):
                print(f"{host}:{dst_port} is closed.")
                
ping_status(host)
