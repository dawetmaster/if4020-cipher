import json
import base64
from fastapi import APIRouter, Request

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
async def autokey_vigenere_encrypt_router(request: Request):
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
        "ciphertext": autokey_vigenere_encrypt(plaintext, key)
    }

@router.post("/decrypt")
async def autokey_vigenere_decrypt_router(request: Request):
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
        "plaintext": autokey_vigenere_decrypt(ciphertext, key)
    }