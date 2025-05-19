import json

def read_config(config_path: str = 'config.json') -> dict:
    '''
    Read and parse JSON configuration file.
    :param config_path: Path to the configuration file
    :return: Dictionary with configuration data
    '''
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Config file not found at {config_path}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file {config_path}") from e

def read_sequence(filename : str) -> str:
    '''
    Load a sequence from a file
    :param filename:
    :return:
    '''
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File {filename} not found.") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"File {filename} contains invalid JSON.") from e
    except Exception as e:
        raise RuntimeError(f"Unknown error loading file {filename}: {e}") from e

    if 'sequence' not in data:
        raise KeyError(f"The file {filename} is missing the 'sequence' key.")
    sequence = data['sequence']
    return sequence


def save_results(filename : str, results : dict) -> None:
    '''
    Saves test results to a JSON file.
    :param filename:
    :param results:
    :return:
    '''
    try:
        with open(filename, 'w') as f:
            json.dump(results, f, indent=4)
    except IOError as e:
        raise IOError(f"Error writing to file {filename}.") from e
    except TypeError as e:
        raise TypeError(f"The data to be saved is not serializable to JSON.") from e
    except Exception as e:
        raise RuntimeError(f"Unknown error loading file {filename}: {e}") from e
