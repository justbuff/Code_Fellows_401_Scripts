#!/usr/bin/env python3

import os
from sys import platform

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
  for root, dir, files in os.walk(prompt_directory):
      if prompt_file in files:
         result.append(os.path.join(root, prompt_file))
  print(result)
  os.system("ls " + str(prompt_file) + " | echo \"$(wc -l) files searched.\"")

def platform_search():
  if platform =="Linux":
    linux_search()
  elif platform == "win32":
    windows_search()
  
platform_search()
