from fastapi import APIRouter, UploadFile, File

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

# TODO: find a way to handle optional file upload in FastAPI
@router.post("/encryptfile")
async def vigenere_encrypt_router_file(key: str, file: UploadFile = File(...)):
  try:
    contents = await file.read()
    plaintext = contents.decode("utf-8")
    return {
        "status": "success",
        "ciphertext": vigenere_encrypt(plaintext, key)
    }
  except Exception as e:
    return {
        "status": "error",
        "message": str(e)
    }

@router.post("/decrypt")
async def vigenere_decrypt_router(ciphertext: str, key: str):
    return {
        "status": "success",
        "plaintext": vigenere_decrypt(ciphertext, key)
    }

@router.post("/decryptfile")
async def vigenere_decrypt_router_file(key: str, file: UploadFile = File(...)):
  try:
    contents = await file.read()
    ciphertext = contents.decode("utf-8")
    return {
        "status": "success",
        "ciphertext": vigenere_decrypt(ciphertext, key)
    }
  except Exception as e:
    return {
        "status": "error",
        "message": str(e)
    }