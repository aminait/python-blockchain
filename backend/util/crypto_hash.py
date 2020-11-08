import hashlib
import json

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    print(f'stringified_args: {stringified_args}')
    joined_data = ''.join(stringified_args)
    print(f'joined_data: {joined_data}')
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one', 1, [2], 'two'): {crypto_hash('one', 1, [2], 'two')}")

if __name__ == '__main__':
    main()