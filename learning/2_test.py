from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message":"hello untoc"}

# make items....
items = [
    {"item_id":1, "item_name":"water1", "item_price":100},
    {"item_id":2, "item_name":"water2", "item_price":200},
    {"item_id":3, "item_name":"water3", "item_price":300},
    {"item_id":4, "item_name":"water4", "item_price":400},
    {"item_id":5, "item_name":"water5", "item_price":500},
    {"item_id":6, "item_name":"water6", "item_price":600}
]
# 1. get
# 1-1. get all item
@app.get("/item/get_all_item")
def get_all_item(skip:int = 0, limit:int = 10):
    return items[skip : skip + limit]

# 1-2. get one item
@app.get("/item/get_item/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["item_id"] == item_id:
            return item

# 2. post
# 2-1. create item
@app.post("/item/create_item")
def create_item(item_id:int, item_name:str, item_price:int):
    # item_id가 중복되어 있는지 확인
    for item in items:
        if item["item_id"] == item_id:
            return {"error message":"같은 아이디에 해당하는 아이템이 있습니다."}
    # 입력한 item을 append
    items.append({"item_id":item_id,
                  "item_name":item_name,
                  "item_price":item_price})
    return items
    
# 3. put
# 3-1. modify item
@app.put("/item/update_item/{item_id}")
def update_item(item_id: int, item_name: str, item_price: int):
    for item in items:
        if item["item_id"] == item_id:
            item["item_name"] = item_name
            item["item_price"] = item_price
            return item
    
    return {"error": "Item not found"}













# 4. delete
# 4-1. delete item


###################################
# path parameter

# query parameter

# request body

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


