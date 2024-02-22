from fastapi import APIRouter

from src.utils.autokeyVigenere import autokey_vigenere_decrypt, autokey_vigenere_encrypt

# Standard Vigenere Cipher
# Using 26 letters of the alphabet

router = APIRouter(
    prefix="/autokey-vigenere",
    tags=["autokey-vigenere"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def vigenere():
    return "Vigenere Cipher API"

@router.post("/encrypt")
async def autokey_vigenere_encrypt_router(plaintext: str, key: str):
    return {
        "status": "success",
        "ciphertext": autokey_vigenere_encrypt(plaintext, key)
    }

@router.post("/decrypt")
async def autokey_vigenere_decrypt_router(ciphertext: str, key: str):
    return {
        "status": "success",
        "plaintext": autokey_vigenere_decrypt(ciphertext, key)
    }