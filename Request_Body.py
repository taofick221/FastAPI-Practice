from fastapi import FastAPI
from pydantic import BaseModel
app =FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None

@app.post("/items/")
def create(item:Item):
    return item




# Request body + path parameters

@app.put("/items/{item_id}")
def update(item_id:str, item:Item):
    return {"item_id":item_id,"item":item}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
