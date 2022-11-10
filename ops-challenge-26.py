#!/usr/bin/env python3

import os
import logging
import datetime
import time

logging.basicConfig(filename='26log.txt', encoding='utf-8', level=logging.DEBUG)

def check_ping():
    print("Logging Started")
    logging.debug("Start Log")
    response = os.system("ping -n 1 8.8.8.8") 
    if response == 0: 
        print(datetime.datetime.now(), '8.8.8.8 is up')
        logging.info("8.8.8.8 is up")
    else:
        print(datetime.datetime.now(), '8.8.8.8 is down')
        logging.error("8.8.8.8 is down")
    time.sleep(2)
    print("Logging End")

if __name__ == '__main__':
    check_ping()
