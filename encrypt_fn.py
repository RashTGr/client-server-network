# This script is to encrypt and decrypt a text file"

from binascii import Error

import cryptography
from cryptography.fernet import Fernet


def write_key():
    """Function to generate and save a key"""
    key = Fernet.generate_key()
    with open("static/crypto.key", "wb") as crypto_file:
        crypto_file.write(key)

def load_key():
    """The function to call the saved key from the file."""
    return open("static/crypto.key", "rb").read()

# Generate and save the key into a file
# write_key()
"""Uncomment to renew the saved key, and comment 
again before decrypt operation.
"""
# Initialize the saved key with the Fernet class
key = load_key()


def encrypt(filename, key):
    """Function to encrypt and write a file"""
    
    f = Fernet(key)
    
    # Read original data from the file
    with open(filename, "rb") as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    # Write encrypted data into the file
    with open(filename, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
            """Writing back the encrypted data into the file,
            this overwrites the original file.
            """
    print("Encryption completed!")


def decrypt(filename, key):
    """Function to decrypt and write the encrypted file."""
    
    f = Fernet(key)

    # Read encrypted data
    with open(filename, "rb") as encrypt_file:
        encrypted_data = encrypt_file.read() 
    try:
        # Decrypt data
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("The 'write_key' is likely left in active mode, " 
              "and a new key generated during decryption.")
    except Error:
        print("It is 'incorrect padding' error!")
    except (TypeError, UnboundLocalError):
        print("Error has to be fixed.")
    try:
        # Write decrypted/original data into the file
        with open(filename, "wb") as decrypt_file:
            decrypt_file.write(decrypted_data)
    except UnboundLocalError:
        print("Don't run the script. The file might already be corrupted.")
    else:
        print("The data is decrypted successfully!")


file = "static/demo_text.txt"

encrypt(file, key)
# decrypt(file, key)