"""This is unit test for text file Encryption 
and Decryption.
"""
from binascii import Error
import cryptography
from cryptography.fernet import Fernet
import unittest

class TestEncryption(unittest.TestCase):
    def setUp(self):
        # Generate and save the key
        write_key()
        # Load the key
        self.key = load_key()

    def test_encrypt(self):
        # Test that the encrypt function returns the expected output
        encrypt("D:\my project code v1\client-server-network-master\static\crypto.key.key", self.key)
        with open("D:\my project code v1\client-server-network-master\static\crypto.key.key", "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
        # Check that the encrypted data is different from the original data
        with open("test.txt", "rb") as original_file:
            original_data = original_file.read()
        self.assertNotEqual(encrypted_data, original_data)

    def test_decrypt(self):
        # Test that the decrypt function returns the expected output
        encrypt("test.txt", self.key)
        decrypt("test.txt", self.key)
        with open("test.txt", "rb") as decrypted_file:
            decrypted_data = decrypted_file.read()
        # Check that the decrypted data is equal to the original data
        with open("test.txt", "rb") as original_file:
            original_data = original_file.read()
        self.assertEqual(decrypted_data, original_data)
file = "D:\my project code v1\client-server-network-master\static\crypto.key.key"

if __name__ == '__main__':
     encrypt(file, key)
if __name__ == '__main__':
    unittest.main()

