from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    user_id: str
    password: str
    user_name: str
    phone_number: str
    email: str
    create_date: datetime
    
