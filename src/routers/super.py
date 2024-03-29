from fastapi import APIRouter, File, Response, UploadFile
from src.utils import transpose

from src.utils.extendedVigenere import extended_vigenere_decrypt, extended_vigenere_encrypt

# Super Encryption Cipher

router = APIRouter(
    prefix="/super",
    tags=["super"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def super_encryption():
    return "Super Encryption Cipher API"

@router.post("/encryptfile")
async def super_encryption_encrypt_router(key: str, col: int = 4, file: UploadFile = File(...)):
    try:
        content = file.file.read()
        encrypted_content = transpose.transpose_bytes(extended_vigenere_encrypt(content, key, file.filename), col)

        return Response(
            encrypted_content,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename=encrypted.dat'}
        )
    except Exception as e:
        return {"error": str(e)}

@router.post("/decryptfile")
async def super_encryption_encrypt_router(key: str, col: int = 4, file: UploadFile = File(...)):
    try:
        content = file.file.read()
        decrypted_content = transpose.transpose_back_bytes(extended_vigenere_decrypt(content, key), col)

        filename = decrypted_content[:decrypted_content.index(b'\x00')].decode('utf-8')

        return Response(
            decrypted_content,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename={filename}'}
        )
    except Exception as e:
        return {"error": str(e)}