from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Restaurant
from app.schemas.restaurant import Restaurant as RestaurantSchema, RestaurantBase

router = APIRouter()

@router.post("/", response_model=RestaurantSchema)
def create_restaurant(restaurant: RestaurantBase, db: Session = Depends(get_db)):
    db_rest = Restaurant(**restaurant.model_dump())
    db.add(db_rest)
    db.commit()
    db.refresh(db_rest)
    return db_rest

@router.get("/", response_model=list[RestaurantSchema])
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).all()