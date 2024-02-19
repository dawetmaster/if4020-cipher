from fastapi import APIRouter

# Super Encryption Cipher

router = APIRouter(
    prefix="/super",
    tags=["super"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def super_encryption():
    return "Super Encryption Cipher API"