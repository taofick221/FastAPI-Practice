# Query Parameters(default)
from fastapi import FastAPI
app=FastAPI()

@app.get("/blog")
def show_comment(limit=10,published:bool=True):
    if published:
       return {f"{limit} blog was published"}
    else:
        return{"Message:"f"{limit} blog was not published"}


# # optional parameters (pizza order)

@app.get("/pizza/{pizza_id}")
def order_pizza(pizza_id:int,topping1:str|None=None,topping2:str|None=None):
    pizza={"pizza_id":pizza_id,"base":"cheese"}
    toppings=[]
    if topping1:
        toppings.append(topping1)
    if topping2:
        toppings.append(topping2)

    if toppings:
        pizza["toppings"]=toppings
    else:
        pizza["toppings"]=["Default topping:tomato sauce"]
    return pizza


# Required query parameters
@app.get("/pizza/{pizza_id}")
def order_pizza(pizza_id:int,topping1:str):
    return{"Order number":f"{pizza_id} and extra toppings {topping1}"}




@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item