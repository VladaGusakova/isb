from tests import bit_frequency_test, identical_consecutive_bits_test, longest_seq_ones_in_block_test
from file_operations import read_sequence, save_results, read_config

def analyze_sequence(bits : str, pi : list) -> dict:
    '''
    Just to organize the information
    :param bits: sequence
    :return: Results
    '''
    return {
        'sequence': bits,
        'bit_frequency_test': bit_frequency_test(bits),
        'identical_consecutive_bits_test': identical_consecutive_bits_test(bits),
        'longest_seq_ones_in_block_test': longest_seq_ones_in_block_test(bits, pi)
    }

def main() -> None:
    '''
    Using the functionality
    :return: None
    '''
    config = read_config()

    cpp_bits = read_sequence(config['cpp_seq_path'])
    java_bits = read_sequence(config['java_seq_path'])

    results = {
        'cpp_sequence': analyze_sequence(cpp_bits, config['pi']),
        'java_sequence': analyze_sequence(java_bits, config['pi'])
    }

    save_results(config['results_path'], results)
    print(f"Results are saved in {config['results_path']}")

if __name__ == '__main__':
    main()
