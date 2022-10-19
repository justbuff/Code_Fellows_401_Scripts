#!/usr/bin/python3

# WIP


import sys  
from sys import flags
from scapy.all import ICMP, IP, sr1, sr, TCP
import random
from ipaddress import IPv4Network
from datetime import datetime

print ("""
    1. TCP Port Range Scanner
    2. ICMP Ping Sweeper
    3. Exit
    """)
    # asks for user input
    ans=raw_input("Please choose an option: ") 
    if ans=="1":
        port_scan()
        
    elif ans=="2":
        ping_sweep()
        
    elif ans=="3":
        sys.exit()
        
    else:
      print("\n Please try again")
 

def port_scan():
  remote_server=input("Please enter an IP address to scan: ")
  remote_serverIP = socket.gethostbyname(remote_server)
  port_range=[22,23,80,443,3389]
  
  try:
    for port in port_range:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = sock.connect_ex((remote_serverIP, port))
      if result ==0:
        print "Port {}:        Open".format(port)
        sock.close()
        
        except KeyboardInterrupt:
          print("You pressed Ctrl+C")
          sys.exit()
        
        except socket.gaierror:
          print("Hostname could not be resolved. Exiting")
          sys.exit()
          
        except socket.error:
          print("Couldn't connect to server")
          sys.exit()

     
def ping_sweep():
  ip_address=input("Please enter IP address to ping: ")
  ip_list=IPv4(ip_address)
  print(ip_list)
  
  for ip in ip_list:
  
    elif(resp.haslayer(ICMP)):
        if(
            int(resp.getlayer(ICMP).type) == 3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host}:{dst_port} is filtered (silently dropped).")
  
  
  
  
