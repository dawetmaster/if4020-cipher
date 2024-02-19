from fastapi import APIRouter

# Affine Cipher
# Using 26 letters of the alphabet

router = APIRouter(
    prefix="/affine",
    tags=["affine"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def affine():
    return "Affine Vigenere Cipher API"