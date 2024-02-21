import numpy as np
import math

def __numeralize_alphabet(alphabet: str) -> int:
    if len(alphabet) == 1 and isinstance(alphabet, str):
        return ord(alphabet.lower()[0]) - ord('a')
    else:
        raise ValueError("Alphabet must be the string with length 1")

def __alphabetize_numerals(value: int) -> str:
    if value >= 0 and value <= 25 and isinstance(value, int):
        return chr(ord('a') + value)
    else:
        raise ValueError("Value must be an integer in range of 0 to 25")
    
def __make_matrix(pseudomatrix: list) -> np.array:
    mat = np.array(pseudomatrix)
    upper_bound = math.ceil(math.sqrt(len(pseudomatrix)))
    # Resize to nxn matrix
    mat = np.resize(mat, (upper_bound, upper_bound))
    return mat

def __determinant(pseudomatrix: list) -> float:
    # Ensure that mat is a list of list of integers (a square matrix)
    # By default, repeat the key (partially) to make a higher nxn matrix
    mat = __make_matrix(pseudomatrix)
    det = np.linalg.det(mat)
    return det

def __key_inv_matrix(matrix: np.array) -> np.array:
    matrix = np.matrix(matrix)
    # Multiplier: modular inverse of determinant
    determinant = round(np.linalg.det(matrix))
    multiplier = pow(determinant % 26, -1, 26)
    adjoint = (np.linalg.inv(matrix) * determinant).round()
    return (multiplier * adjoint) % 26

def __check_matrix_has_inverse(pseudomatrix: list) -> bool:
    # Check using numpy as the determinant is a float
    det_not_zero = not np.isclose(__determinant(pseudomatrix), 0.0, rtol=1e-09, atol=1e-09)
    det_relatively_prime = math.gcd(round(__determinant(pseudomatrix)) % 26, 26) == 1
    return det_not_zero and det_relatively_prime

def hill_encrypt(plaintext: str, key: str) -> str:
    # make plaintext and key lowercase
    plaintext = plaintext.lower()
    key = key.lower()

    # remove non-alphabet characters
    plaintext = "".join(filter(str.isalpha, plaintext))
    key = "".join(filter(str.isalpha, key)) # ensure the key consists of alphabetic characters

    # Make a numeral list out of the strings *fire emoji*
    key_pseudomatrix = [__numeralize_alphabet(char) for char in key]
    numeral_plaintext = [__numeralize_alphabet(char) for char in plaintext]

    # If key_psuedomatrix has a determinant of zero, raise an exception.
    if not __check_matrix_has_inverse(key_pseudomatrix):
        raise ValueError("Key cannot be applied to encrypt the plaintext")
    
    # Get padding size
    padding_size = math.ceil(math.sqrt(len(key_pseudomatrix)))

    # Add padding 'z' to the numeral plaintext (it has value of 25)
    while (len(numeral_plaintext) % padding_size != 0):
        numeral_plaintext.append(25)
    
    # Encrypt the numeral plaintext
    key_matrix = __make_matrix(key_pseudomatrix)
    numeral_ciphertext = []
    for i in range(0, len(numeral_plaintext), padding_size):
        current_part = np.array(numeral_plaintext[i:i+padding_size]) \
                        .reshape((padding_size, 1))
        cipher_part = np.matmul(key_matrix, current_part) % 26
        cipher_part = cipher_part.reshape(padding_size)
        numeral_ciphertext += cipher_part.tolist()
    
    ciphertext = "".join([__alphabetize_numerals(x) for x in numeral_ciphertext])
    return ciphertext

def hill_decrypt(ciphertext: str, key: str) -> str:
    # make ciphertext and key lowercase
    ciphertext = ciphertext.lower()
    key = key.lower()

    # remove non-alphabet characters
    ciphertext = "".join(filter(str.isalpha, ciphertext))
    key = "".join(filter(str.isalpha, key)) # ensure the key consists of alphabetic characters

    # Make a numeral list out of the strings *fire emoji*
    key_pseudomatrix = [__numeralize_alphabet(char) for char in key]
    numeral_ciphertext = [__numeralize_alphabet(char) for char in ciphertext]

    # If key_psuedomatrix has a determinant of zero, raise an exception.
    if not __check_matrix_has_inverse(key_pseudomatrix):
        raise ValueError("Key cannot be applied to encrypt the ciphertext")
    
    # Get padding size
    padding_size = math.ceil(math.sqrt(len(key_pseudomatrix)))

    # Decrypt the numeral ciphertext
    key_matrix = __make_matrix(key_pseudomatrix)
    decrypt_key_matrix = __key_inv_matrix(key_matrix)
    numeral_plaintext = []
    for i in range(0, len(numeral_ciphertext), padding_size):
        current_part = np.array(numeral_ciphertext[i:i+padding_size]) \
                        .reshape((padding_size, 1))
        decrypt_part = np.matmul(decrypt_key_matrix, current_part) % 26
        decrypt_part = np.asarray(decrypt_part).reshape(padding_size).round().astype(int)
        numeral_plaintext += decrypt_part.tolist()
    
    plaintext = "".join([__alphabetize_numerals(x) for x in numeral_plaintext])
    return plaintext

if __name__ == '__main__':
    key = "heru kntlx"
    encrypted_key = hill_encrypt("OK", key)
    print(encrypted_key)
    decrypted_key = hill_decrypt(encrypted_key, key)
    print(decrypted_key)
