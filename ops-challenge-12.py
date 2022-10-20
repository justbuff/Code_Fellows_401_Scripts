#!/usr/bin/python3

import sys
from scapy.all import ICMP,IP,sr1,sr,TCP
import random
from ipaddress import IPv4Network

def option_menu():
    print ("""
    1. TCP Port Range Scanner
    2. ICMP Ping Sweeper
    3. Exit
    """)
    ans=input("Please choose an option: ") 
    if ans=="1":
        port_scan()  
    elif ans=="2":
        ping_sweep()   
    elif ans=="3":
        sys.exit()   
    else:
      print("Please try again")

def port_scan():
  remote_server=input("Please enter an IP address to scan: ")
  remote_serverIP = socket.gethostbyname(remote_server)
  port_range=[22,23,80,443,3389]
  for dst_port in port_range:
        src_port = random.randint(1025, 65534)
        resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
        if resp is None: 
            print(f"{host}:{dst_port} is filtered (silently dropped).")
        elif (resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags==0x12):
                print(f"{host}:{dst_port} is open.")
            elif(resp.getlayer(TCP).flags==0x14):
                print(f"{host}:{dst_port} is closed.")
   
def ping_sweep():
  ip_address=input("Please enter IP address in CIDR notation to ping: ")
  ip_list=IPv4(ip_address)
  live_count=0
  for ip in ip_list:
        resp = sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0,)
        if (host in (ipadd.network_address,ipadd.broadcast_address)):
            continue
        if resp is None:
            print(f"{host} is not responding.")
        elif (int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print(f"{host} is blocking ICMP.")
        else:
            print(f"{host} is responding.")
            live_count += 1

while True:
    option_menu()
  
