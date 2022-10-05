#!/usr/bin/python3

import datetime
import time
import os

# function
def check_ping():
    # variable
    response = os.system("ping -n 1 8.8.8.8") # pings 8.8.8.8 once
    if response == 0: # non-zero responses are failed pings
        print(datetime.datetime.now(), '8.8.8.8 is up')
    else:
        print(datetime.datetime.now(), '8.8.8.8 is down')
    time.sleep(2) # time between pings 2 seconds

# infinite while loop
while True:
    check_ping()
