from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

class CAST5Manager:
    def __init__(self, key_length):
        '''
        Initializes CAST5Manager with specified key length.
        :param key_length: Length key in bits
        :return: None
        '''
        self.key_length = key_length // 8
        self.block_size = 8

    def generate_key(self) -> bytes:
        """
        Generates a key with the given length
        :return: Key
        """
        return os.urandom(self.key_length)

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        """
        Encrypting a text file with a symmetric algorithm
        :param key: Symmetric key
        :param data: Text to encrypt
        :return: Byte string
        """
        iv = os.urandom(8)
        cipher = Cipher(algorithms.CAST5(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(64).padder()
        padded_data = padder.update(data) + padder.finalize()
        encrypted = encryptor.update(padded_data) + encryptor.finalize()
        return iv + encrypted

    def decrypt(self, encrypted_data: bytes, key: bytes) -> str:
        '''
        Decrypts data encrypted with a symmetric algorithm
        :param encrypted_data: Encrypted data with IV prepended
        :param key: Symmetric key
        :return: Decrypted text
        '''
        iv = encrypted_data[:8]
        ciphertext = encrypted_data[8:]
        cipher = Cipher(algorithms.CAST5(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(64).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        return data
