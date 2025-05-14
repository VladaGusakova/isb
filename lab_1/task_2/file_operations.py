import json

def read_config(config_path='config.json'):
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at {config_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in config file {config_path}")

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at {file_path}")
    except UnicodeDecodeError:
        raise ValueError(f"Could not decode file {file_path} with utf-8 encoding")

def write_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except IOError:
        raise IOError(f"Could not write to file {file_path}")

def write_json(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except IOError:
        raise IOError(f"Could not write JSON to file {file_path}")