#!/usr/bin/env python3

# WIP

# Automated Brute Force Wordlist Attack Tool Part 1 of 3

# Mode 1: Offensive; Dictionary Iterator

# Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
# Add a delay between words.
# Print to the screen the value of the variable.

# Mode 2: Defensive; Password Recognized

# Accepts a user input string.
# Accepts a user input word list file path.
# Search the word list for the user input string.
# Print to the screen whether the string appeared in the word list.


import time
import getpass

def iterator():
  path = input("Please enter your dictionary filepath:\n")
  file = open(path)
  line = file.readline()
  print(line)
  
  while line:
    line = line.rstrip()
    word = line
    print(word)
    time.sleep(1)
    line = file.readline()
  file.close()
  
def password_check():
  pwd = getpass.getpass("Please enter a password:\n")
  path = input("Please enter the wordlist file path:\n")
  if string in path:
    print(str(pwd) + " is inside the wordlist")
  else:
    print(str(pwd) + " is not inside the wordlist")
  
iterator()
password_check()
  

