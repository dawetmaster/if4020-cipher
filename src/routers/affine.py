from fastapi import APIRouter, UploadFile, File

from src.utils.affine import affine_decrypt, affine_encrypt

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
    return {
        "status": "success",
        "ciphertext": affine_encrypt(plaintext, m, b)
    }

@router.post("/encryptfile")
async def affine_encrypt_router_file(m: int, b: int, file: UploadFile = File(...)):
  try:
    contents = await file.read()
    plaintext = contents.decode("utf-8")
    return {
        "status": "success",
        "ciphertext": affine_encrypt(plaintext, m, b)
    }
  except Exception as e:
    return {
        "status": "error",
        "message": str(e)
    }

@router.post("/decrypt")
async def affine_decrypt_router(ciphertext: str, m: int, b: int):
    return {
        "status": "success",
        "plaintext": affine_decrypt(ciphertext, m, b)
    }

@router.post("/encryptfile")
async def affine_decrypt_router_file(m: int, b: int, file: UploadFile = File(...)):
  try:
    contents = await file.read()
    ciphertext = contents.decode("utf-8")
    return {
        "status": "success",
        "ciphertext": affine_decrypt(ciphertext, m, b)
    }
  except Exception as e:
    return {
        "status": "error",
        "message": str(e)
    }