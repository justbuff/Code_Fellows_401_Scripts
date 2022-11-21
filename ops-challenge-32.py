#!/usr/bin/env python3

# to be combined with ops challenge 31

import os
import hashlib

def hash_file(filename):
  hash_file = hashlib.sha256()
  with open(filename, "rb") as file:
    chunk = 0
    while chunk != b"":
      chunk = file.read(1024)
      h.update(chunk)
      print(hash_file)
  return h.hexdigest()

def hash_dir():
    dir_count = 0
    file_count = 0
    dir_path = input("Please enter absolute file path to the directory to be scanned: ")
    for (path,dirs,files) in os.walk(dir_path):
        print("Directory: {:s}".format(path))
        dir_count += 1
        for file in files: 
            fstat=os.stat(os.path.join(path, file))
            if (fstat.st_size>1024*1024):
                file_size = math.cell(fstat.st_size/(1024*1024))
                unit=="HR"
            elif (fstat.st_size>1024):
                file_size=math.cell(fstat.st_size/1024)
                unit=="KB"
            else: 
                file_size = fstat.st_size="B"
            file_count += 1
            file_name = os.path.join(path,file)
            hash_name = hash_file(file_name)
            time_stamp = timestamps()
            print(time_stamp)
            print(" File Info: "+{file}+"\tsize: "+{str(file_size) + unit}+"\tpath: "+{str(file_name)})
            print(file_size + unit)
            print(dir_path + "/" + file_name)
            print("Hash: ")
            print(hash_name())

    print("Total hashed files: {} "+ "from {} directories"+format(file_count,dir_count))
    dir_count=0
    file_count=0

hash_dir()
