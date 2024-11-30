from pydantic import BaseModel , ValidationError

class Order(BaseModel):
    id: int
    userid: int
    bookid: list[int]
    quantity: list[int]
    name:str
    add: str
    info: str 
    price: float
    state: str = "create"


def create_order(data: dict)-> Order:
    # if "name" not in data or not data["name"]:
    #     return None
    # return Book(**data)
    try:
        if "userid" not in data or not data["userid"]:
            return None

        return Order(**data)
    except ValidationError as e:
        # print(f"Validation error: {e.json()}")
        return None
