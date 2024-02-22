import json
import base64
from fastapi import APIRouter, Request, UploadFile, File

from src.utils.hill import hill_decrypt, hill_encrypt

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
async def hill_encrypt_router(request: Request):
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
async def hill_decrypt_router(request: Request):
    # Get request details
    body = await request.body()
    decoded_body = json.loads(body.decode('utf-8'))
    base64_encoded = decoded_body.get('encoded_base64toggle')
    if base64_encoded is not None and base64_encoded == "on":
        plaintext = base64.b64decode(decoded_body['plaintext']).decode('utf-8')
    else:
        plaintext = decoded_body['plaintext']
    key = decoded_body['key']

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