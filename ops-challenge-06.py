#!/usr/bin/python3


# still working on this script


from cryptography.fernet import Fernet

# key generation

# generates key and saves it to file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# loads key from file
def load_key():
    return open("key.key", "rb").read()

write_key()
    
f = Fernet(key)

key = load_key()
print("Key is " + str(key.decode('utf-8')))

# functions

def encrypt_file():
    file = user_path.encode()
    encrypted_file = f.encrypt(file)
    print("File is " + str(encrypted_file.decode('utf-8')))
  
def decrypt_file():
    file = user_path.encode()
    decrypted_file = f.decrypt(file)
    print("File is " + str(decrypted_file.decode('utf-8')))
    
def encrypt_message():
    message = user_msg.encode()
    encrypted_message = f.encrypt(message)
    print("Ciphertext is " + str(encrypted_message.decode('utf-8')))
    
def decrypt_message():
    message = user_msg.encode()
    decrypted_message = f.decrypt(message)
    print("Plaintext is " + str(decrypted_message.decode('utf-8')))


# infinite while loop
ans=True
while ans:
    # creates list
    print ("""
    1. Encrypt a file
    2. Decrypt a file
    3. Encrypt a message
    4. Decrypt a message
    """)
    # asks for user input
    ans=raw_input("What would you like to do? ") 
    if ans=="1":
        user_path = input(print("\n Please provide file path: "))
        encrypt_file()
        
    elif ans=="2":
        user_path = input(print("\n Please provide file path: "))
        decrypt_file()
        
    elif ans=="3":
        user_msg = input(print("\n Please provide a message: "))
        encrypt_message()
    
    elif ans=="4":
        user_msg = input(print("\n Please provide a message: "))
        decrypt_message()
        
    else:
      print("\n Please try again") 
