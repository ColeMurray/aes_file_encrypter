import base64

import Crypto.Random
from Crypto.Cipher import AES


class PlainTextEncrypter(object):
    CHUNK_SIZE = AES.block_size

    def __init__(self, key):
        self.key = key

    def encrypt_file(self, infile_path, outfile_path):
        with open(infile_path, 'r') as f:
            lines = f.read()
            with open(outfile_path, 'wb+') as out:

                    out.write(self.encrypt(lines))

    def decrypt_file(self, in_filepath, out_filepath):
        with open(in_filepath, 'rb') as f:
            lines = f.read()
            with open(out_filepath, 'w+') as out:
                    out.write(self.decrypt(lines))

    def encrypt(self, text):
        iv = Crypto.Random.get_random_bytes(16)
        raw = self._pad(text)
        aes = AES.new(self.key, AES.MODE_CBC, iv)
        cipher_text = aes.encrypt(raw)
        return base64.b64encode(iv + cipher_text)

    def decrypt(self, ciphertext):
        enc = base64.b64decode(ciphertext)
        iv = enc[:self.CHUNK_SIZE]
        aes = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(aes.decrypt(enc[self.CHUNK_SIZE:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.CHUNK_SIZE - len(s) % self.CHUNK_SIZE) * chr(self.CHUNK_SIZE - len(s) % self.CHUNK_SIZE)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]



def main():
    import argparse

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--file', dest='filepath', action='store', help='File to be encrypted')
    parser.add_argument('--dest', dest='dest_path', action='store', help='Destination of output')
    parser.add_argument('--encrypt', dest='encrypt', action='store_true', default=False, help='Flag for encrypting')
    parser.add_argument('--decrypt', dest='decrypt', action='store_true', default=False, help='Flag for decrypt')
    parser.add_argument('--b64key', dest='key', action='store', help='Base64 encoded Key for encrypt, decrypt')

    args = parser.parse_args()

    if args.filepath is None:
        raise IOError("Missing input filepath")

    if args.dest_path is None:
        raise IOError("Missing output filepath")

    if args.encrypt:
        key = args.key
        if key is None:
            key = base64.b64encode(Crypto.Random.get_random_bytes(32))
            print(key)
            print('Key used: {}'.format(key))

        encrypter = PlainTextEncrypter(base64.b64decode(key))
        encrypter.encrypt_file(args.filepath, args.dest_path)

    if args.decrypt:
        if args.key is None:
            raise IOError('Missing key to decrypt')

        encrypter = PlainTextEncrypter(base64.b64decode(args.key))
        encrypter.decrypt_file(args.filepath, args.dest_path)

if __name__ == '__main__':
   main()
