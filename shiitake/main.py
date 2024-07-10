from fastapi import FastAPI
from pydantic import BaseModel
from uvicorn import run

app = FastAPI()


class Item(BaseModel):
    data: str


@app.post("/api")
async def create_item(item: Item):
    return item.data


def main():
    run(app, host="0.0.0.0", port=8000)
