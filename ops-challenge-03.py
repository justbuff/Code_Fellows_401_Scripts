#!/bin/usr/python3

import datetime
import time
import os
import smtplib

user_ip = input("Please enter IP address: ") 
user_email = input("Please enter your email address: ")
user_password = input("Please enter your email password: ")
current_ping = 0
last_ping = 0

def ping():
    response = os.system("ping -n 1 " + user_ip)
    if response == 0:
        return True
    else:
        return False

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

server.login(user_email, user_password)

def send_upAlert():
    print(datetime.datetime.now())
    msg = "Server is up!"
    server.sendmail('flyhomes123@gmail', user_email, msg)
    server.quit()
    
def send_downAlert():
    print(datetime.datetime.now())
    msg = "Server is down!"
    server.sendmail('flyhomes123@gmail', user_email, msg)
    server.quit()
  
while True:
    current_ping = ping()
    time.sleep(2)
    if current_ping != last_ping:
        if current_ping == True:
            send_upAlert()
        if current_ping == False:
            send_downAlert()
    last_ping = current_ping 
