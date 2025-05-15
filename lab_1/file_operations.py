import json
from typing import Dict, Any


def read_config(config_path: str = 'config.json', required_keys: list = None) -> Dict[str, Any]:
    '''
    Read and parse JSON configuration file.
    :param config_path: Path to the configuration file
    :return: Dictionary with configuration data
    '''
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)

            if required_keys:
                for key_path in required_keys:
                    keys = key_path.split('.')
                    current = config
                    for key in keys:
                        if key not in current:
                            raise ValueError(f"Missing required key: {key_path}")
                        current = current[key]

            return config

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Config file not found at {config_path}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file {config_path}") from e


def read_file(file_path: str) -> str:
    '''
    Read content from a text file.
    :param file_path: Path to the file to read
    :return: Content of the file as string
    '''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found at {file_path}") from e


def write_file(file_path: str, content: str) -> None:
    '''
    Write content to a text file.
    :param file_path: Path to the file to write
    :param content: Content to write
    :return: None
    '''
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"Could not write to file {file_path}") from e


def write_json(file_path: str, data: Dict[str, Any]) -> None:
    '''
    Write data to a JSON file.
    :param file_path: Path to the JSON file
    :param data: Dictionary to serialize to JSON
    :return:
    '''
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except IOError as e:
        raise IOError(f"Could not write JSON to file {file_path}") from e
    except TypeError as e:
        raise ValueError(f"Data contains non-serializable objects: {str(e)}") from e


def read_key_from_json(file_path: str, key_name: str = 'key') -> str:
    '''
    Read a specific key from JSON file.
    :param file_path: Path to the JSON file
    :param key_name: Name of the key to read
    :return: Value of the requested key
    '''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if key_name not in data:
                raise KeyError(f"Key '{key_name}' not found in {file_path}")
            return data[key_name].upper().replace('Ё', 'Е')

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Key file not found at {file_path}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in key file {file_path}") from e