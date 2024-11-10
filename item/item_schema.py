from pydantic import BaseModel

class Create_model(BaseModel):
    item_id:int
    item_name: str
    item_price: int