import os
import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.serialization import load_pem_private_key

class FileManager:
    def read_file(self, filepath : str) -> bytes:
        '''
        Reads binary data from a file.
        :param filepath: Path to the file
        :return: File content as bytes
        '''
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
            print(f"File read: {filepath} ({len(data)} bytes)")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        except Exception as e:
            raise IOError(f"Error reading file {filepath}: {e}")

    def write_file(self, data : bytes, filepath: str) -> None:
        '''
        Writes binary data to a file, creating directories if needed.
        :param data: Data bytes to write
        :param filepath: Path to the file
        :return: None
        '''
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'wb') as f:
                f.write(data)
            print(f"File written: {filepath} ({len(data)} bytes)")
        except Exception as e:
            raise IOError(f"Error writing file {filepath}: {e}")

    def save_private_key_pem(self, private_key, filepath : str) -> None:
        '''
        Saves private key in PEM format to a file.
        :param private_key: Private key object
        :param filepath: Path to the file
        :return: None
        '''
        try:
            pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
            self.write_file(pem, filepath)
            print(f"Private key saved: {filepath}")
        except Exception as e:
            raise IOError(f"Error saving private key: {e}")

    def save_public_key_pem(self, public_key, filepath : str) -> None:
        '''
        Saves public key in PEM format to a file.
        :param public_key: Public key object
        :param filepath: Path to the file
        :return: None
        '''
        try:
            pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            self.write_file(pem, filepath)
            print(f"Public key saved: {filepath}")
        except Exception as e:
            raise IOError(f"Error saving public key: {e}")

    def load_private_key_pem(self, filepath : str):
        '''
        Loads private key from a PEM file.
        :param filepath: Path to the PEM file
        :return: Private key object
        '''
        try:
            data = self.read_file(filepath)
            private_key = load_pem_private_key(data, password=None)
            return private_key
        except Exception as e:
            raise IOError(f"Error loading private key: {e}")

    def load_public_key_pem(self, filepath : str):
        '''
        Loads RSA public key from a PEM file.
        :param filepath: Path to the PEM file
        :return: RSA public key object
        '''
        try:
            data = self.read_file(filepath)
            public_key = load_pem_public_key(data)
            return public_key
        except Exception as e:
            raise IOError(f"Error loading public key: {e}")

    def load_json_config(self, filepath : str) -> dict:
        '''
        Loads JSON configuration from a file.
        :param filepath: Path to the JSON config file
        :return: Configuration dictionary
        '''
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print(f"Configuration loaded: {filepath}")
            return config
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: {filepath}")
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON format error in file {filepath}: {e}")
        except Exception as e:
            raise IOError(f"Error loading config {filepath}: {e}")
