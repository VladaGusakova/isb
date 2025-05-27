import sys
from pars import create_parser
from hybrid_crypto import HybridCrypto
from file_manager import FileManager

def main() -> None:
    '''
    Using all functions
    :return: None
    '''
    try:
        file_manager = FileManager()
        config = file_manager.load_json_config('settings.json')
        parser = create_parser()
        args = parser.parse_args()

        if args.cast_key_length < 40 or args.cast_key_length > 128 or args.cast_key_length % 8 != 0:
            raise ValueError("Incorrect key length.")
        config['cast_key_length'] = args.cast_key_length

        crypto = HybridCrypto(config, file_manager)
        if args.generation:
            crypto.generate_keys()
        elif args.encryption:
            crypto.encrypt_file()
        elif args.decryption:
            crypto.decrypt_file()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
