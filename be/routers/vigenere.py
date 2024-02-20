from fastapi import APIRouter

from be.utils.vigenere import vigenere_decrypt, vigenere_encrypt

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
async def vigenere_encrypt_router(plaintext: str, key: str):
    return {
        "status": "success",
        "ciphertext": vigenere_encrypt(plaintext, key)
    }

@router.post("/decrypt")
async def vigenere_decrypt_router(ciphertext: str, key: str):
    return {
        "status": "success",
        "plaintext": vigenere_decrypt(ciphertext, key)
    }