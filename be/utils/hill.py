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

def __determinant(mat: list) -> float:
    # Ensure that mat is a list of list of integers (a square matrix)
    # By default, repeat the key (partially) to make a higher nxn matrix
    mat = np.array(mat)
    upper_bound = math.ceil(math.sqrt(len(mat)))
    # Resize to nxn matrix
    mat = np.resize(mat, (upper_bound, upper_bound))
    det = np.linalg.det(mat)
    return det

def __check_matrix_has_inverse(mat: list) -> bool:
    # Check using numpy as the determinant is a float
    return not np.isclose(__determinant(mat), 0.0, rtol=1e-09, atol=1e-09)

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

if __name__ == '__main__':
    matrix = [2, 2, 0, 2]
    print(__determinant(matrix))
    print(__check_matrix_has_inverse(matrix))

