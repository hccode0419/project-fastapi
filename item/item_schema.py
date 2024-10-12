from pydantic import BaseModel
from datetime import datetime


class Create_item(BaseModel):
    item_name: str
    item_price: int
    amount: int
    create_at: str
    create_date: datetime

