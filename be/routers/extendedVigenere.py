from fastapi import APIRouter, File, UploadFile, Response

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
def extended_vigenere_encrypt(key: str, file: UploadFile = File(...)):
    try:
        content = file.file.read()
        extension = file.filename.split('.')[-1]

        # encrypt per byte using key
        for i in range(len(content)):
            # if using bytes, it couldn't be added with int as byte range is 0-255 so use XOR
            content = content[:i] + bytes([content[i] ^ ord(key[i % len(key)])]) + content[i+1:]

        return Response(
            content,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename=encrypted.{extension}'}
        )
    except Exception as e:
        return {"error": str(e)}

@router.post("/decrypt")
def extended_vigenere_decrypt(key: str, file: UploadFile = File(...)):
    try:
        content = file.file.read()
        extension = file.filename.split('.')[-1]

        # encrypt per byte using key
        for i in range(len(content)):
            # if using bytes, it couldn't be added with int as byte range is 0-255 so use XOR
            content = content[:i] + bytes([content[i] ^ ord(key[i % len(key)])]) + content[i+1:]

        return Response(
            content,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename=decrypted.{extension}'}
        )
    except Exception as e:
        return {"error": str(e)}