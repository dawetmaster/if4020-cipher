from fastapi import APIRouter

from src.utils.playfair import playfair_decrypt, playfair_encrypt

# Playfair Cipher
# Using 26 letters of the alphabet

router = APIRouter(
    prefix="/playfair",
    tags=["playfair"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def playfair():
    return "Playfair Cipher API"

@router.post("/encrypt")
async def playfair_encrypt_router(plaintext: str, key: str):
    return {
        "status": "success",
        "ciphertext": playfair_encrypt(plaintext, key)
    }

@router.post("/decrypt")
async def playfair_decrypt_router(ciphertext: str, key: str):
    return {
        "status": "success",
        "plaintext": playfair_decrypt(ciphertext, key)
    }
