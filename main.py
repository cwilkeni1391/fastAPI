from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

#Example root path
@app.get("/")
def root():
    return {"Hello" : "World"}

#example post route
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    if limit > len(items):
        return items[0:len(items)]
    else:
        return items[0:limit]

#get item based on id or position in list
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail='Item not Found')

