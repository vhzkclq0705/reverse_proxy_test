from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    a = 1
    b = 2
    return {"Hello": a + b}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}