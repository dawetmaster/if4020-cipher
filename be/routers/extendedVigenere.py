from fastapi import APIRouter

# Extended Vigenere Cipher
# Using 256 ASCII characters

router = APIRouter(
    prefix="/extended-vigenere",
    tags=["extended-vigenere"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def extended_vigenere():
    return "Extended Vigenere Cipher API"