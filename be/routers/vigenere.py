from fastapi import APIRouter

# Standard Vigenere Cipher
# Using 26 letters of the alphabet

router = APIRouter(
    prefix="/vigenere",
    tags=["vigenere"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def vigenere():
    return "Vigenere Cipher API"

@router.post("/encrypt")
async def vigenere_encrypt(plaintext: str, key: str):
    # make plaintext and key lowercase
    plaintext = plaintext.lower()
    key = key.lower()

    # remove non-alphabet characters
    plaintext = "".join(filter(str.isalpha, plaintext))

    # repeat key
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]

    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += (chr((ord(plaintext[i]) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))).upper()

    return {
        "status": "success",
        "ciphertext": ciphertext
    }

@router.post("/decrypt")
async def vigenere_decrypt(ciphertext: str, key: str):
    # make ciphertext and key lowercase
    ciphertext = ciphertext.lower()
    key = key.lower()

    # remove non-alphabet characters
    plaintext = "".join(filter(str.isalpha, ciphertext))

    # repeat key
    key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)]

    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += (chr((ord(ciphertext[i]) - ord(key[i]) + 26) % 26 + ord('a'))).upper()

    return {
        "status": "success",
        "plaintext": plaintext
    }