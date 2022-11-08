#!/usr/bin/env python3

import os
import logging



def log_script:
  

logging.basicConfig(filename='example.txt', encoding='utf-8', level=logging.DEBUG)
print("Logging Started")
logging.debug("Debug Info")
logging.info("Info")
logging.warning("Warning Info")
logging.error("Error Info")
logging.critical("Critical Info")
print("Logging End")

