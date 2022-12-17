"""This is unit test for text file Encryption 
and Decryption.
"""

import unittest

import encrypt_fn as enc


class PicklingTest(unittest.TestCase):
    # configure input & output to pass to each test scenario
    def setUp(self):
        self.input_enc = file
        self.output_dec = file2
 
    # cleanup generated data during test cases
    def tearDown(self):
        self.input_enc = 0
        self.output_dec = 0
        
    # Unit test to test encryption and decryption script
    def test_encrypt(self):
        self.assertEqual(enc.encrypt(self.input_enc, test_key), 
                         enc.decrypt(self.output_dec, test_key))

    def test_encrypt_2(self):
        self.assertEqual(enc.encrypt(self.input_enc, test_key_2), 
                         enc.decrypt(self.output_dec, test_key_2))

    def test_encrypt_3(self):
        self.assertEqual(enc.encrypt(self.input_enc, test_key_3), 
                         enc.decrypt(self.output_dec, test_key_3))

    def test_encrypt_4(self):
        self.assertEqual(enc.encrypt(self.input_enc, test_key_4), 
                         enc.decrypt(self.output_dec, test_key_4))

  
# File path and keys to be used in different test cases
file = "../static/demo_text.txt"
file2 = "../static/demo_text.txt"
test_key = "LoqtVWM5aPJOTmKx8IA-MPKgkQpbPDob5BK9aVR5aE0="
test_key_2 = "1NaJ_rQ5Q5v_5Zi3q3UXjIEBoDL2lwdG_HwurlmUWV4="
test_key_3 = "78LEjqropNkHZI0eBC1HqXyWJwMHIzvHkVv4E0mlw4U="
test_key_4 = "E2e71siE2xdPP9Zj3XOPFj8mHNDmDzKcPYcfm1tQbXA="

print("\nUnit tests for text file Encryption is completed!\n")


if __name__ == "__main__":
    unittest.main()
