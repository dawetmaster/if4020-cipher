from fastapi import APIRouter, Request

from src.utils.playfair import playfair_decrypt, playfair_encrypt

import json
import base64

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
async def playfair_encrypt_router(request: Request):
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
        "ciphertext": playfair_encrypt(plaintext, key)
    }

@router.post("/decrypt")
async def playfair_decrypt_router(request: Request):
    # Get request details
    body = await request.body()
    decoded_body = json.loads(body.decode('utf-8'))
    ciphertext = decoded_body['ciphertext']
    key = decoded_body['key']

    return {
        "status": "success",
        "plaintext": playfair_decrypt(ciphertext, key)
    }
