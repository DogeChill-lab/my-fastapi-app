from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import MenuItem
from app.schemas.menu import MenuItem as MenuItemSchema, MenuItemBase

router = APIRouter()

@router.get("/restaurant/{restaurant_id}", response_model=list[MenuItemSchema])
def get_menu(restaurant_id: int, db: Session = Depends(get_db)):
    return db.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id).all()

@router.post("/", response_model=MenuItemSchema)
def create_menu_item(item: MenuItemBase, db: Session = Depends(get_db)):
    db_item = MenuItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item