#!/usr/bin/env python3

import os
import logging
import datetime
import time


def check_ping():
    response = os.system("ping -n 1 8.8.8.8") 
    if response == 0: 
        print(datetime.datetime.now(), '8.8.8.8 is up')
    else:
        print(datetime.datetime.now(), '8.8.8.8 is down')
    time.sleep(2) 
  
logging.basicConfig(filename='example.txt', encoding='utf-8', level=logging.DEBUG)
print("Logging Started")
logging.debug("Debug Info")
logging.info("Info")
logging.warning("Warning Info")
logging.error("Error Info")
logging.critical("Critical Info")
print("Logging End")

if __name__ == '__main__':
    check_ping()

