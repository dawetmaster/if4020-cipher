def __remove_repeating_characters(input_string: str):
    seen = set()
    output_string = ''
    for char in input_string:
        if char not in seen:
            output_string += char
            seen.add(char)
    return output_string

def __add_remaining_alphabets(input_string: str):
    # 'j' is not allowed
    alphabets = list("abcdefghiklmnopqrstuvwxyz")
    existing_alphabets = set(input_string)
    output_string = input_string
    for alphabet in alphabets:
        if alphabet not in existing_alphabets:
            output_string += alphabet
    return output_string

def __encrypt_char_pair(char_pair: str, key: str):
    # key is an array with length 25
    char1_index: int = key.index(char_pair[0])
    char2_index: int = key.index(char_pair[1])
    # Check same vertical index
    if (char1_index % 5) == (char2_index % 5):
        encrypted_char1 = key[(char1_index + 5) % 25]
        encrypted_char2 = key[(char2_index + 5) % 25]
        return "".join([encrypted_char1, encrypted_char2])
    # check same horizontal index
    if (char1_index // 5) == (char2_index // 5):
        _quotient = char1_index // 5
        encrypted_char1 = key[5 * _quotient + ((char1_index % 5 + 1) % 5)]
        encrypted_char2 = key[5 * _quotient + ((char2_index % 5 + 1) % 5)]
        return "".join([encrypted_char1, encrypted_char2])
    # or else, rotate it
    row1, col1 = char1_index // 5 , char1_index % 5
    row2, col2 = char2_index // 5 , char2_index % 5
    encrypted_char1 = key[row1 * 5 + col2]
    encrypted_char2 = key[row2 * 5 + col1]
    return "".join([encrypted_char1, encrypted_char2])

def __decrypt_char_pair(char_pair: str, key: str):
    # key is an array with length 25
    char1_index: int = key.index(char_pair[0])
    char2_index: int = key.index(char_pair[1])
    # Check same vertical index
    if (char1_index % 5) == (char2_index % 5):
        encrypted_char1 = key[(char1_index - 5) % 25]
        encrypted_char2 = key[(char2_index - 5) % 25]
        return "".join([encrypted_char1, encrypted_char2])
    # check same horizontal index
    if (char1_index // 5) == (char2_index // 5):
        _quotient = char1_index // 5
        encrypted_char1 = key[5 * _quotient + ((char1_index % 5 - 1) % 5)]
        encrypted_char2 = key[5 * _quotient + ((char2_index % 5 - 1) % 5)]
        return "".join([encrypted_char1, encrypted_char2])
    # or else, rotate it
    row1, col1 = char1_index // 5 , char1_index % 5
    row2, col2 = char2_index // 5 , char2_index % 5
    encrypted_char1 = key[row1 * 5 + col2]
    encrypted_char2 = key[row2 * 5 + col1]
    return "".join([encrypted_char1, encrypted_char2])

def __prepare_cryptkey(key: str):
    # Remove 'j' from the key
    key = key.replace('j', '')

    # Remove repeating characters from the key
    key = __remove_repeating_characters(key)

    # Add remaining alphabet characters to the key without 'j'
    key = __add_remaining_alphabets(key)
    return key

def playfair_encrypt(plaintext: str, key: str):
    # Make the plaintext and key lowercase
    plaintext = plaintext.lower()
    key = key.lower()

    # Remove non-alphabet characters
    plaintext = "".join(filter(str.isalpha, plaintext))
    key = "".join(filter(str.isalpha, key))

    # Prepare cryptkey
    key = __prepare_cryptkey(key)

    # Here's the magic: Read the plaintext by two characters each read,
    # then insert 'x' into the plaintext in case there is a group
    # consisting of same characters or have an odd length in the end.
    # Idea: use 'while' instead of 'for' because the length of the
    # plaintext is possibly increasing.
    i = 0
    while (i < len(plaintext) - 1):
        if plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + 'x' + plaintext[i+1:]
        i += 2
    if len(plaintext) % 2 != 0:
        added_alphabet = 'x' if plaintext[-1] != 'x' else 'y'
        plaintext = plaintext + added_alphabet

    # Another magic: the encryption algorithm
    # Read the plaintext as groups of two characters.
    # Here's the method:
    # 1. Locate the characters in the key matrix.
    # 2a. If the characters are in the same column, shift one row forward,
    # 2b. If the characters are in the same row, shift one column forward,
    # 2c. Otherwise, rotate the characters by a "rectangle" formed by the two characters.
    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        encrypted_chars = __encrypt_char_pair(plaintext[i:i+2], key)
        encrypted_text += encrypted_chars

    return encrypted_text

def playfair_decrypt(ciphertext: str, key: str):
    # Make the ciphertext and key lowercase
    ciphertext = ciphertext.lower()
    key = key.lower()

    # Remove non-alphabet characters
    ciphertext = "".join(filter(str.isalpha, ciphertext))
    key = "".join(filter(str.isalpha, key))

    # Prepare cryptkey
    key = __prepare_cryptkey(key)

    # Decrypt with magic!
    decrypted_text = ""
    for i in range(0, len(ciphertext), 2):
        decrypted_chars = __encrypt_char_pair(ciphertext[i:i+2], key)
        decrypted_text += decrypted_chars

    return decrypted_text


if __name__ == '__main__':
    encrypted_key = playfair_encrypt("ACE OF BASx", "lemah ya kamu")
    print(encrypted_key)
    decrypted_key = playfair_decrypt(encrypted_key, "lemah ya kamu")
    print(decrypted_key)
