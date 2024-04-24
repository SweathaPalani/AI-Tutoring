from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# data model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# In-memory store for items
items = {}

@app.get("/")
def read_root():
    return {"Hello": "Worldd"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
