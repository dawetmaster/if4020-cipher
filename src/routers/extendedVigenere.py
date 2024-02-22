from fastapi import APIRouter, File, UploadFile, Response

from src.utils.extendedVigenere import extended_vigenere_decrypt, extended_vigenere_encrypt

# Extende, key: strd Vigenere Cipher
# Using 256 ASCII characters

router = APIRouter(
    prefix="/extended-vigenere",
    tags=["extended-vigenere"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def extended_vigenere():
    return "Extended Vigenere Cipher API"

@router.post("/encryptfile")
def extended_vigenere_encrypt_router(key: str, file: UploadFile = File(...)):
    try:
        content = file.file.read()
        encrypted_content = extended_vigenere_encrypt(content, key, file.filename)

        return Response(
            encrypted_content,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename=encrypted.dat'}
        )
    except Exception as e:
        return {"error": str(e)}

@router.post("/decryptfile")
def extended_vigenere_decrypt_router(key: str, file: UploadFile = File(...)):
    try:
        content = file.file.read()
        decrypted_content = extended_vigenere_decrypt(content, key)

        filename = decrypted_content[:decrypted_content.index(b'\x00')].decode('utf-8')

        return Response(
            decrypted_content,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename={filename}'}
        )
    except Exception as e:
        return {"error": str(e)}