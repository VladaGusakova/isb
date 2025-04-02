
alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_len = len(alphabet)

def create_key_sequence(key : str, text_length : int) -> list:
    '''
    Сreate a digital key symbol by symbol
    :param key: Our key from file
    :param text_length: Our text length
    :return: Digital key
    '''
    key_sequence = []
    key_length = len(key)
    for i in range(text_length):
        key_char = key[i % key_length]
        key_num = alphabet.index(key_char) + 1
        key_sequence.append(key_num)
    return key_sequence

def encrypt(text : str, key_sequence : list) -> str:
    '''
    Encryption function using an improvement of the Caesar cipher
    :param text: Our text from file
    :param key_sequence: Digital key
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

def main() -> None:
    '''
    We read the files and use functions to encrypt and create a digital key and then save the encrypted text
    :return: None
    '''
    with open('task_1/text.txt', 'r', encoding='utf-8') as file:
        original_text = file.read().upper()

    with open('task_1/key.txt', 'r', encoding='utf-8') as file:
        key = file.read().upper().replace('Ё', 'Е')

    key = ''.join([char for char in key if char in alphabet])
    key_sequence = create_key_sequence(key, len(original_text))
    encrypted_text = encrypt(original_text, key_sequence)

    with open('task_1/encrypted.txt', 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

    print("Done.")

if __name__ == "__main__":
    main()

