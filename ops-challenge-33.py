#!/usr/bin/env python3

# to be combined with ops challenges 31 and 32

from sys import platform
import os, time, datetime, math
import hashlib

def linux_search():
  prompt_file = input("Please provide a target file path: ")
  prompt_directory = input("Please provide a target directory path: ")
  for root, dir, files in os.walk(prompt_directory):
      if prompt_file in files:
         result.append(os.path.join(root, prompt_file))
  print(result)
  os.system("ls " + str(prompt_file) + " | echo \"$(wc -l) files searched.\"")

def windows_search():
  prompt_file = input("Please provide a target file path: ")
  prompt_directory = input("Please provide a target directory path: ")
  searched = os.popen("dir /a:-d /s /b " + str(dir) + " | find /c \":\\\"").read()
  print("Files searched: " + searched)
  found = os.popen("dir /b/s " + str(dir) + "\\" + str(prompt_file) + " | find /c \":\\\"").read()
  print("Files found: " + found)
  os.system("dir /b/s " + str(prompt_directory) + "\\" + str(prompt_file))

def platform_search():
  if platform == "linux" or platform == "linux2":
    linux_search()
  elif platform == "win32":
    windows_search()
  
platform_search()

def malware_check():
    api_key = os.getenv('API_KEY_VIRUSTOTAL') 
    query = 'python3 virustotal-search.py -k ' + api_key + ' -m ' + hash
    os.system(query)

def hash_file(filename):
  hash_file = hashlib.sha256()
  with open(filename, "rb") as file:
    chunk = 0
    while chunk != b"":
      chunk = file.read(1024)
      h.update(chunk)
      print(hash_file)
  return h.hexdigest()

def time_stamp():
    rn=datetime.datetime.now()
    return rn.strftime('%m-%d-%Y %H:%M:%S')
  
def hash_dir():
    dir_count = 0
    file_count = 0
    dir_path = input("Please enter absolute file path to the directory to be scanned: ")
    for (path,dirs,files) in os.walk(dir_path):
        print("Directory: {:s}".format(path))
        dir_count += 1
        for file in files: 
            fstat=os.stat(os.path.join(path, file))
            if (fstat.st_size > 1024 * 1024):
                file_size = math.ceil(fstat.st_size / (1024 * 1024))
                unit = "MB"
            elif (fstat.st_size>1024):
                file_size=math.ceil(fstat.st_size / 1024)
                unit = "KB"
            else: 
                file_size = fstat.st_size
                unit = "B"
            file_count += 1
            file_name = os.path.join(path,file)
            hash_name = hash_file(file_name)
            time_stamp = timestamp()
            print(time_stamp)
            print(" File Info: "+{file}+"\tsize: "+{str(file_size) + unit} + "\tpath: "+{str(file_name)})

    print("Total hashed files: {} "+ "from {} directories"+format(file_count,dir_count))
    dir_count=0
    file_count=0

hash_dir()
malware_check()


  
