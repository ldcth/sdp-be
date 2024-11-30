from fastapi import APIRouter, HTTPException
from models.order import order
from repositories.order_repository import order_repository

router = APIRouter()

@router.get("/orders")
def get_orders():
    orders = order_repository.get_all_orders()
    return orders

@router.get("/orders/{order_id}")
def get_order(order_id: str):
    order = order_repository.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="order not found")
    return order

@router.post("/orders")
def create_order(order: order):
    return order_repository.add_order(order.dict())

@router.put("/orders/{order_id}")
def update_order(order_id: str, order: order):
    return order_repository.update_order(order_id, order.dict())

@router.delete("/orders/{order_id}")
def delete_order(order_id: str):
    order_repository.delete_order(order_id)
    return {"message": "order deleted successfully"}