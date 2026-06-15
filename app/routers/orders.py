from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Order, OrderItem, MenuItem
from app.schemas.order import OrderCreate, OrderResponse, OrderItemResponse

router = APIRouter()


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    total = 0
    order_items = []

    for item in order.items:
        menu_item = db.query(MenuItem).filter(MenuItem.id == item.menu_item_id).first()
        if not menu_item:
            raise HTTPException(status_code=404, detail=f"Item {item.menu_item_id} not found")
        total += menu_item.price * item.quantity
        order_items.append(OrderItem(menu_item_id=item.menu_item_id, quantity=item.quantity))

    new_order = Order(total_price=total, status="pending")
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for oi in order_items:
        oi.order_id = new_order.id
        db.add(oi)
    db.commit()

    return new_order