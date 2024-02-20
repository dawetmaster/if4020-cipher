def vigenere_encrypt(plaintext: str, key: str) -> str:
    # make plaintext and key lowercase
    plaintext = plaintext.lower()
    key = key.lower()

    # remove non-alphabet characters
    plaintext = "".join(filter(str.isalpha, plaintext))

    # repeat key
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]

    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr((ord(plaintext[i]) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))

    return ciphertext

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    # make ciphertext and key lowercase
    ciphertext = ciphertext.lower()
    key = key.lower()

    # remove non-alphabet characters
    plaintext = "".join(filter(str.isalpha, ciphertext))

    # repeat key
    key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)]

    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr((ord(ciphertext[i]) - ord(key[i]) + 26) % 26 + ord('a'))

    return plaintext