from lab_1.file_operations import read_config, read_file, write_file, write_json


def calculate_frequencies(text: str) -> dict:
    '''
    Calculate the frequency of each character in the given text.
    :param text: The input text to analyze
    :return: A dictionary where keys are characters and values are their frequencies
    '''

    freq = {}
    total = len(text)
    if total == 0:
        return freq

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char in freq:
        freq[char] = freq[char] / total
    return freq


def map_frequencies(encrypted_freq: dict, russian_freq: dict) -> dict:
    '''
    Create a substitution dictionary by mapping character frequencies.
    :param encrypted_freq: Frequency dictionary of encrypted text
    :param russian_freq: Frequency dictionary of Russian language
    :return: A substitution dictionary mapping encrypted chars to Russian chars
    '''

    encrypted_sorted = sorted(encrypted_freq.items(), key=lambda x: x[1], reverse=True)
    russian_sorted = sorted(russian_freq.items(), key=lambda x: x[1], reverse=True)

    substitution = {}
    for i in range(min(len(encrypted_sorted), len(russian_sorted))):
        encrypted_char, _ = encrypted_sorted[i]
        russian_char, _ = russian_sorted[i]
        substitution[encrypted_char] = russian_char
    return substitution


def apply_manual_substitutions(substitution: dict,manual_subs: dict) -> dict:
    '''
    Apply manual substitutions to the substitution dictionary with validation.
    :param substitution: Current substitution dictionary
    :param manual_subs: Dictionary of substitutions
    :return: Updated substitution dictionary
    '''
    for encrypted_char, decrypted_char in manual_subs.items():
        if encrypted_char in substitution:
            substitution[encrypted_char] = decrypted_char
        else:
            print(f"Warning: Character '{encrypted_char}' not found in substitution dictionary. Skipping.")

    return substitution


def decrypt(text: str, substitution: dict) -> str:
    '''
    Decrypt text using the substitution dictionary.
    :param text: Encrypted text to decrypt
    :param substitution: Substitution dictionary
    :return: Decrypted text
    '''

    decrypted = []
    for char in text:
        if char in substitution:
            decrypted.append(substitution[char])
        else:
            decrypted.append(char)
    return ''.join(decrypted)


def main() -> None:
    '''
    Main function that executes the decryption workflow
    :return:
    '''
    try:
        config = read_config(required_keys=['freq_russian', 'file_paths', 'file_paths.manual_substitutions'])
        freq_russian = config['freq_russian']
        file_paths = config['file_paths']
        manual_subs = config['file_paths']['manual_substitutions']

        encrypted_text = read_file(file_paths['encrypted'])

        encrypted_freq = calculate_frequencies(encrypted_text)
        substitution_key = map_frequencies(encrypted_freq, freq_russian)
        substitution_key = apply_manual_substitutions(substitution_key, manual_subs)

        decrypted_text = decrypt(encrypted_text, substitution_key)

        write_file(file_paths['decrypted'], decrypted_text)
        write_json(file_paths['substitution_key'], substitution_key)

        print(f"Decryption completed successfully. Substitution key saved to {file_paths['substitution_key']}")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise


if __name__ == "__main__":
    main()