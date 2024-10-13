from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    item_name: str
    item_price: int

class Create_item(Item):
    amount: int
    create_at: str
    create_date: datetime

class Modify_item(Item):
    amount: int 