def autokey_vigenere_encrypt(plaintext: str, key: str) -> str:
    # Make plaintext and key lowercase
    plaintext = plaintext.lower()
    key = key.lower()

    # Remove non-alphabet characters
    plaintext = "".join(filter(str.isalpha, plaintext))
    key = "".join(filter(str.isalpha, key))

    # Join the key and plaintext together
    key = key + plaintext

    ciphertext = ""
    for i in range(0, len(plaintext)):
        ciphertext += chr((ord(plaintext[i]) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
    
    return ciphertext

def autokey_vigenere_decrypt(ciphertext: str, key: str) -> str:
    # Make ciphertext and key lowercase
    ciphertext = ciphertext.lower()
    key = key.lower()

    # Remove non-alphabetic characters
    ciphertext = "".join(filter(str.isalpha, ciphertext))
    key = "".join(filter(str.isalpha, key))

    # Here it goes...
    i = 0
    plaintext = ""
    while (i < len(ciphertext)):
        if i < len(key):
            plaintext += chr((ord(ciphertext[i]) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            plaintext += chr((ord(ciphertext[i]) - ord(plaintext[i-len(key)]) + 26) % 26 + ord('a'))
        i += 1

    return plaintext
