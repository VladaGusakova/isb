from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

class RSAManager:
    def __init__(self, key_size : int) -> None:
        '''
        Initializes RSAManager with specified RSA key size.
        :param key_size: Key size in bits
        :return: None
        '''
        self.key_size = key_size
        self.padding_scheme = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )

    def generate_key_pair(self) -> tuple:
        '''
        Generates an RSA private and public key pair.
        :return: Tuple (private_key, public_key)
        '''
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size
        )
        return private_key, private_key.public_key()

    def encrypt(self, data: bytes, public_key) -> bytes:
        '''
        Encrypts data using RSA public key with OAEP padding.
        :param data: Data bytes to encrypt
        :param public_key: RSA public key object
        :return: Encrypted data bytes
        '''
        try:
            return public_key.encrypt(data, self.padding_scheme)
        except Exception as e:
            raise Exception(f"RSA encryption failed: {e}")

    def decrypt(self, encrypted_data: bytes, private_key) -> bytes:
        '''
        Decrypts data using RSA private key with OAEP padding.
        :param encrypted_data: Encrypted data bytes
        :param private_key: RSA private key object
        :return: Decrypted data bytes
        '''
        try:
            return private_key.decrypt(encrypted_data, self.padding_scheme)
        except Exception as e:
            raise Exception(f"RSA decryption failed: {e}")
