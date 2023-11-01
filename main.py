from fastapi import FastAPI

from .models import registration

app = FastAPI()


@app.post("/")
async def register_parking():
    return {"message": "Hello from the post route"}


@app.put("/")
async def put():
    return {"message": "Hello from the put route"}


@app.delete("/")
async def delete():
    return {"message": "Hello from the delete route"}


@app.get("/items")
async def list_items():
    return {"message": "list items route"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
