
freq_russian = {
    ' ': 0.128675, 'О': 0.096456, 'И': 0.075312,
    'Е': 0.072292, 'А': 0.064841, 'Н': 0.061820,
    'Т': 0.061619, 'С': 0.051953, 'Р': 0.040677,
    'В': 0.039267, 'М': 0.029803, 'Л': 0.029400,
    'Д': 0.026983, 'Я': 0.026379, 'К': 0.025977,
    'П': 0.024768, 'З': 0.015908, 'Ы': 0.015707,
    'Ь': 0.015103, 'У': 0.013290, 'Ч': 0.011679,
    'Ж': 0.010673, 'Г': 0.009867, 'Х': 0.008659,
    'Ф': 0.007249, 'Й': 0.006847, 'Ю': 0.006847,
    'Б': 0.006645, 'Ц': 0.005034, 'Ш': 0.004229,
    'Щ': 0.003625, 'Э': 0.002416, 'Ъ': 0.000000
}

def calculate_frequencies(text : str) -> dict:
    '''
    Counts the frequency of each character in the text
    :param text: Our text from file
    :return:
    '''
    freq = {}
    total = len(text)
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char in freq:
        freq[char] = freq[char] / total
    return freq

def map_frequencies(encrypted_freq : dict, russian_freq : dict) -> dict:
    '''
    Matches characters from each dictionary
    :param encrypted_freq: Text dictionary
    :param russian_freq: Ru dictionary
    :return:
    '''
    encrypted_sorted = sorted(encrypted_freq.items(), key=lambda x: x[1], reverse=True)
    russian_sorted = sorted(russian_freq.items(), key=lambda x: x[1], reverse=True)

    substitution = {}
    for i in range(min(len(encrypted_sorted), len(russian_sorted))):
        encrypted_char, _ = encrypted_sorted[i]
        russian_char, _ = russian_sorted[i]
        substitution[encrypted_char] = russian_char
    return substitution

def manual_substitution(substitution : dict, encrypted_char : str, decrypted_char : str) -> dict:
    '''
    To manually change symbols
    :param substitution:
    :param encrypted_char: The symbol we want to replace
    :param decrypted_char: New symbol
    :return: New substitution
    '''
    if encrypted_char not in substitution:
        print("No")

    substitution[encrypted_char] = decrypted_char
    return substitution

def decrypt(text : str, substitution : dict) -> str:
    decrypted = []
    for char in text:
        if char in substitution:
            decrypted.append(substitution[char])
        else:
            decrypted.append(char)  # Оставляем символы, которых нет в алфавите
    return ''.join(decrypted)

def main() -> None:
    '''
    Apply all functions to replace and save text
    :return: None
    '''
    with open('./cod5.txt', 'r', encoding='utf-8') as file:
        encrypted_text = file.read()

    encrypted_freq = calculate_frequencies(encrypted_text)

    substitution_key = map_frequencies(encrypted_freq, freq_russian)
    substitution_key = manual_substitution(substitution_key, '1','Ч')
    substitution_key = manual_substitution(substitution_key, 'Y', 'Ъ')
    substitution_key = manual_substitution(substitution_key, 'F', 'З')
    substitution_key = manual_substitution(substitution_key, 'Т', 'Н')
    substitution_key = manual_substitution(substitution_key, 's', 'E')
    substitution_key = manual_substitution(substitution_key, 'Р', 'Х')
    substitution_key = manual_substitution(substitution_key, 'Х', 'У')
    substitution_key = manual_substitution(substitution_key, '9', 'Ы')
    substitution_key = manual_substitution(substitution_key, '\n', ' ')
    substitution_key = manual_substitution(substitution_key, 'И', 'П')
    substitution_key = manual_substitution(substitution_key, 'R', 'Б')
    substitution_key = manual_substitution(substitution_key, 'П', 'Ш')
    substitution_key = manual_substitution(substitution_key, 'ю', 'И')
    substitution_key = manual_substitution(substitution_key, 'Ж', 'Т')
    substitution_key = manual_substitution(substitution_key, '@', 'К')
    substitution_key = manual_substitution(substitution_key, 'i', 'M')
    substitution_key = manual_substitution(substitution_key, 'г', 'В')
    substitution_key = manual_substitution(substitution_key, 'i', 'M')
    substitution_key = manual_substitution(substitution_key, 'Ё', 'Ь')
    substitution_key = manual_substitution(substitution_key, 'у', 'Ф')
    substitution_key = manual_substitution(substitution_key, '<', 'Ж')
    substitution_key = manual_substitution(substitution_key, 'N', 'Ц')
    substitution_key = manual_substitution(substitution_key, 'К', 'Л')
    substitution_key = manual_substitution(substitution_key, 'Й', 'Д')
    substitution_key = manual_substitution(substitution_key, '7', 'Г')
    substitution_key = manual_substitution(substitution_key, 'Q', 'Я')
    substitution_key = manual_substitution(substitution_key, 'J', 'Ю')
    print(substitution_key)
    decrypted_text = decrypt(encrypted_text, substitution_key)

    with open('./decrypted.txt', 'w', encoding='utf-8') as file:
        file.write(decrypted_text)

    with open('./substitution_key.txt', 'w', encoding='utf-8') as file:
        for encrypted_char, decrypted_char in substitution_key.items():
            file.write(f"{encrypted_char} -> {decrypted_char}\n")
    print("Done.")

if __name__ == "__main__":
    main()
