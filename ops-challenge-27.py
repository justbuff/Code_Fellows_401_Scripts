#!/usr/bin/env python3

import logging
import time
from logging.handlers import TimedRotatingFileHandler
import os
import datetime


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
    
def create_timed_rotating_log(path):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    handler = TimedRotatingFileHandler(path,
                                       when="h",
                                       interval=1,
                                       backupCount=5)
    logger.addHandler(handler)
    
    for i in range(6):
        logger.info("This is a test!")
        time.sleep(75)

if __name__ == "__main__":
    log_file = "timed_test.log"
    create_timed_rotating_log(log_file)
  


if __name__ == '__main__':
    check_ping()


