from pydantic import BaseModel
from datetime import datetime

# 입력 받는 양식
class Create_item(BaseModel):
    item_name: str
    item_price: int
    amount: int
    create_at: str
    create_date: datetime