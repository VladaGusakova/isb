import math
from scipy.special import gammainc

def bit_frequency_test(bits : str) -> float:
    '''
    Check the randomness of the sequence using a frequency bit test.
    :param bits: sequence
    :return: p_value
    '''
    n = len(bits)
    s_n = abs(sum(1 if b == '1' else -1 for b in bits)) / math.sqrt(n)
    p_value = math.erfc(s_n / math.sqrt(2))
    return p_value


def identical_consecutive_bits_test(bits : str) -> float:
    '''
    The test consists of finding all sequences of identical bits.
    :param bits: sequence
    :return: p_value
    '''
    n = len(bits)
    zeta = bits.count('1') / n
    if abs(zeta - 0.5) >= 2 / math.sqrt(n):
        return 0.0
    v_n = sum(1 if bits[i] != bits[i+1] else 0 for i in range(n-1))
    p_value = math.erfc(abs(v_n - 2*n*zeta*(1-zeta)) / (2*math.sqrt(2*n)*zeta*(1-zeta)))
    return p_value


def longest_seq_ones_in_block_test(bits : str, pi : list, block_size=8) -> float:
    '''
    Test for the longest sequence of ones in a block.
    :param bits: sequence
    :param block_size: block size(8)
    :param pi: pi values
    :return: p_value
    '''
    if len(bits) != 128:
        raise ValueError("Incorrect number of bits")

    n = len(bits)
    num_blocks = n // block_size
    blocks = [bits[i*block_size:(i+1)*block_size] for i in range(num_blocks)]
    v = [0, 0, 0, 0]
    for block in blocks:
        max_seq = 0
        current_seq = 0
        for bit in block:
            if bit == '1':
                current_seq += 1
                max_seq = max(max_seq, current_seq)
            else:
                current_seq = 0
        match max_seq:
            case x if x <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case _:
                v[3] += 1
    chi2 = sum((v[i] - num_blocks * pi[i])**2 / (num_blocks * pi[i]) for i in range(4))
    p_value = gammainc(3 / 2, chi2 / 2)
    return p_value
