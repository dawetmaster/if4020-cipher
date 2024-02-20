def affine_encrypt(plaintext: str, m: int, b: int):
    # make plaintext lowercase
    plaintext = plaintext.lower()

    # remove non-alphabet characters
    plaintext = "".join(filter(str.isalpha, plaintext))

    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr((m * (ord(plaintext[i]) - ord('a')) + b) % 26 + ord('a'))

        chr(m * (ord('k') - ord('a')))

    return ciphertext

def affine_decrypt(ciphertext: str, m: int, b: int):
    # make ciphertext lowercase
    ciphertext = ciphertext.lower()

    # remove non-alphabet characters
    ciphertext = "".join(filter(str.isalpha, ciphertext))

    # find modular multiplicative inverse of m
    i = 0
    while (m * i) % 26 != 1:
        i += 1
        if i > 26:
            return {
                "status": "error",
                "message": "Invalid m"
            }
    m = i

    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr((m * (ord(ciphertext[i]) - ord('a') - b)) % 26 + ord('a'))

    return plaintext