#!/usr/bin/env python3

from zipfile import ZipFile

zip_file = input("Please enter the absolute path of the zip file you want to brute force:")
password_list = "./usr/share/wordlists/rockyou.txt"
obj = zipfile.ZipFile(zip_file)

def crack_password(password_list, obj):
    idx = 0
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idx)
                    print("Password is", word.decode())
                    return True
                except:
                    continue
    return False
  
  if crack_password(password_list, obj) == False:
    print("Password not found in this file")
    
