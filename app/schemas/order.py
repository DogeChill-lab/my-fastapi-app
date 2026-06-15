from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderItemResponse(BaseModel):
    menu_item_id: int
    quantity: int
    price: float

class OrderResponse(BaseModel):
    id: int
    status: str
    total_price: float
    created_at: str
    items: List[OrderItemResponse]