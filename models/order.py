from pydantic import BaseModel

class Book(BaseModel):
    id: str
    userid: str
    bookid: list[str]
    quantity: list[int]
    add: str
    info: str 
    price: float
    state: str
