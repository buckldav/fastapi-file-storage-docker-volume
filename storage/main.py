from fastapi import FastAPI
from decouple import config
from pydantic import BaseModel
import aiofiles
import secrets


class Settings(BaseModel):
    base_staticfiles_path = config("STATICFILES_PATH")
CONFIG = Settings()


app = FastAPI(debug=True)


@app.get("/")
async def hello():
    return {"hello": "world"}


@app.get("/{path}")
async def file(path: str):
    filepath = CONFIG.base_staticfiles_path + f"/{path}"

    async with aiofiles.open(filepath, "w") as f:
        await f.write(secrets.token_urlsafe(20) + f"\n{filepath}")

    return {"filepath": filepath}
