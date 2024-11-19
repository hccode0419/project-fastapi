from fastapi import FastAPI, APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from .user_schema import User

from database import get_userdb

from models import User as User_model

router = APIRouter(
    prefix="/user"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)

@router.post("/sign_up", response_model = User)
def sign_up(user: User, 
            user_db : Session = Depends(get_userdb)):
    
    # 아이디 중복 확인
    
    # 전화번호 중복 확인
    
    
    
    
    user_info = User_model(user_id = user.user_id,
                     password=user.password,
                     user_name=user.user_name,
                     phone_number=user.phone_number,
                     email=user.email,
                     create_date=user.create_date)
    
    insert_data(user_db, user_info)

    return user_info
@router.get("/log_in")
def log_in():
    pass

