from fastapi import FastAPI

app = FastAPI()

items = {
    1 : {"item_name":"untoc", "item_price":15000},
    2 : {"item_name":"phone", "item_price":35000},
    3 : {"item_name":"computer", "item_price":24000},
    4 : {"item_name":"pencil", "item_price":1000},
    5 : {"item_name":"mouse", "item_price":2000},
    6 : {"item_name":"water", "item_price":100}
}

@app.get("/")
def root():
    return {"message":"hello UNTOC"}


@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id:int):
    return items[item_id]

@app.post("/create_item")
def create_itme(item_id: int , item_name, item_price: int):
    items[item_id] = {"item_name": item_name, "item_price":item_price}

    return items[item_id]

