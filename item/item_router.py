from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_itemdb

from .item_schema import Create_item, Modify_item
from models import Item as Item_model

router = APIRouter(
    prefix="/item"
)


def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)



@router.get("/")
def root():
    return {"message":"hello UNTOC"}

@router.get("/get_items")
def get_items(skip:int = 0, limit:int = 10, 
              item_db: Session = Depends(get_itemdb)):
    
    item = item_db.query(Item_model).all()
    if not item:
        raise HTTPException(status_code=404, detail="item 내역이 없습니다.")
    
    return item[skip : skip + limit]

@router.get("/get_item")
def get_item(item_id:int, 
             item_db: Session = Depends(get_itemdb)):
    item = item_db.query(Item_model).filter(Item_model.item_id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"item_id : {item_id} 내역이 없습니다.")

    return item


@router.post("/create_item", response_model=Create_item)
def create_item(item:Create_item, 
                item_db: Session = Depends(get_itemdb)):
    
    create_items = Item_model(item_name=item.item_name, 
                item_price=item.item_price,
                amount=item.amount,
                create_at=item.create_at,
                create_date=item.create_date)

    insert_data(item_db, create_items)

    return create_items

@router.put("/update_item", response_model=Modify_item)
def update_item(item: Modify_item,
                item_id: int,
                item_db: Session = Depends(get_itemdb)):
    
    modify_item = Modify_item(item_name=item.item_name,
                              item_price=item.item_price,
                              amount=item.amount)

    item = item_db.query(Item_model).filter(Item_model.item_id == item_id).first()

    """
    item_db에서 Item_model에 해당하는 table을 들고온 후 Item_model.item_id와 입력한 item_id가 같은 첫번째 row를 들고온다.

    이때 Item_model은 model.py에 작성한 DB table의 양식이다.

    이 형식은 자주 등장할 것이니 기억해주세요!

    """

    if not item:
        raise HTTPException(status_code=404, detail=f"item_id : {item_id} 내역이 없습니다.")

    """
    item이 있는지 확인하여 없으면 예외처리한다.

    """

    item.item_name = modify_item.item_name
    item.item_price = modify_item.item_price
    item.amount = modify_item.amount

    item_db.commit()
    item_db.refresh(item)

    return modify_item

@router.delete("/delete_item")
def delete_item(item_id: int,
                item_db: Session = Depends(get_itemdb)):
    
    
    item = item_db.query(Item_model).filter(Item_model.item_id == item_id)
    
    if not item.first():
        raise HTTPException(status_code=404, detail=f"item_id : {item_id} 내역이 없습니다.")
    
    item.delete()

    item_db.commit()

    return {"message":f"item_id : {item_id} - success delete"}