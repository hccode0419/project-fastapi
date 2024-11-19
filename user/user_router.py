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
    check_user_id = user_db.query(User_model).filter(User_model.user_id == user.user_id).first()
    if check_user_id:
        raise HTTPException(status_code=404, detail="해당 아이디는 존재하는 아이디입니다.")
    
    # 전화번호 중복 확인
    check_phone_number = user_db.query(User_model).filter(User_model.phone_number == user.phone_number).first()
    if check_phone_number:
        raise HTTPException(status_code=404, detail="중복되는 전화번호입니다.")
    
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

