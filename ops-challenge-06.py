#!/usr/bin/python3


# still working on this one


from cryptography.fernet import Fernet

# infinite while loop
ans=True
while ans:
    # creates list
    print ("""
    1. Encrypt a file
    2. Decrypt a file
    3. Encrypt a message
    4. Decrpyt a message
    """)
    # asks for user input
    ans=raw_input("What would you like to do? ") 
    if ans=="1" or ans=="2":
    # creates file path variable 
      user_path = input(print("\n Please provide file path: "))
    elif ans=="3" or ans=="4":
    # creates message variable
      user_msg = input(print("\n Please provide a message: "))
    else:
      print("\n Please try again") 

# generates key and saves it to file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# loads key from file
def load_key():
    return open("key.key", "rb").read()

write_key()
    
key = load_key()
print("Key is " + str(key.decode('utf-8')))

message = user_msg.encode()
print("Plaintext is " + str(message.decode('utf-8')))

f = Fernet(key)

# Encrypt message
encrypted = f.encrypt(message)
# Print encrpyted message
print("Ciphertext is " + str(encrypted.decode('utf-8')))


decrypted = f.decrypt(encrypted)
print("Decrypted message is " + str(decrypted))
