from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    username: str
    password: str
    date: str
    gender: bool
    role: str 
    cart: list[str]