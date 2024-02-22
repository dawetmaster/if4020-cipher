from fastapi import APIRouter, File, UploadFile, Response

from src.utils.extendedVigenere import extended_vigenere_decrypt, extended_vigenere_encrypt

# Extende, key: strd Vigenere Cipher
# Using 256 ASCII characters

#TODO: Add parse from file and to file

router = APIRouter(
    prefix="/extended-vigenere",
    tags=["extended-vigenere"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def extended_vigenere():
    return "Extended Vigenere Cipher API"

@router.post("/encrypt")
def extended_vigenere_encrypt_router(key: str, file: UploadFile = File(...)):
    try:
        content = file.file.read()
        extension = file.filename.split('.')[-1]
        encrypted_content = extended_vigenere_encrypt(content, key)

        # TODO: store filename and extension
        return Response(
            encrypted_content,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename=encrypted.{extension}'}
        )
    except Exception as e:
        return {"error": str(e)}

@router.post("/decrypt")
def extended_vigenere_decrypt_router(key: str, file: UploadFile = File(...)):
    try:
        content = file.file.read()
        extension = file.filename.split('.')[-1]
        decrypted_content = extended_vigenere_decrypt(content, key)

        # TODO: store filename and extension
        return Response(
            content,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename=decrypted.{extension}'}
        )
    except Exception as e:
        return {"error": str(e)}