from binascii import b2a_hex, a2b_hex
from random import choice
from string import digits

from Crypto.Cipher import AES
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms


class AesCrypto(object):
    def __init__(self, key=None, iv=None):
        self.key = key or self.get_random(16)
        self.iv = iv or self.get_random(16)
        self.mode = AES.MODE_CBC

    @staticmethod
    def pkcs7_padding(data):
        if not isinstance(data, bytes):
            data = data.encode()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        return padded_data

    def encrypt(self, plaintext):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plaintext = plaintext
        plaintext = self.pkcs7_padding(plaintext)
        ciphertext = cryptor.encrypt(plaintext)
        return b2a_hex(ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plaintext = cryptor.decrypt(a2b_hex(ciphertext))
        return bytes.decode(plaintext).rstrip().strip('\x01')

    def get_random(self, length):
        return ''.join(choice(digits + 'abcdef') for _ in range(length)).encode('utf-8').lower()


if __name__ == '__main__':
    aes = AesCrypto('ddfbccae-b4c4-11')
    encrypted = aes.encrypt('Congratulations1111! hello')
    print(encrypted)
    decrypted = aes.decrypt(encrypted)
    print(decrypted)
