from pydantic import BaseModel

class Author(BaseModel):
    id: str
    name: str
    bookid: list[str]  
