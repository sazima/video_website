from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class EncryptUtils:

    @classmethod
    def encrypt(cls, key: str, msg: str):
        key_bytes = key.encode()
        msg_bytes = msg.encode()
        iv = get_random_bytes(16)
        cipher = AES.new(key_bytes, AES.MODE_CFB, iv)
        ciphertext = cipher.encrypt(msg_bytes)
        return iv.hex() + '$' + ciphertext.hex()

    @classmethod
    def decrypt(cls, key: str, text: str):
        iv, ciphertext = text.split('$')
        key_bytes = key.encode()
        cipher = AES.new(key_bytes, AES.MODE_CFB, bytearray.fromhex(iv))
        msg = cipher.decrypt(bytearray.fromhex(ciphertext))
        return msg.decode("utf-8")


if __name__ == '__main__':
    key = '1234567812345678'
    a = 'hello world'
    res = EncryptUtils.encrypt(key, a)
    print(res)
    print(EncryptUtils.decrypt(key, res))
    # print(res.hex())
    # print(EncryptUtils.decrypt(key, res))
