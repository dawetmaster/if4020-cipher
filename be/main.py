from fastapi import FastAPI

from routers import affine, extendedVigenere, super, vigenere

app = FastAPI()

app.include_router(affine.router)
app.include_router(extendedVigenere.router)
app.include_router(super.router)
app.include_router(vigenere.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}