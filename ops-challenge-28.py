#!/usr/bin/env python3

import os
import logging
import datetime
import time
from logging

logger = logging.getLogger('logger_example')
logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

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
