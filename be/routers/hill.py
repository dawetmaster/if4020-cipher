from fastapi import APIRouter, UploadFile, File

from be.utils.hill import hill_decrypt, hill_encrypt

# Standard hill Cipher
# Using 26 letters of the alphabet

router = APIRouter(
    prefix="/hill",
    tags=["hill"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def hill():
    return "Hill Cipher API"

@router.post("/encrypt")
async def hill_encrypt_router(plaintext: str, key: str):
    return {
        "status": "success",
        "ciphertext": hill_encrypt(plaintext, key)
    }

# TODO: find a way to handle optional file upload in FastAPI
@router.post("/encryptfile")
async def hill_encrypt_router_file(key: str, file: UploadFile = File(...)):
  try:
    contents = await file.read()
    plaintext = contents.decode("utf-8")
    return {
        "status": "success",
        "ciphertext": hill_encrypt(plaintext, key)
    }
  except Exception as e:
    return {
        "status": "error",
        "message": str(e)
    }

@router.post("/decrypt")
async def hill_decrypt_router(ciphertext: str, key: str):
    return {
        "status": "success",
        "plaintext": hill_decrypt(ciphertext, key)
    }

@router.post("/decryptfile")
async def hill_decrypt_router_file(key: str, file: UploadFile = File(...)):
  try:
    contents = await file.read()
    ciphertext = contents.decode("utf-8")
    return {
        "status": "success",
        "ciphertext": hill_decrypt(ciphertext, key)
    }
  except Exception as e:
    return {
        "status": "error",
        "message": str(e)
    }