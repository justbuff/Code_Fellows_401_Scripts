#!/bin/usr/python3

import datetime
import time
import os
import smtplib

user_ip = input("Please enter IP address: ") 
user_email = input("Please enter your email address: ")
user_password = input("Please enter your email password: ")
current_output = 0
last_output = 0

def ping():
    response = os.system("ping -n 1 " + user_ip)
    if response == 0:
        print(datetime.datetime.now(), user_ip, 'is up')
    else:
        print(datetime.datetime.now(), user_ip, 'is down')
    time.sleep(2)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

server.login(user_email, user_password)

def send_upAlert():
    datetime.datetime.now()
    msg = "Server is up!"
    server.sendmail('flyhomes123@gmail', user_email, msg)
    server.quit()
    
def send_downAlert():
    datetime.datetime.now()
    msg = "Server is down!"
    server.sendmail('flyhomes123@gmail', user_email, msg)
    server.quit()
  
while True:
    current_output == ping()
    if current_output == last_output:
        if current_output == True:
            send_upAlert()
        if current_output == False:
            send_downAlert()
    last_output = current_output
