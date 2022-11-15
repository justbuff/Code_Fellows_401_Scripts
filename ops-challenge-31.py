#!/usr/bin/env python3

import os
from sys import platform

def Linux_search():
  prompt_file = input("Please provide a target file path: ")
  prompt_directory = input("Please provide a target directory path: ")
  for root, dir, files in os.walk(prompt_directory):
      if prompt_file in files:
         result.append(os.path.join(root, prompt_file))
  return result
  print(result)

def Windows_search():
  $prompt_file = Read-Host -Prompt "Please provide a target fille path"
  $prompt_directory = Read-Host -Prompt "Please provide a target directory path"
  function search_directory {
    Get-ChildItem -Path $prompt_directory -Filter $prompt_file
  }
  Write-Output search_directory
  
