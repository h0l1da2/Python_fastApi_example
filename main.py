from fastapi import FastAPI
from web import tag, hello

app = FastAPI()

app.include_router(hello.router, prefix="/hello", tags=["Hello"])
app.include_router(tag.router, prefix="/tag", tags=["Tag"])