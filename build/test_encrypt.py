"""This is unit test for text file Encryption 
and Decryption.
"""
    
import unittest
import os
from binascii import Error
import cryptography
from cryptography.fernet import Fernet

class TestEncryptDecrypt(unittest.TestCase):
    def setUp(self):
        self.key_path = "D:\zip file version\client-server-network-combatzone-2\static\crypto.key"
        self.file_path = "D:\zip file version\client-server-network-combatzone-2\static\serdes.dat"

        # Generate and save a key
        key = Fernet.generate_key()
        with open(self.key_path, "wb") as crypto_file:
            crypto_file.write(key)

    def test_encrypt_decrypt(self):
        # Load the key
        key = open(self.key_path, "rb").read()

        # Encrypt the file
        f = Fernet(key)
        with open(self.file_path, "rb") as file:
            data = file.read()
        encrypted_data = f.encrypt(data)
        with open(self.file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        # Decrypt the file
        f = Fernet(key)
        with open(self.file_path, "rb") as encrypt_file:
            encrypted_data = encrypt_file.read()
        decrypted_data = f.decrypt(encrypted_data)

        # Check that the decrypted data is the same as the original data
        with open(self.file_path, "rb") as file:
            original_data = file.read()
        self.assertEqual(decrypted_data, original_data)

   

if __name__ == "__main__":
    unittest.main()
