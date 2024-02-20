from fastapi import APIRouter

from be.utils.affine import affine_decrypt, affine_encrypt

# Affine Cipher
# Using 26 letters of the alphabet

router = APIRouter(
    prefix="/affine",
    tags=["affine"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def affine():
    return "Affine Cipher API"

@router.post("/encrypt")
async def affine_encrypt_router(plaintext: str, m: int, b: int):
    # TODO: add file upload option
    return {
        "status": "success",
        "ciphertext": affine_encrypt(plaintext, m, b)
    }

@router.post("/decrypt")
async def affine_decrypt_router(ciphertext: str, m: int, b: int):
    # TODO: add file upload option
    return {
        "status": "success",
        "plaintext": affine_decrypt(ciphertext, m, b)
    }