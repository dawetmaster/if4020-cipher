from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from be.routers import affine, extendedVigenere, super, vigenere

app = FastAPI()

templates = Jinja2Templates(directory="be/templates")

app.include_router(affine.router)
app.include_router(extendedVigenere.router)
app.include_router(super.router)
app.include_router(vigenere.router)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})