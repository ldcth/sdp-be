from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    username: str
    password: str
    date: str
    gender: bool
    info: str
    role: str 
    cart: list[str]
    history: list[str]