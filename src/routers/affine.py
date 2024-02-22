import json
import base64
from fastapi import APIRouter, Request, UploadFile, File

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
async def affine_encrypt_router(request: Request):
    # Get request details
    body = await request.body()
    decoded_body = json.loads(body.decode('utf-8'))
    base64_encoded = decoded_body.get('encoded_base64toggle')
    if base64_encoded is not None and base64_encoded == "on":
        plaintext = base64.b64decode(decoded_body['plaintext']).decode('utf-8')
    else:
        plaintext = decoded_body['plaintext']
    key = decoded_body['key']
    # Return the request details as output

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
async def affine_decrypt_router(request: Request):
    # Get request details
    body = await request.body()
    decoded_body = json.loads(body.decode('utf-8'))
    ciphertext = decoded_body['ciphertext']
    key = decoded_body['key']

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