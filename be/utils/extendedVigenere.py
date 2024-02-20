def extended_vigenere_encrypt(content: bytes, key: str):
    for i in range(len(content)):
        # if using bytes, it couldn't be added with int as byte range is 0-255 so use XOR
        content = content[:i] + bytes([content[i] ^ ord(key[i % len(key)])]) + content[i+1:]

    return content

def extended_vigenere_decrypt(content: bytes, key: str):
    for i in range(len(content)):
        # if using bytes, it couldn't be added with int as byte range is 0-255 so use XOR
        content = content[:i] + bytes([content[i] ^ ord(key[i % len(key)])]) + content[i+1:]

    return content