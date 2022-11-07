import unittest

import string

from Cipher import cipher

import random

from pathlib import Path

characters = [string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits]

class TestFunction(unittest.TestCase):

    def test_text_encryption(self):
        test_message = "Test@567"
        self.assertEqual(cipher(test_message, 4, characters), "Xiwx^9ab", " The message was not encrypted ")


    def test_text_decryption(self):
        testx_message = "Xiwx^9ab"
        self.assertEqual(cipher(testx_message, -4, characters), "Test@567", " The message was not decrypted " )


    # File Testing


    def test_file_encrypt(self):
        plaintxt_file = open("plaintext.txt", "r+")
        holder = plaintxt_file.read()
        decrypted_file = open("Decryptedfile.txt", "r+")
        holder2 = decrypted_file.read()
        self.assertEqual(holder,holder2, " The files are not the same ")



if __name__ == '__main__':
    unittest.main()