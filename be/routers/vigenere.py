from fastapi import APIRouter

# Standard Vigenere Cipher
# Using 26 letters of the alphabet

router = APIRouter(
    prefix="/vigenere",
    tags=["vigenere"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def vigenere():
    return "Vigenere Cipher API"