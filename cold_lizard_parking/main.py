from fastapi import FastAPI

app = FastAPI()


# Check if car is parked in given spot
@app.get("/", description="This is our first route.", deprecated=True)
async def root():
    return {"message": "Hello world!"}


# Register parking
@app.post("/")
async def post():
    return {"message": "Hello from the post route"}


# Delete all parking for a given registration number
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
