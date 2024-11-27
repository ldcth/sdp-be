class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return {"message": f"Added {item} to cart"}

cart = Cart()

from fastapi import APIRouter

router = APIRouter()

@router.post("/cart/add/{item}")
def add_to_cart(item: str):
    return cart.add_item(item)