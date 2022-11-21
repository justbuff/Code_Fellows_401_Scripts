#!/usr/bin/env python3

# to be combined with ops challenges 31 and 32

from sys import platform
import os, time, datetime, math
import hashlib

def malware_check():
    api_key = os.getenv('API_KEY_VIRUSTOTAL') 
    query = 'python3 virustotal-search.py -k ' + api_key + ' -m ' + hash
    os.system(query)
  
