import json
from file_operations import read_config, read_text_file, read_key_from_json, write_to_file


def initialize_alphabet(config):
    alphabet = config['alphabet']
    return alphabet, len(alphabet)


def create_key_sequence(key: str, text_length: int, alphabet: str) -> list:
    '''
    Сreate a digital key symbol by symbol
    :param key: Our key from file
    :param text_length: Our text length
    :param alphabet: Alphabet to use
    :return: Digital key
    '''
    key_sequence = []
    key_length = len(key)
    for i in range(text_length):
        key_char = key[i % key_length]
        key_num = alphabet.index(key_char) + 1
        key_sequence.append(key_num)
    return key_sequence


def encrypt(text: str, key_sequence: list, alphabet: str, alphabet_len: int) -> str:
    '''
    Encryption function using an improvement of the Caesar cipher
    :param text: Our text from file
    :param key_sequence: Digital key
    :param alphabet: Alphabet to use
    :param alphabet_len: Length of alphabet
    :return: Encrypted text
    '''
    encrypted_text = []
    for i, char in enumerate(text):
        if char in alphabet:
            char_num = alphabet.index(char) + 1
            key_num = key_sequence[i]
            encrypted_num = (char_num + key_num) % alphabet_len
            if encrypted_num == 0:
                encrypted_num = alphabet_len
            encrypted_char = alphabet[encrypted_num - 1]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)


def decrypt(encrypted_text: str, key_sequence: list, alphabet: str, alphabet_len: int) -> str:
    '''
    Decryption function using an improvement of the Caesar cipher
    :param encrypted_text: Encrypted text
    :param key_sequence: Digital key
    :param alphabet: Alphabet to use
    :param alphabet_len: Length of alphabet
    :return: Decrypted text
    '''
    decrypted_text = []
    for i, char in enumerate(encrypted_text):
        if char in alphabet:
            char_num = alphabet.index(char) + 1
            key_num = key_sequence[i]
            decrypted_num = (char_num - key_num) % alphabet_len
            if decrypted_num == 0:
                decrypted_num = alphabet_len
            decrypted_char = alphabet[decrypted_num - 1]
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)


def main() -> None:
    '''
    Main function to handle encryption and decryption
    :return: None
    '''
    config = read_config()
    alphabet, alphabet_len = initialize_alphabet(config)
    file_paths = config['file_paths']

    original_text = read_text_file(file_paths['text'])
    key = read_key_from_json(file_paths['key'])

    key = ''.join([char for char in key if char in alphabet])

    key_sequence = create_key_sequence(key, len(original_text), alphabet)
    encrypted_text = encrypt(original_text, key_sequence, alphabet, alphabet_len)
    write_to_file(file_paths['encrypted'], encrypted_text)

    decrypted_text = decrypt(encrypted_text, key_sequence, alphabet, alphabet_len)
    write_to_file(file_paths['decrypted'], decrypted_text)

    print("Encryption and decryption completed.")


if __name__ == "__main__":
    main()