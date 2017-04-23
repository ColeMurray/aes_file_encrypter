import os
import unittest

from Crypto import Random

from aes_encrypter import PlainTextEncrypter


class TestPlainTextEncrypter(unittest.TestCase):
    def test_encrypt_decrypt_should_match(self):
        plain_text = "Hello there"
        key = Random.get_random_bytes(32)

        encrypter = PlainTextEncrypter(key)
        cipher_text = encrypter.encrypt(plain_text)
        decrypted_text = encrypter.decrypt(cipher_text)

        self.assertEqual(plain_text, decrypted_text)

    def test_encrypt_decrypt_from_file_should_be_equal(self):
        key = Random.get_random_bytes(32)

        plain_text = "Hello there"
        input_path = os.getcwd() + 'crypto_input'
        enc_outpath = os.getcwd() + 'encrypted_input'

        decrypt_outpath = os.getcwd() + 'crypto_output'

        with open(input_path, 'w') as f:
            f.write(plain_text)

        encrypter = PlainTextEncrypter(key)
        encrypter.encrypt_file(input_path, enc_outpath)

        encrypter.decrypt_file(in_filepath=enc_outpath, out_filepath=decrypt_outpath)

        with open(decrypt_outpath, 'r') as f:
            output = f.read()

        self.assertEqual(plain_text, output)

        os.remove(input_path)
        os.remove(enc_outpath)
        os.remove(decrypt_outpath)


if __name__ == '__main__':
    unittest.main()
