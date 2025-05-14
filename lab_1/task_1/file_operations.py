import json

def read_config(config_path='config.json'):
    with open(config_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().upper()

def read_key_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data['key'].upper().replace('Ё', 'Е')

def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

