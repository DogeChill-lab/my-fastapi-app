from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    name: str
    description: str
    price: float
    image: str = "default.jpg"
    restaurant_id: int
    category_id: int = 1

class MenuItem(MenuItemBase):
    id: int

    class Config:
        from_attributes = True