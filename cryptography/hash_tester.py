import hashlib

def main():
    return

def md5_digest(message):
    message_bytes = message.encode('utf-8')
    digest_bytes = hashlib.md5(message_bytes).digest()
    hex_digits = [f'{b:02x}' for b in digest_bytes]
    hex_string = ''.join(hex_digits)
    return hex_string

def sha256_digest(message):
    message_bytes = message.encode('utf-8')
    digest_bytes = hashlib.sha256(message_bytes).digest()
    hex_digits = [f'{b:02x}' for b in digest_bytes]
    hex_string = ''.join(hex_digits)
    return hex_string

def sha3_256_digest(message):
    message_bytes = message.encode('utf-8')
    digest_bytes = hashlib.sha3_256(message_bytes).digest()
    hex_digits = [f'{b:02x}' for b in digest_bytes]
    hex_string = ''.join(hex_digits)
    return hex_string

def blake2s_digest(message):
    message_bytes = message.encode('utf-8')
    digest_bytes = hashlib.blake2s(message_bytes).digest()
    hex_digits = [f'{b:02x}' for b in digest_bytes]
    hex_string = ''.join(hex_digits)
    return hex_string

def sha1_digest(message):
    message_bytes = message.encode('utf-8')
    digest_bytes = hashlib.sha1(message_bytes).digest()
    hex_digits = [f'{b:02x}' for b in digest_bytes]
    hex_string = ''.join(hex_digits)
    return hex_string

if __name__ == "__main__":
    main()