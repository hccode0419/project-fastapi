from fastapi import FastAPI

app = FastAPI()

items = [
    {"item_id": 1, "item_name":"untoc", "item_price":15000},
    {"item_id": 2, "item_name":"phone", "item_price":35000},
    {"item_id": 3, "item_name":"computer", "item_price":24000},
    {"item_id": 4, "item_name":"pencil", "item_price":1000},
    {"item_id": 5, "item_name":"mouse", "item_price":2000},
    {"item_id": 6, "item_name":"water", "item_price":100}
]

@app.get("/")
def root():
    return {"message":"hello UNTOC"}

@app.get("/get_items")
def get_items(skip:int = 0, limit:int = 10):
    return items[skip : skip + limit]

@app.get("/get_item")
def get_item(item_id:int):
    for item in items:
        if item["item_id"] == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/create_item/{item_id}")
def create_itme(item_id: int , item_name:str, item_price: int):
    items.append({"item_id":item_id, "item_name":item_name, "item_price": item_price})

    return items[item_id - 1]

@app.put("/update_item/{item_id}")
def update_item(item_id: int, item_name: str, item_price: int):
    for item in items:
        if item["item_id"] == item_id:
            item["item_name"] = item_name
            item["item_price"] = item_price
            return item
    
    return {"error": "Item not found"}

@app.delete("/delete_item/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item["item_id"] == item_id:
            deleted_item = items.pop(item_id-1)
            return {"message": "deleted", "deleted_item":deleted_item}
    return {"error": "Item not found"}

