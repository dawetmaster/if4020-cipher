from fastapi import APIRouter, UploadFile, File, Request
from fastapi.templating import Jinja2Templates

from src.utils.vigenere import vigenere_decrypt, vigenere_encrypt

import json

# Standard Vigenere Cipher
# Using 26 letters of the alphabet

router = APIRouter(
    prefix="/vigenere",
    tags=["vigenere"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def vigenere(request: Request):
   return Jinja2Templates(directory="src/templates").TemplateResponse("index.html", {
      "ciphertype_name": "Vigenere",
      "ciphertype": "vigenere",
      "request": request
   })

@router.post("/encrypt")
async def vigenere_encrypt_router(request: Request):
    # Get request details
    body = await request.body()
    decoded_body = json.loads(body.decode('utf-8'))
    plaintext = decoded_body['plaintext']
    key = decoded_body['key']

    # Return the request details as output
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
async def vigenere_decrypt_router(request: Request):
    # Get request details
    body = await request.body()
    decoded_body = json.loads(body.decode('utf-8'))
    ciphertext = decoded_body['ciphertext']
    key = decoded_body['key']

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